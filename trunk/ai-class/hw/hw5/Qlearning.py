
def updateQ( s0, a0, s1, a1, gamma, alpha, Q, R ):
    return Q[(s0,a0)] + alpha * ( R[s0] + gamma*Q[(s1,a1)] - Q[(s0,a0)] )

def initializeQR( states, actions, terminal_reward, nonterminal_reward, terminal_state ):    
    Q0 = {}
    R = {}    
    for s in states:
        if s == terminal_state:
            R[s] = terminal_reward
        else:
            R[s] = nonterminal_reward
        for a in actions:
            Q0[(s,a)] = R[s]

    return Q0, R





actions = ['NORTH', 'SOUTH','EAST','WEST']
states = [(i+1,j+1) for i in range(3) for j in range(4) if not ((i+1 == 2) and (j+1 == 2))]
terminal_state  = (3,4)
terminal_reward = 100
nonterminal_reward = 0
alpha = 0.5
gamma = 0.9

(Q, R) = initializeQR( states, actions, terminal_reward, nonterminal_reward, terminal_state )

s0 = (3,3)
a0 = 'NORTH'
s1 = (3,4)
a1 = 'NORTH'
Q[(s0,a0)] = updateQ( s0, a0, s1, a1, gamma, alpha, Q, R )

