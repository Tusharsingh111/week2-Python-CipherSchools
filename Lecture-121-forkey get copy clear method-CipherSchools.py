#fronkeys
d={'name' : 'unknown', 'age' : 'unknown'}

d = dict.fromkeys(['name', 'age','height'],'unknown')
print(d)

# get metod
d={'name' : 'unknown', 'age' : 'unknown'}
#print(d['names'])
print(d.get('name'))

if d.get('names'):
    print('present')
else:
    print('not present')

d.clear()
print(d)