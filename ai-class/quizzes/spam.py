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
