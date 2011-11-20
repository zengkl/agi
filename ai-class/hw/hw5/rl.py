def distance(x, y):
    return abs( y - x )

def invertstate( states ):
    inv = {}
    for s in states:
        if states[s] in inv:
            inv[states[s]].append( s )
        else:
            inv[states[s]] = [s]
    return inv
state0 = invertstate({1: 'A',
          2: 'B',
          3: 'G',
          4: '',
          5: ''})

state1 = invertstate( {1: '',
          2: 'B',
          3: 'A',
          4: 'B',
          5: 'G'})

state2 = invertstate( {1: 'B',
          2: 'B',
          3: 'A',
          4: '',
          5: 'G'})
 
state3 = invertstate( {1: 'A',
          2: '',
          3: 'G',
          4: 'B',
          5: ''})
 
def f1(locationOf):
    """ distance from agent A to goal G """
    agentA = locationOf['A'][0]
    goal = locationOf['G'][0]
    return distance( agentA, goal )

def f2( locationsOf ):
    """ distance from agent A to closest bad guy B """
    agentA = locationsOf['A'][0]
    return min( [ distance( agentA, badguy ) for badguy in locationsOf['B'] ] )

def f3( locationsOf ):
    """ distance of closest bad guy to goal """
    goal = locationsOf['G'][0]
    return min( [ distance( goal, badguy ) for badguy in locationsOf['B'] ] )
 




def f4( locationsOf ):
    """ distance of (closest bad guy to A) to goal """
    closestDistance = 100
    for badguy in locationsOf['B']:
        dist = distance( locationsOf['A'][0], locationsOf['B'][badguy] )
        if dist < closestDistance:
            closestDistance = dist
            closestBadguy = badguy
    return distance( locationsOf['G'][0], locationsOf['B'][closestBadguy] )
 


def F( state ):
    return [ f1( state ), f2( state ) ]

def G( state ):
    return [ f1( state ), f2( state ), f3( state ) ]
