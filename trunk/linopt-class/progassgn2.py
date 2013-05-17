# solves LPs of the form
# max cx
# sub to: Ax <= b

from sympy import *

# requires a feasible basis B for the LP
def solve(A, b, c, B, verbose):
	m, n = A.rows, A.cols
	itr = 0

	# find vertex corresponding to feasible basis B
	AB = A.extract(B, range(n))
	bB = b.extract(B, [0])
	x = AB.LUsolve(bB)
	
	ABi = AB.inv()

	while True:
		itr += 1


		# compute lambda
		l = (c.T*ABi).T
		# check for optimality
		if all(e >= 0 for e in l):
			return x, itr

		# find leaving index B[r]
		r = min(i for i in range(l.rows) if l[i] < 0)

		# compute direction to move int
		d = - ABi[:,r]

		# determine the set K
		K = [i for i in range(m) if (A[i,:]*d)[0] > 0]

		if not K:
			return 'unbounded', itr

		# find entering index e
		e, v = None, None
		for k in K:
			w = (b[k] - (A[k,:]*x)[0]) / ((A[k,:]*d)[0])
			if v is None or w < v:
				v = w
				e = k
		if verbose: 
			print "%d: x.T: " % itr, x.T
			print "    B: ", B
			print "    l.T: ", l.T 
			print "    d.T: ", d.T
			print "    epsilon: ", v
			print "    leaving index B[r]: ", B[r]
			print "    entering index e: ", e
		# update basis
		B[r] = e
		AB[r, :] = A[e, :]
		bB[r, :] = b[e, :]

		# update inverse
		#ABi = AB.inv()
		f = AB[r , :] * ABi

		g = -f
		g[r] = 1 
		g /= f[r]
		
		X = eye(n)
		X[r, :] = g
		
		g[r] -= 1
		ABi += ABi[:,r]*g

		# move to the new vertex
		x = x + v*d

def simplex(A, b, c, B, verbose=False):
	x, itr = solve(A, b, c, B, verbose)

	if x == 'infeasible':
		print 'LP is infeasible'
	elif x == 'unbounded':
		print 'LP is unbounded'
	else:
		print 'Vertex', x.T, 'is optimal'
		print 'Optimal value is', (c.T * x)[0]
		print 'Found after', itr, 'simplex iterations'

