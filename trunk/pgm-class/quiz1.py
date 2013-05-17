P = {}
P['President = 1'] = 0.01
P['President = 0'] = 1 - P['President = 1'] 
P['Accident = 1'] = 0.1
P['Accident = 0'] = 1 - P['Accident = 1']
P['Traffic = 1 | President = 0, Accident = 0'] = 0.1
P['Traffic = 1 | President = 0, Accident = 1'] = 0.5
P['Traffic = 1 | President = 1, Accident = 0'] = 0.6
P['Traffic = 1 | President = 1, Accident = 1'] = 0.9


P['Traffic = 1 | Accident = 1'] = P['Traffic = 1 | President = 0, Accident = 1']*P['President = 0'] + P['Traffic = 1 | President = 1, Accident = 1'] * P['President = 1']
P['Traffic = 1'] = P['Traffic = 1 | President = 0, Accident = 0']*P['President = 0']*P['Accident = 0'] + P['Traffic = 1 | President = 0, Accident = 1']*P['President = 0']*P['Accident = 1'] + P['Traffic = 1 | President = 1, Accident = 0']*P['President = 1']*P['Accident = 0'] + P['Traffic = 1 | President = 1, Accident = 1']*P['President = 1']*P['Accident = 1']
P['Accident = 1 | Traffic = 1'] = P['Traffic = 1 | Accident = 1']*P['Accident = 1']/P['Traffic = 1']
P['Accident = 1 | Traffic = 1, President = 1'] = (P['Accident = 1 | Traffic = 1'] - P['Accident = 1 | Traffic = 1, President = 0']*P['President = 0'])/P['President = 1']
