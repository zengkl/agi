# Joint Probability rule:

P['A | B'] = P['A,B']/P['B']

P['A | B'] != P['A,B']/P['A']

P['A,B'] = P['B,A']
P['A,B'] = P['A | B']*P['B']

P['A | B'] != P['B | A']

# Complement
P['!A'] = 1 - P['A']

# Total Probability:

P['A'] = P['A | B']*P['B'] + P['A | !B']*P['!B']

P['B'] = P['B | A']*P['A'] + P['B | !A']*P['!A']

P['A | B'] = P['A | B,C']*P['C'] + P['A | B,!C']*P['!C']

#Depends on 
P['B'] _|_ P['C']
