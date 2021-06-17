d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'],
'Marks': [57,87,67,79]}
max=d['Marks'][0]
if max<d['Marks'][1]:
    max=d['Marks'][1]
if max<d['Marks'][2]:
    max=d['Marks'][2]   
if max<d['Marks'][3]:
    max=d['Marks'][3] 
print(max)
a=max.denominator
print(d['Student'][a])


