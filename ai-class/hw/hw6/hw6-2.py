import sympy
P = {}

P['A_oo'] = sympy.Symbol('A_oo')
P['B_oo'] = 1 - P['A_oo']
# As t -> oo, At -> A(t-1)
P['A(t-1)'] = P['A_oo']
P['B(t-1)'] = 1 - P['A(t-1)']
P['At | A(t-1)'] = 0.9
P['Bt | A(t-1)'] = 1 - P['At | A(t-1)']
P['At | B(t-1)'] = 0.5
P['Bt | B(t-1)'] = 1 - P['At | B(t-1)']

sympy.solve(P['A_oo'] - (P['At | A(t-1)']*P['A_oo'] + P['At | B(t-1)']*(1 - P['A_oo']) ), P['A_oo'])
