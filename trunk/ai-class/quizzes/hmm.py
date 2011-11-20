import sympy
P ={}
P['Rt'] = sympy.Symbol('Rt')
P['Rt | R(t-1)'] = 0.6
P['Rt | S(t-1)'] = 0.2
P['R(t-1)'] = P['Rt']
P['S(t-1)'] = 1-P['R(t-1)']
P['Rt | R(t-1)']*P['R(t-1)'] + P['Rt | S(t-1)']*P['S(t-1)']
0.4*Rt + 0.2
P['Rt | R(t-1)']*P['R(t-1)'] + P['Rt | S(t-1)']*P['S(t-1)'] -P['Rt']
-0.6*Rt + 0.2
>>> 0.2/0.6
0.2/0.6
0.33333333333333337
sympy.solve(P['Rt | R(t-1)']*P['R(t-1)'] + P['Rt | S(t-1)']*P['S(t-1)'] -P['Rt'], P['Rt'])
[0.333333333333333]

k = 1.0
>>> P['R0'] = (1+k)/(1+ k*2)
P['R0'] = 0
>>> P['S|S'] = (3+k)/(3+k*2)
P['S|S'] = 0.75
>>> P['R|S'] = 1 - P['S|S']
P['R|S'] = 1 - P['S|S']
>>> P['S|R'] = (1+k)/(1+2*k)
P['S|R'] = 0.5
>>> P['R|R'] = (0+k)/(1 + 2*k)
P['R|R'] = 0.5
>>> 


def Laplace_Smoothing(Spam, Ham, mSpam, mHam, M, k = 1.0):
    P = {}
    P['Spam'] = float(len(mSpam) + k) /float(len(mSpam) + len(mHam) + k*2)
    P['Ham'] = float(len(mHam) + k)/float(len(mSpam) + len(mHam) + k*2)
    P['Today | Spam'] = float(Spam['Today'] + k)/float(total(Spam) + k*len(M))
    P['Today | Ham'] = float(Ham['Today'] + k)/float(total(Ham) + k*len(M))
    P['Is | Spam'] = float(Spam['Is'] + k)/float(total(Spam) + k*len(M))
    P['Is | Ham'] = float(Ham['Is'] + k)/float(total(Ham) + k*len(M))
    P['Secret | Spam'] = float(Spam['Secret'] + k)/float(total(Spam) + k*len(M))
    P['Secret | Ham'] = float(Ham['Secret'] + k)/float(total(Ham) + k*len(M))
    P['Today Is Secret | Spam'] = P['Today | Spam'] * P['Is | Spam']*P['Secret | Spam']
    P['Today Is Secret | Ham'] = P['Today | Ham'] * P['Is | Ham']*P['Secret | Ham']
    P['Spam | Today Is Secret'] = P['Today Is Secret | Spam']*P['Spam']/(P['Today Is Secret | Spam']*P['Spam'] + P['Today Is Secret | Ham']*P['Ham'])
    return P


P['R0'] = 1
P['S0'] = 1 - P['R0']
P['R1 | R0'] = 0.6
P['S1 | R0'] = 1 - P['R1 | R0']
P['R1 | S0'] = 0.2
P['S1 | S0'] = 1 - P['R1 | S0']
P['H1 | R1'] = 0.4
P['H1 | S1'] = 0.9
P['G1 | R1'] = 1 - P['H1 | R1'] 
P['G1 | S1'] = 1 - P['H1 | S1'] 
P['R1'] = P['R1 | R0']*P['R0'] + P['R1 | S0']*P['S0']
P['S1'] = 1 - P['R1']
P['H1'] = P['H1 | R1']*P['R1'] + P['H1 | S1']*P['S1']

P['R1 | H1'] = P['H1 | R1']*P['R1']/P['H1']
P['R1 | H1']












