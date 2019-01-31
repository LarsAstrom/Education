#listor
a = []
b = list()
a = [2,3,5,7,11]
'''
for i in range(5):
  print(a[i])

for x in a:
  print(x)

for i in range(len(a)):
  print(a[i])


a.append(13)
a.append(17)

print(a)

a.remove(2)

print(a)


b = []
for i in range(10000):
  b.append(i)

import random,time

random.shuffle(b)
time1 = time.time()

for i in range(10000):
  b.remove(i)
time2 = time.time()
print(time2-time1)
'''
'''
l = []
l.append(4)
l.append(27)
l.append(65536)
l.append(37)
l.append(-1)
l.append(22)
print(l)
l.sort()
print(l)

t1 = (1,2)
print(t1)
print(t1[0])
print(t1[1])
'''

l = []
l.append((60,160))
l.append((75,170))
l.append((60,150))
l.append((50,140))
l.append((87,200))
print(l)
l.sort()
print(l)
l.reverse()
print(l)
l2 = []
for i in range(len(l)):
  temp = l[i]
  l2.append((temp[1],temp[0]))
print(l2)
l2.sort()
print(l2)


#Set
'''
s = set()
s.add(5)
s.add(7)
s.add(14)
print(s)

b = [5,7,14]
s2 = set(b)
print(s2)

s.add(5)
print(s)
s.remove(5)
print(s)
'''

#Dictionary
'''
d = {}
d['Teodor'] = 'gillar Geometri'
print(d)
print(d['Teodor'])


primtal = [2,3,5,7,11,13,17,19]
primtalsordning = {}
# Vill göra: primtalsordning[11] = 4
for i in range(len(primtal)):
  primtalet = primtal[i]
  primtalsordning[primtalet] = i
#print(primtalsordning[11])

for i in range(1,21):
  if i in primtalsordning:
    print(primtalsordning[i])
  else:
    print(i,'inte primtal')
'''
