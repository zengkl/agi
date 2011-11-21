from mdp import *

class DeterministicGridMDP(GridMDP):
    def __init__( self, grid, terminals, init=(0,0), gamma = 1 ):
        GridMDP.__init__( self, grid, terminals, init, gamma )
    def T( self, state, action ):
        if action == None:
            return [(0.0, state)]
        else:
            return [(1.0, self.go(state, action))]

Fig[9,16] = DeterministicGridMDP([[-3, -3, -3, 100],
                         [-3, None, -3, -100],
                         [-3, -3, -3, -3]], 
                        terminals = [(3, 2), (3, 1)], gamma = 1)

q14 = DeterministicGridMDP([[-5, -5, None, 100],
                        [-5, -5, -5, -5]],
                       terminals = [(3, 1)], gamma = 1)


def value_iterate_1(mdp, epsilon=0.001, U0=dict([(s, 0) for s in mdp.states]) ):
    "Solving an MDP by value iteration. [Fig. 17.4]"
    R, T, gamma = mdp.R, mdp.T, mdp.gamma
    U = U0.copy()
    delta = 0
    for s in mdp.states:
        U[s] = R(s) + gamma * max([sum([p * U0[s1] for (p, s1) in T(s, a)])
                                    for a in mdp.actions(s)])
        delta = max(delta, abs(U0[s] - U[s]))
    return U, delta

U,delta = value_iterate_1( Fig[9,16] )
