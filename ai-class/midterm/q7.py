P= {'A'     : 0.5, 
    'B | A' : 0.2,
    'B | !A': 0.2,
    'C | A' : 0.8,
    'C | !A': 0.4}

P['!A']       = 0.5
P['!A,C']     = P['C | !A']*P['!A']
P['A,C']      = P['C | A']*P['A']
P['B']        = P['B | A']*P['A'] + P['B | !A']*P['!A']
#P['B | !A,C'] = P['!A,C | B']*P['A,C']/P['B']
#P['B | A,C']  = P['A,C | B']*P['B']/P['A,C']
P['!A,B,C']   = P['B | !A,C']*P['!A,C']
P['A,B,C']    = P['B | A,C']*P['A,C']
P['B | C']    = P['B'] #P['B | A,C']*P['A,C'] + P['B | !A,C']*P['!A,C']
P['C | B']    = 

P['C']        = P['C | A']*P['A'] + P['C | !A']*P['!A']
    
P['C | B']  = P['B | C']*P['C']/P['B']
