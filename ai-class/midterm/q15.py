seq = 'AAAAB'
def count( query, seq ):
    match = 0
    nomatch = 0
    for i in range(len(seq ) - len(query) + 1 ):
        if seq[i:len(query)+i] == query:
            match += 1
        else:
            nomatch +=1
    return match, nomatch
P = {}
k = 1.0
match, nomatch = count('AA', seq )
P['A0'] = (1 + k)/(1 + 2*k)
P['At | A(t-1)'] = (match + k)/(match + nomatch + k*2)
match, nomatch = count('BA', seq )
P['At | B(t-1)'] = (match + k)/(match + nomatch + k*2)
