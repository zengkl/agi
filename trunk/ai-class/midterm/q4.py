P = {'H,H':0.04}
P['H'] = math.sqrt(P['H,H'])
P['T'] = 1 - P['H']
P['T,T'] = P['T']*P['T']
