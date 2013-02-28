import sys
sys.path.append('~/Courses/ai-class/src/python')
from probability import *

P = ProbDist()
P['A0'] = 0.5
P['B0'] = 1 - P['A0']
P['A1 | A0'] = 0.5
P['B1 | A0'] = 0.5
P['B1 | B0'] = 0.5
P['A1 | B0'] = 0.5
P['X0 | A0'] = 0.1
P['Y0 | A0'] = 1 - P['X0 | A0']
P['X0 | B0'] = 0.8
P['Y0 | B0'] = 1 - P['X0 | B0']
P['X0'] = P['X0 | A0']*P['A0'] + P['X0 | B0']*P['B0']
P['A0 | X0'] = P['X0 | A0']*P['A0']/P['X0']
P['B0 | X0'] = P['X0 | B0']*P['B0']/P['X0']

P['A0,X0']  = P['A0 | X0']*P['X0']
P['A1 | A0,X0'] = P['A0,A1,X0']/P['A0,X0']
P['A1 | X0'] = P['A1 | A0']*P['A0 | X0'] + P['A1 | B0']*P['B0 | X0']
P['A1 | X0,X1'] = P['A1 | A0']*P['A0 | X0'] + P['A1 | B0']*P['B0 | X0']

#P['A1 | A0,X0']*P['A0'] + P['A1 | B0,X0']*P['B0']
