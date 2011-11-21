def total( bag ):
    count = 0.0
    for m in bag:
        count += bag[m]
    return count


def makeBag( titles, dictionary=None ):
    bag = {}
    if dictionary:
        for word in dictionary:
            bag[word] = 0
    for title in titles:
        words = title.split(' ')
        for word in words:
            if word in bag:
                bag[word] +=1
            else:
                bag[word] = 1
    return bag

OldTitles = ['Top Gun',
             'Shy People',
             'Top Hat']

NewTitles = ['Top Gear',
             'Gun Shy']

Titles = []
Titles.extend( OldTitles )
Titles.extend( NewTitles )
M = makeBag( Titles )
Old = makeBag( OldTitles, M )
New = makeBag( NewTitles,  M )

k = 1
P = {}
P['Old'] = float(len(OldTitles) + k) /float(len(OldTitles) + len(NewTitles) + k*2)
P['New'] = float(len(NewTitles) + k)/float(len(OldTitles) + len(NewTitles) + k*2)
P['Top | Old'] = float(Old['Top'] + k)/float(total(Old) + k*len(M))


P['Top | New'] = float(New['Top'] + k)/float(total(New) + k*len(M))
P['Top | Old'] = P['Perfect | Old'] * P['Top | Old']
P['Top | New'] = P['Perfect | New'] * P['Top | New']
P['Old | Top'] = P['Top | Old']*P['Old']/(P['Top | Old']*P['Old'] + P['Top | New']*P['New'])
P['New | Top'] = P['Top | New']*P['New']/(P['Top | Old']*P['Old'] + P['Top | New']*P['New'])


