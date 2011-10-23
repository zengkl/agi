


Pseudo = {}
P = {}
P['Cancer'] = 0.01
P['Healthy'] = 1 - P['Cancer']
P['+ | Cancer'] = 0.9
P['- | Cancer'] = 1 - P['+ | Cancer']
P['+ | Healthy'] = 0.2
P['- | Healthy'] = 1 - P['+ | Healthy']
P['++ | Cancer'] = P['+ | Cancer'] * P['+ | Cancer']
P['+- | Cancer'] = P['+ | Cancer'] * P['- | Cancer']
P['+- | Healthy'] = P['+ | Healthy'] * P['- | Healthy']
Pseudo['Cancer | +-'] = P['+- | Cancer']*P['Cancer']
Pseudo['Healthy | +-'] = P['+- | Healthy'] * P['Healthy']
#eta2 = 1/(Pseudo['+- | Healthy'] + Pseudo['+- | Cancer'])
eta = 1/(Pseudo['Healthy | +-'] + Pseudo['Cancer | +-'])
P['Cancer | +-'] = eta*Pseudo['Cancer | +-']
P['+'] = P['+ | Cancer']*P['Cancer'] + P['+ | Healthy']*P['Healthy']
P['Cancer | +'] = P['+ | Cancer']*P['Cancer']/P['+']
P['Healthy | +'] = P['+ | Healthy']*P['Healthy']/P['+']

P['T2=+ | T1=+'] = P['+ | Cancer']*P['Cancer | +'] + P['+ | Healthy']*P['Healthy | +']




