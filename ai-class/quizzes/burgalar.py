P = {}
f = {}
P['+b'] = 0.001
P['+e'] = 0.002
P['+m | +a'] = 0.7
P['+a | +b,+e'] = 0.95
P['+j | +a'] = 0.9

P['a'] = P['+a']
P['e'] = P['+e']
P['a | +b,e'] =  P['+a | +b,+e']
P['+j | a'] = P['+j | +a']
P['+m | a'] = P['+m | +a']

f['+b,+m,+j,+a,+e'] = P['+b']*P['e']*P['a | +b,e']*P['+j | a']*P['+m | a']