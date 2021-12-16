import re

p = re.compile('(pattern)')

m = p.search('ones always like displaying beautiful pattern')

if(m!=None):
    found =m.group()
    print(found)
    print(m.span())
    print(type(m.span()))
else:
    print("no match")