from collections import defaultdict

items = [('a',1),('b',2),('a',3),('b',4),('a',5),('c',6)]

d = defaultdict(list)

for key, value in items:
    d[key].append(value)
    
print(dict(d))


# count letters in string
count = defaultdict(int)
s = "yo mummy"

for i in s:
    count[i]+=1
    
print(dict(count))