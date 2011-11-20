def total( bag ):
    count = 0.0
    for m in bag:
        count += bag[m]
    return count


B = {}
P = {}

Mspam = [['Offer','Is', 'Secret'],
         ['Click','Secret', 'Link'],
         ['Secret', 'Sports', 'Link']]

Mham = [['Play','Sports', 'Today'],
        ['Went', 'Play', 'Sports'],
        ['Secret', 'Sports', 'Event'],
        ['Sports', 'Is', 'Today'],
        ['Sports', 'Costs', 'Money']]
Ham = {'Play': 2, 'Sports': 5, 'Today': 2, 'Went': 1, 'Secret': 1, 'Event': 1,
                'Costs': 1, 'Money': 1, 'Is': 1}
Spam = {'Offer': 1, 'Is': 1, 'Secret': 3, 'Link': 2, 'Sports': 1, 'Today' : 0, 'Click': 1}
M = {'Sports': 6, 'Offer': 1, 'Is': 2, 'Secret': 4, 'Click': 1, 'Link': 2, 'Play': 2,
     'Today': 2, 'Went': 1, 'Event': 1, 'Costs': 1, 'Money': 1}




#P['M'] = P['M | Spam']*P['Spam'] + P['M | Ham']*P['Ham']
#P['Spam | M'] = P['M | Spam']*P['Spam']/P['M']

k = 0
P['Sports | Spam'] = Spam['Sports']/total( Spam )

P['Sports'] = M['Sports']/total(M)
P['Spam'] = (total(Spam) + k)/(total(M) + k*len(M))


P['Ham'] = (total(Ham) + k)/(total(M) + k*len(M))
P['Secret'] = M['Secret']/total( M )
P['Is'] = M['Is']/total( M )

P['Secret | Ham'] = Ham['Secret']/total(Ham)
P['Is | Ham'] = Ham['Is']/total(Ham)
P['Secret is Secret | Ham'] = P['Secret | Ham'] * P['Secret | Ham'] * P['Is | Ham']
P['Secret is Secret'] = P['Secret']*P['Secret']*P['Is']

P['Is | Spam'] = Spam['Is']/total(Spam)
P['Secret | Spam'] = Spam['Secret']/total(Spam)
P['Secret is Secret | Spam'] = P['Secret | Spam']*P['Secret | Spam']*P['Is | Spam']

P['Spam | Sports'] = P['Sports | Spam']*P['Spam']/P['Sports']

P['Spam | Secret is Secret'] = P['Secret is Secret | Spam']*P['Spam']/(P['Secret is Secret | Spam']*P['Spam'] + P['Secret is Secret | Ham']*P['Ham'])


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



MovieTitles = ['A Perfect World',
               "My Perfect Woman",
               'Pretty Woman']

SongTitles = ['A Perfect Day',
              'Electric Storm',
              'Another Rainy Day']

Titles = []
Titles.extend( MovieTitles )
Titles.extend( SongTitles )
M = makeBag( Titles )
Movie = makeBag( MovieTitles, M )
Song = makeBag( SongTitles,  M )

Query = 'Perfect Storm'

k = 1


def Laplace_Smoothing(Movie, Song, MovieTitles, SongTitles, M, k = 1.0):
    P = {}
    P['Movie'] = float(len(MovieTitles) + k) /float(len(MovieTitles) + len(SongTitles) + k*2)
    P['Song'] = float(len(SongTitles) + k)/float(len(MovieTitles) + len(SongTitles) + k*2)
    P['Perfect | Movie'] = float(Movie['Perfect'] + k)/float(total(Movie) + k*len(M))
    P['Perfect | Song'] = float(Song['Perfect'] + k)/float(total(Song) + k*len(M))
    P['Storm | Movie'] = float(Movie['Storm'] + k)/float(total(Movie) + k*len(M))
    P['Storm | Song'] = float(Song['Storm'] + k)/float(total(Song) + k*len(M))
    P['Perfect Storm | Movie'] = P['Perfect | Movie'] * P['Storm | Movie']
    P['Perfect Storm | Song'] = P['Perfect | Song'] * P['Storm | Song']
    P['Movie | Perfect Storm'] = P['Perfect Storm | Movie']*P['Movie']/(P['Perfect Storm | Movie']*P['Movie'] + P['Perfect Storm | Song']*P['Song'])
    P['Song | Perfect Storm'] = P['Perfect Storm | Song']*P['Song']/(P['Perfect Storm | Movie']*P['Movie'] + P['Perfect Storm | Song']*P['Song'])
    return P