if __name__ == '__main__':

	# small example
	A = Matrix([[1, 0, 0, 0],
	     [20, 1, 0, 0],
	     [200, 20, 1, 0],
	     [2000, 200, 20, 1],
	     [-1, 0, 0, 0],
	     [0, -1, 0, 0],
	     [0, 0, -1, 0],
	     [0, 0, 0, -1]])
	b = Matrix([1,100,10000,1000000, 0,0,0,0])
	c = Matrix([1000, 100, 10, 1])
	B = range(4, 8)

	simplex(A, b, c, B, verbose=True)

	A = Matrix([[  3,   0,  10,  10,  -5, -10,   6,  -6,   8,   9,   9,  10,   1,   0, -3,   8,   2,  -4,  -6,  -5,  10,  -4,  -6,  -3,  -7],
		   [  7,   0,   1,   2,  -6,   2,   0,  -3,   2,  -7,  -4,  -3, -10,  -6, -2,  -3,  -8,   8,   7,  -7,   5,   6,   2,   9, -10],
		   [ 10,  10,   8,  -9,  -1,   7,   6,  -2,   1,   7,   0,   3,  -8,   5, -1,  -5,  10,  -6,  -8,   0,   3,  -1,  -3,  -2,   3],
		   [ -4,   1, -10,   2,  -5,   2,   2,   3,  10,  -6,  -8,  -4,   9,   9,  3,  -1, -10,   8,  -5,   0,   3,  -4,   7,  -1,   3],
		   [ -9,  -1,  -8,   0,   0,   7,   1,   7,   1,   3,   5,   1,   0,   7, -5,  -2,   4,   4,   6,  10,   3,   9, -10,   4, -10],
		   [  6,  -6,  -3,   6,   7,   9,   0,  10,  -6,  -2,   9,  -1,   3,  -4, -1,   2,   9,  -4,   6,  -3,  -7,  10,   5,  -6,   7],
		   [ -3,  -7,   9,   1,   3,  -6,  -1,  -2,  -5,   4,   5,  -5,   8,   4,  9,  10, -10, -10,   2,   0,  -5,   7,   1,  10,  -7],
		   [ -5,   0,  -4,   2,   1,   7,  -3,  -7,   4,  -6,  -4,   7,   8,  -8,  6,   0,   7,   8,   4,   8,   7,   5,   4,  -9,  -9],
		   [  1,  -5,  10,   3,  -2,   0,   5,  -6,  -5,   2,  -2,  -4,  -5,   1,  8,  -7,  -9,  -1,   8,  -9,  -5, -10,  10,   1,  -9],
		   [  3,   1,   2,  -9,  -7,   3,   5,   2,   2,   8,   7,  -7, -10,  -9,  1,   9,   8,   0,  -1,  -1,  -8,   4,  10,   8,  -1],
		   [  8,   2,  -1,  -4,   5,   9, -10,  -3,   7,   0,  -7,  -4,  -8,  -8, -1,   5,   9,  -8,   2,  -7,   9,   2,  -3,   5,   7],
		   [ -2,   3,   9,   4,   4,   2,  -7,  -4,   4,   8,   4,  -4,  -9,  -1, -2,  -5,   0,  -8,   7,   9,  -8,  -9,  -8,  -6,   0],
		   [ -7,  -9,   0,  -9,  -2,  -2,   8,  -4,   3, -10,  -3,  -4,   0,   5, -8,   3,   9,   7,  -1, -10,   7,  -6,  -7,  -6,  -6],
		   [ -7,   3,  -8,  -3,   4,   4,  -8,   7,  -4,   1,   5,  -3,   5, -10,  2,   6,   2,  -8,  -2,  -1,  -8,  -5,   6,   9, -10],
		   [  2,  -6,  -4,  -4,   2,  -5,  -1, -10,   2,   0,  -4,  -9,  -6,  -7,  2,  -6,   4,   5,  -2, -10,  10,  -5,   7,  -7,   2],
		   [ -4,   8,   9,   0,   3,   2,   6,  -8,  -2,   2,  -9,   4,   6,  -9, -2,   4,  -2,   6,   2,   3,   9,  -6,   0,  -7,   2],
		   [ -8,  -9,   5,   2,  -4,   5,  10,   0,  -6,  -2,  -6,   9,  -7,   7, -4,  -4,  -8,   1,  -8,  -7,   3,  -6,  -8,   8,  -3],
		   [ 10,   9,  -3,  -3,   6,   0,   1,   6,  -9,   6,   6,   8,   8,  -4,  9,   1,  -6,  -6,   5,   9,  -9,   0, -10,  -9, -10],
		   [ -5,   7,   8,  -5,  -2,  -7,   4,   4,   4,  -3,  10,   3,  -9,   8, -2,  -1,   7,   1,   9,  -5,  -7,   6,  -8,  10,  -1],
		   [ -7,  -6,   0,  -6,   0,   9,   2,  -5, -10,   4,   1,  -6,  10,   1,  2,   4,   8,   6,  -6,   9,  -9,   7,  -1,   6,   0],
		   [ -7,  -5,   2,  -1,   1,  -2,  -7,  -7,   8,  -7,   8,  -7,  -9,   2,  6,  10,  -9,  -1,   4,  -7,   7,  -6,  -6,   1,   7],
		   [ -4,   8, -10,  -9,  -3,  -5,  -2,   4,   0,   8,   7,   6,   9,   5,  6,  -2,  -6,   7,   6,   2,   8,  -4,  -6,  -9,   9],
		   [  0, -10,   1,   5,   6,   0,  10,  -6,  -4, -10,  -6,  -8,   4,   3, -7,  -7,   4,  -3,   7,  10,   0,  -6,   0,  -7,  -5],
		   [ -1,  -3,  -3,  10,  -4,  10,   0,  -5,  -7,  10,   3,   6,  -1,   7, -1,  -3,   5,   7,   5,  -4,   6,  -3,   4,  -6,  10],
		   [ -6,   0,   3,  -4,  -3,   1,  10,   2,  -2,  -1,   5,   2,   9,  -9, -4,  -6,   9,  -7,   7, -10,  -6,  10,  -8, -10,   7],
		   [ -8,  -8, -10,  -3,  -5,   9,   5,  -1,  -9,  -1,   9,  -5,   4,   1,  5,  -8,  -1,   8,  -7,   0,  10,   7,  10,  -3,   0],
		   [ -8,   6,   2,   1,   7,   7,  -2,   3,  -2,  -5,  -7,   1,   0,   1,  2,   1,  -9,  -4,   7,  -8,  -8,  -6,   6,   8,   2],
		   [  1,   9,  10,  -4,  -8,   1,   1,   8,  10,  -7,   4,  -4,  -5,   3,  0,   1,  -8,   6,  -4,  -3,  -1,   0,   4,  -2, -10],
		   [  2,   8,  -4, -10,  -8,  -6,   9,   9,  -4,  -2,  -3,   1,   0,   4, -3, -10,  10, -10,   4,  -7,   7,   5,  -4,  -8,   2],
		   [ -9,   9,  -7,   3,  -4,   4,   2,   7,  10, -10,   0,   5,  -4,  -4, -4,   4,  -1,   2,   3,  10,  -2,   7,  -7,   0,   5],
		   [  4,  -9,   4,  -9,   1,  -7,   2,   6,  10,  -1,   5,  -1,   9,   3,  2,  -6,  -5,   3,   5,  -5,   8,   5,  -3,   8,   9],
		   [ -1,  -3,   4,  -1,   3,  -4, -10,  -3,  -7,   5,   2,  -9,   3,   9, -3,  -8,   8,   8,   6,   4,   3,   6,  -1,   3,  -2],
		   [  2,  -7,  -4,  10,   0,  -5,  -2,   3,   9,  -4,  -4,   4,   8,   8, -4,  -2,  10,   4,  -3,  -3,   6,   8,  -1,   0,   3],
		   [  1,  -6,   5,   2,   1,   6,   3,   3,   6,  -8,   6,   3,   3,  -8, -8,   5,  -8,   7,   2,  -8,   6,   5,   3,   8,  -2],
		   [  3,  -7,   7,   4,  -3,  -7,  -7,  -9,  -3,  -4,  10,   6,   5, -10,  9,   9,   9,  -3,   7,   5,   4,   1,  -3,   3,  -8],
		   [ -3,   7,   6,  -9,  10,   0,  -3,  -2,  10,  -9,   9,  -2,   7,  -5, -9,  -7,   4,  -1,   0,   0,  -8,   4,   0,   6,   4],
		   [ -1,  -5,  -7,  -1,   9,  -6,   9,  -7,   9,  -1,  -9,  -6,  -5,   6, -6,   2,  -9,   2,  -2,  10,   8,   4,  10,  -9,  -6],
		   [  1,   9,  -1,   1,  -9,   6, -10,   2,   2,   0,  -3,  -3,   8,  -5,  2,   6,  -2,   6,  -2,  -6,   5,  10,   6,  -4,   5],
		   [ -7,   4,  -6,   6, -10,  -4,  -4,   5,  -8,   1,  -6,  10,   5,  -8, -9,   6,  -3,   1,   3, -10,   2,  -3,  -6,  -5,   5],
		   [ 10,   8,   0,  -1,   2,  -7,  -2,  -5,  -5,  10,   7,  10,  -9,  -2,  1,   1, -10,   1,   3,  -7,  -8,  -7,  -1, -10,  -7],
		   [  6,   1,   7,   2,  -3,  -4,  -1,   1,  -2, -10,   8,  -6,   0,  -2, -6,   5,   7,  -7,   9,   7,  -7,  -9,  -9,  -8,  -5],
		   [  3,  -2,   1,  -1, -10,   3,  10,  -5,   5,   4,   4,   4,  -4,  -1, -2,  -9,  -8,  -7,  -4,   6,   8,  -7,   0,   3,   5],
		   [ 10,   3,  -6,  -5,  -9,  -8,   1,   8, -10,   7,   5,   5,  -2,  -7,  3,  -9,   7,  -5,  -3,   1,   8,  -7,   4,  -4,   3],
		   [  1,  -3,  -1,   4,  -3,   9,  10,   5,   7,  -1,  -2,  -6, -10,   6, -6,   5,   3,  -4,   3,  -1,  -2,  -2,   1,  -5,   1],
		   [  8,   6,   0,   2,   8,   6,  -5,   7,  -7,   3,   7,   4,  -8,   8,  6,   0,  -3, -10,   9,   7,  -9,  10,  -5,  -6, -10],
		   [ 10,   6,  -6,  -6,   7,   8,  -8,  -3,  10,   8,  -3,   6,  -7,  -9,  4,  -7,   4,   7,   3,  -1,  10,  -1,  -2,   0,   3],
		   [ -8,   1,  -6,  -1,   7,   0,   8,   3,   4,  -8,  10,  -7,  -2,  -6,  3, -10,   7,  -6,  -7,  -7,  -1,  -2,   0,  -4,   2],
		   [  9,   2,   9,   7,  -9, -10,  -3,   4,   3,   9,   2,  -9,  -1,  -3,  6,   6,  -8,  -8,  -7,  -3,  -8,   1,  -1,   9,   4],
		   [ -4,  -6,  10,  -4,   2,   4,   0,   5,   8,  -9,  -3, -10,  -6,  10, 10,  -5,   4,  -7,   9,   0,  -9,   6,   3,  -7,  -3],
		   [ -7,  -2,  -6,   2,  -8, -10,  -9,  -6,  -9,   5,  -4,   0,   9,   8, -6,  10,   8,   8,   3,   3,   9,  -3,   0,   5,  -2],
		   [  9,   6,   8,   0,   2,  -2,   9,   5,   3,   8,  -8,   1,   8,   2,  1,   4,   3,   3,  10,   8,   9,   3,  10,   6,  -8],
		   [ -9,  10,   9,  -1,   5,  -4,  -7,   3,  -4, -10, -10,  -7,   6,  -5, -1,  -1,  -8,   6,  -4,  -5,   3,  -1,   2, -10,   4],
		   [ -5,  10,   3,  -8,  10,  -9,   8,   3,  -6,   7,  -5,  -5,   6,   0, -7,   3,   7,  -7,   9,  -3, -10,   4,  -8,  -7,  -6],
		   [ -6,  -3,  -7,  -7,   5,  -8,  10,  10,   2,  -9,  -1,   5,   9,   0, -2,   6,   9,   7,  -1,   1,   3,  -8,  -2,   6,   0],
		   [ -5,   3, -10, -10,  -1,   4,   2,   4,   5,  -9,   5,  -3,  -8,   1, -8,   3,   8,  -3,  -8,  -2,   5,   1,  -2,   6,  -1],
		   [ -6,   0,  -8,   4,  -8,  -6,  -8,   6,  -5,  10,   7,   5,  10,   9,  1,  -5,  -3,   6,   2, -10,  -2,   9,  -8,   1,  -6],
		   [ -9,  -6,  -1,   9,   3,  -8,  -7,   6,   2,   1,   1,  -3,  -8,  -5, -9,   9,   1,  -8,   1,  -2,   7,   7,  -7,   7,  -8],
		   [ -2,   4,  -3,   2,   7,  -2,  -3,   4,  -5,  -2,   6, -10,  -3,   6, -8,  -2,  10,   9,  -4,   3,  -3,  -3,  -2,  10,   9],
		   [  2,   3,  -1,   5,   3,  -1,   3,   8,   8,   3,  -2,  -8,   4,  10, -3, -10,   7,   5,   0,   2,  -9,  -3,   8,  -7,   2],
		   [  4,   0,   6,  -5,   3,   1,   9,  10,   2,  -4,   6,  -5,  -2,  -8,  5,   9,  -4, -10,   8,   0,   6,  -2,  -4,   4,  -1],
		   [-10,  -6,  -9,  -5,   3,  -9,   7,  -4,   8,   2,  -7,  -7,  -4, -10,  6,   8,   2,   3,  -9,   0,  -8,  10,  -4,  -1,   4],
		   [ -6,  -8,  -3,  -4,  -2,  -2,   6,   1,   6,   6,  -3,   6,  -5,   2, -4,   3,   9,  -9,  -7,   2,  -9,  -1,  -6,  -3,  -1],
		   [-10,   2,   0, -10,  -8,   4,   5,   9,  -2, -10,   8,   5, -10,  -3, -9,  -3,  -7,   2,  -9,  -7,   5,  -2,   5,  -8,  -8],
		   [ -2,   7,   3,   0,  -3,   1,   1,  -9,   0,   5,   2,   9,   2,   8,  5,   6,  -9,  10,   5,  -5,   6,  -9,   1,   6,   5],
		   [  6,  -5,  -1,  -7,  -3,  -4,   2,   1,  10,  -4,   0,  -5,   6,   9, -8,   6,  -9,   5,  -5,   9,   6,   6,  -4,   7,  -2],
		   [ -2, -10,  -4,   5,   1,   3,   1,  -8,  -9,  -6,  -4,   7,  10,  -9,  0,   3, -10,   4,   5,  -8,  10,  -1,   1,   7,  -7],
		   [ 10,   9, -10,   7,   1,   4,  10,   4,   4,  -9,  -2,   0,  -2,  -8, -6,   5,  -7,  -2, -10, -10,  -7,  -3,  -8,   5,   0],
		   [  7,   8,  -9,  -5,   5,  -9,  -8,   5,   3,  10,  10,  -2,  -7,   3,  6,   3,   0,   3,   3,   3,   5,  -1,  -1,  -1,   3],
		   [ -2,  -2,  -1,  -2,  10,   5,   1,   0,   9,   0,  -8,   7,   4,   5,  4,   4, -10,   1,   1,  -8,   1,  -1,   5,  10,  -8],
		   [  5,  -6,  10,  -7,   2,  -6,   7,  -8,   2,  -6,  -5,  -9,  -2,   1, -9,  -9,   1,  -8,  -7,   7,   1,   8,   2,   6,   4],
		   [  0,  -7,   2,   1,   6,   6,  -2,   9,  -8,  -6,   9,   5,  -9,  -9,  3,   1,   1,   5,  -6,  -7,  -1,   9,   1,   1,  -4],
		   [ 10,   8,  -2,   0,  -5,  -1,   4,   1,  -1,  -4,   1,   7,   2,   3,  8,  -1,   4, -10,   5,  -6,   3,   6,  -1,   5,  -5],
		   [  3,  -4,  -8,  -8,  -7,   2,  10,  10,  -9,   3,   7,  -5,  -7,  -8, -3,   1,   3,   0,   0,  -6,  -7,  -9,  10,   4,   2],
		   [  8,   6,   4,  -1,   6,  -2,   6,  -1, -10, -10,  -9,   0,  -5,  -5, -8,  -4,   2,   7,   7,  -5,   7,  -8, -10,  -8,  -6],
		   [  3,   2,  -5,  -2,  10,   9,  -1,   1,  -6,  -7,  -5,  -3,  -5,  -2, -8,  -7,  -5,  -7,   6,  -6,  -1,  -3,  10,  10,   3],
		   [ -9,  -9,  10,  10,  -6,   9,  -3,   5,   8,  -4,   2,  -5,   4,   4, -8,  -1,   7,   6,   7,  -8,  -8,  -2,   7,  -9,   8],
		   [ -8,  -9,  -8,  -8,   5,   8,  -7,   3,   6,   2, -10,  -2,  -6,   9, -5,  10,  -2,  -1,  -1,  -7,  -9,   4,   8,   6,  -1],
		   [  3,   5,   0,  -2,  -9,   1,  -4,   7,  -8,   0,  -2,   4,   9,  -2,  4,   2,   9,  -1,   8,  -9,  -3,   3,   4,   7,  -8],
		   [  4,   7,   2,  -7,   8,   4,  -6,  -5,  -7,   7,  -8,   6,   1,   5, -7,  -8,   6,   4,   1,  -8,   7,  -6,   5,   2, -10],
		   [ -8,  -2,  -5,  -7,  -8,  -4,  -8,  -3,   4,  -8,   9,  -1,  -7,  -8, -3,   2,   3,  -1,   5,   4,  -3,  -9,   9,   5,  10],
		   [ -5,  -8,   4,   2,  -6,   9,   5,   6,  10,  -2,   7,   6,   4,   2,  8,  -6,  -1,  -6,  10,  -4,   4,   8,  -4,  -4,  10],
		   [  3,   9,  -4,   5,   8,  -5,   0,   9,  -8,   3,  -9,   9,  -6,   7,  0,  -4,   0,   8,   0,  -2,  -9,   1,   5,   7,   5],
		   [ -2,  -1,   9,  -2,   0,   7,   1,  -4,   4,  -5,   7,   3,   8,  -9,  4,   6,   2,   6,   8,  -1,  -7,   4,  -6,   5,   8],
		   [ -8,   9,   4,   3,   3,  10,   8,  10,  -3,   5,   7,  -5,   9,  -9,  4,   4,  10,  -3,  -3,  -9,   0,  -7,   4,  10,   2],
		   [ -9,   8,   9,   9,   6,   5,  -4, -10,  -8,  -9,   8,  -3,   1,   3,  1, -10,  -1,  -7,   9,   7,  -6,   8,   2,  -8,  -7],
		   [ -6,  -6,   3,  -1,   3,   9,  10,  10,   8,   9,  -6,   7,   5,  -5,  3,  -5,   7,   4,   3,   9,  -6,   9,  -5,  -4,  -3],
		   [-10,  -3,   5,  -6,  -4,  -6,   1,   9,   4,  10,   7,   6,   2,   4, -4,  -4,   5,   6, -10,   4,  -9,   6,  -2,   8,  -2],
		   [ -5,  -8,   0,  10,  -2,  -4,  -4,   5,   4,   3,  -7,  -8,   2,  10, -6,  -4,  -6,   7,   4,  -6,   2,  -2,   6,  -2,   8],
		   [  1,   1,  -5,   9,   3,  -8,  -2,  -2,  -5,  -2,   7,  -2,   3,   5, -4,   8,  -9,   4,   5,   9,   5,   3,  10,   8,   7],
		   [  8, -10,   0,  -9,   3,  -9,  -4,   2,  -1,   7,  -9,  -7,  -3,   2, -9,   8,   0,   3,   7, -10,  -7,   3,   5,   8,  -2],
		   [ -6,  -9,  -8,  -4,   6,   2,  -6,  10,   2,   0,  -3,  10,  -7,   6, -7,   7,   0,  -4,  -5,  -5,   2,   9, -10,  -8,  -8],
		   [  6,   4, -10, -10,  -7,   6,   0,   9,  -7,   3,  -9,  -5,  -5,  -7,  3,  -4,  -9,   7,   4,   3,   8,   6,   8,  -5,   0],
		   [ -5,  -4,   8,   1,  -2,  -4,  -8,  -9,   9,  -5,   7,  -4,   6,  -1, -4,  -6,  -5,  -4,  -1,   0,   6,  -3,   4,  -4,  -8],
		   [  3,   3,   5,   8,   8,   9,   1,  -6,  -1,  -1,  -2,   8,  -8,  10,  3,  -7,   1,   6,  -2,  -4,  -3,  -7, -10,  -2,  -7],
		   [  5,   4,  -4,   3,   2,   6,   4, -10,  10,  -5,   6, -10,   5,   3, -4,  -9,  -5,  -4,   4,   8,  -4,  -3,  -6,   0,  10],
		   [ -3,  -3,  10,  -8,   7,   6,  -5,   4,   6,  -7,   1,   9,  10,  10,  9,  10,   0,   0,  -6,   5,  -4,   2,   7,  -8,   3],
		   [ -2,   9,   7,  -4,   0,  -3,  -3,  -9,   7,   3,   2, -10,   3,   2, 10,   1,  -2,  -7,  -5,  -4,   5,   4,  -6, -10, -10],
		   [ -9,  -3,  10,   3,  -4,   7,  -8,  -1, -10,   1,   5,  -9,   6,   5, -6,  -6,   1,  -5,   4,   3,  -9,   4,  -7,   3,   7],
		   [  5,   4,   5,  -1,  10,   1,   9,   8,   3,  10,   7,  10,  -1,   5,  6,  -3,  -7,  -5,  -1,   7,   1,   7,  -5,   7,   5],
		   [  8,  -2,   2,  -9,   5,  -8,   3,   1,   5,   0,  -2,   1,  -3,  -4,  5,  -9,   9,   7,  -5,  -7,  -6,   2,   2,   2,   9],
		   [ -1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
		   [  0,  -1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
		   [  0,   0,  -1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
		   [  0,   0,   0,  -1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
		   [  0,   0,   0,   0,  -1,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
		   [  0,   0,   0,   0,   0,  -1,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
		   [  0,   0,   0,   0,   0,   0,  -1,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
		   [  0,   0,   0,   0,   0,   0,   0,  -1,   0,   0,   0,   0,   0,   0,  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
		   [  0,   0,   0,   0,   0,   0,   0,   0,  -1,   0,   0,   0,   0,   0,  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
		   [  0,   0,   0,   0,   0,   0,   0,   0,   0,  -1,   0,   0,   0,   0,  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
		   [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  -1,   0,   0,   0,  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
		   [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  -1,   0,   0,  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
		   [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  -1,   0,  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
		   [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  -1,  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
		   [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, -1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
		   [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,  -1,   0,   0,   0,   0,   0,   0,   0,   0,   0],
		   [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0,  -1,   0,   0,   0,   0,   0,   0,   0,   0],
		   [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0,  -1,   0,   0,   0,   0,   0,   0,   0],
		   [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0,   0,  -1,   0,   0,   0,   0,   0,   0],
		   [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0,   0,   0,  -1,   0,   0,   0,   0,   0],
		   [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0,   0,   0,   0,  -1,   0,   0,   0,   0],
		   [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0,   0,   0,   0,   0,  -1,   0,   0,   0],
		   [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0,   0,   0,   0,   0,   0,  -1,   0,   0],
		   [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0,   0,   0,   0,   0,   0,   0,  -1,   0],
		   [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  -1]])
	b = Matrix([5, 6, 4, 5, 9, 2, 7, 2, 7, 7, 0, 9, 5, 0, 6, 1, 8, 4, 2, 1, 3, 1, 3, 10, 2, 8, 8, 4, 0, 9, 8, 2, 0, 6, 7, 1, 2, 1, 5, 6, 4, 2, 6, 4, 6, 4, 2, 1, 10, 7, 9, 3, 10, 2, 3, 3, 4, 3, 3, 8, 4, 5, 4, 1, 7, 6, 7, 6, 5, 4, 8, 4, 6, 6, 7, 1, 2, 3, 2, 1, 2, 2, 8, 7, 5, 8, 1, 6, 0, 1, 10, 6, 2, 7, 8, 3, 5, 9, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
	c = Matrix([8, 6, -5, -2, -10, 0, -9, 10, 2, 3, -6, -3, -9, 2, -5, -9, 4, 1, 7, -2, -6, 10, 0, 4, 4])
	B = range(100, 125)
	simplex(A, b, c, B, verbose=True)
