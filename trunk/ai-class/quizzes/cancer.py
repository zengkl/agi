


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
P['Cancer | T1=+'] = P['+ | Cancer']*P['Cancer']/P['+']
P['Healthy | T1=+'] = P['+ | Healthy']*P['Healthy']/P['+']

P['T2=+ | T1=+'] = P['+ | Cancer']*P['Cancer | T1=+'] + P['+ | Healthy']*P['Healthy | T1=+']

P['S']  = 0.7
P['R'] = 0.01
P['~R'] = 1 - P['R']
P['~S'] = 1 - P['S']
P['R | S'] = P['R']
P['H | S,R'] = 1
P['H | ~S,R'] = 0.9
P['H | S,~R'] = 0.7
P['H | ~S,~R'] = 0.1
P['H'] = P['S']*P['R']*P['H | S,R'] + P['S']*P['~R']*P['H | S,~R'] + P['~S']*P['R']*P['H | ~S,R'] + P['~S']*P['~R']*P['H | ~S,~R']
P['H | R'] = P['H | S,R']*P['S'] + P['H | ~S,R']*P['~S']
P['R | H'] = P['H | R']*P['R']/P['H']
P['H | S'] = P['H | S,R']*P['R'] + P['H | S,~R']*P['~R']  # 4. Total probability
P['H,S'] = P['H | S']*P['S']   # 3. Joint probability
P['H,S | R'] = P['S']*P['H | S,R'] 
P['R,H,S'] = P['R']*P['S']   # 2. Independence of R and S. Total dependence of H
P['R | H,S'] = P['R,H,S']/P['H,S'] # 1. Joint probability 

P['R | H,S'] = P['H,S | R'] * P['R']/P['H,S'] # 0. Bayes Rule
    * P['H,S | R'] = P['S']*P['H | S,R'] # 1. Conditional independence
       ** P['S']  = 0.7  # Given
       ** P['H | S,R'] = 1 # Given
    * P['H,S'] = P['H | S']*P['S']   # 2. Joint probability
       ** P['H | S'] = P['H | S,R']*P['R'] + P['H | S,~R']*P['~R'] # 2. Total probability
          *** P['H | S,R'] = 1 # Given
          *** P['R'] = 0.01 # Given
          *** P['H | S,~R'] = 0.7  # Given
          *** P['~R'] = 1 - P['R']  # complement of Given
    * P['R'] = 0.01 # 3. Given


#===========================================
P['R | H,S'] = P['R,H,S']/P['H,S'] # 1. Joint probability 
     * P['R,H,S'] = P['R']*P['S']   # 2. Independence of R and S. Total dependence of H
        ** P['R'] = 0.01 # 2a. Given
        ** P['S'] = 0.7  # 2b. Given 
     * P['H,S'] = P['H | S']*P['S']   # 3. Joint probability
        ** P['H | S'] = P['H | S,R']*P['R'] + P['H | S,~R']*P['~R']  # 3a. Total probability
           *** P['H | S,R'] = 1  # 3aa.  Given
           *** P['R'] = 0.01 # 3ab. Given
           *** P['H | S,~R'] = 0.7  # 3ac. Given
           *** P['~R'] = 1 - P['R']  # 3ad.  Complement of Given
        ** P['S'] = 0.7   # 3b. Given


# Joint Probability rule:

P['A | B'] = P['A,B']/P['B']

P['A | B'] != P['A,B']/P['A']

P['A,B'] = P['B,A']

P['A | B'] != P['B | A']


# Total Probability:

P['A'] = P['A | B']*P['B'] + P['A | !B']*P['!B']

P['A | B'] = P['A | B,C']*P['C'] + P['A | B,!C']*P['!C']

#Depends on 
P['B'] _|_ P['C']
