P = {}
# Exercise 1
P['A'] = 0.5
P['B | A'] = 0.2
P['B | !A'] = 0.8

P['!A'] = 1 - P['A']
P['B'] = P['B | A']*P['A'] + P['B | !A']*P['!A']
P['A | B'] = P['B | A']*P['A']/P['B']

# Conditional joint probabilities
P['A | B,C'] = P['B | A,C']*P['A | C']/P['B | C']

# Exercise 2.
# ------- Given -------
P['A'] = 0.5
P['X | A'] = 0.2
P['X | !A'] = 0.6

# ------- Proof -------
P['!A'] = 1 - P['A']    # Complement 
P['!X | !A'] = 1 -P['X | !A']  # Complement of conditional 
P['!X | A'] = 1 - P['X | A']   # Complement of conditional

P['X'] = P['X | A']*P['A'] + P['X | !A']*P['!A']  # Total probability
P['!X'] = 1 - P['X']     # Complement
P['X1,X2,!X3'] = P['X | A']*P['X | A']*P['!X | A']*P['A'] + P['X | !A']*P['X | !A']*P['!X | !A']*P['!A']   # Joint probability of Independent variables
P['X1,X2,!X3 | A'] = P['X | A']*P['X | A']*P['!X | A']  # Joint probability of independent variables
P['A | X1, X2,!X3'] = P['X1,X2,!X3 | A']*P['A']/P['X1,X2,!X3']  # Bayes rule


# ------ Dead end ---------
P['!X | !A'] = 1 -P['X | !A']  #
P['!X | A'] = 1 - P['X | A']
P['!X'] = P['!X | A']*P['A'] + P['!X | !A']*P['!A']
