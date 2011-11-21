from search import *
q2graph = UndirectedGraph(Dict(
        A=Dict(B=10,C=10,D=10,E=10,F=10),
        B=Dict(G=10),
        C=Dict(H=10,I=10),
        E=Dict(J=10,K=10),
        F=Dict(L=10),
        K=Dict(L=10)))
q2graph.locations = Dict(A=(15,0),B=(11,0),C=(8,0),D=(7,0),E=(6,0),F=(10,0), G=(2,0), H=(3,0),I=(9,0),J=(5,0),K=(20,0),L=(0,0))
q2 = GraphProblem( 'A', 'L', q2graph )

f = memoize(lambda n: max(getattr(n, 'f', -infinity), n.path_cost + q2.h(n)), 'f')
frontier = PriorityQueue(min, f )
explored = {}


