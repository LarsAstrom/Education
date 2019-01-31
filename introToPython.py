# Lista:
a = [1]*10
print(a)
a[0] = 2
print(a)
a[9] = 4
print(a)
a[-1] = 5
print(a)
print(sum(a))
print(max(a))
print(min(a))
b = [1,2,3,'FlerSiffror','Sträng',9,True,False]
print(b)
c = []
c.append(1)
c.append('Lars')
c.append([])
print(c)
c[2].append(37)
d = [1,2,3,4]
print(d)
d.append(5)
print(d)
e = d.pop()
print(d,e)
e = d.pop(0)
print(d,e)
f = [[] for _ in range(5)]
print(f)
f = [[i] for i in range(5)]
print(f)


# For loop:
n = 10
for i in range(n):
    print(i)
for i in a:
    print(i)

# While:
s = 0
t = 0
while s < 1000:
    t += 1
    s += t
    print(s)

# Booleaner och if:
bol = True
if bol:
    print('Lars är bäst')
bol = False
if bol: print('Nähäää, du')

# Inputläsning
b = input()
print(b, type(b))
b = int(b)
print(b, type(b))
c,d = map(int,input().split())
print(c,d)
print(c/d)
print(c//d)
li = list(map(int,input().split()))
print(li)
print(' '.join(map(str,li)))
# Input i python2: raw_input() istället för input()
# Då blir print lite annorlunda (ex. printar tuplar).

# Metoder
def gcd(a,b):
    if a == b: return a
    else: return gcd(min(a,b-a),max(a,b-a))

print(gcd(385,3718))

# Maps
d = {}
d['a'] = 1
d[1] = 'a'
print(d)
for i in range(3):
    s = input()
    if s in d.keys(): print(d[s])

# Tuple
a = (1,2)
print(a)
def hej(a,b):
    return a,b
c,d = hej(a[1],a[0])
f = hej(1,2)
print(c,d,a,f)
# a[0] = 1 ger Fel!
