# part 1. get convex hull from given points on xy-plane.

# cross product of vec(b-a) and vec(c-a)
def f(a,b,c):
    v,w=[b[0]-a[0],b[1]-a[1]],[c[0]-a[0],c[1]-a[1]]
    return v[0]*w[1]-w[0]*v[1]

# sort points
l = sorted([[*map(int,input().split())]for _ in range(int(input()))])
r=[]
h=[]
# lower half
for i in l:
    while len(h)>=2 and f(h[-2],h[-1],i)<=0: h.pop() # 
    h+=[i]
r+=h
h=[]
# upper half
for i in l[::-1]:
    while len(h)>=2 and f(h[-2],h[-1],i)<=0: h.pop()
    h+=[i]
r+=h[1:-1]
# convex hull
print(r)

# part 2. get diameter of convex hull by using rotating callipers technique.

# given point a, b and c, get distance to point c from line [a,b] with following formula:
# |vec(b-a) X vec(c-a)| = |vec(b-a)|*|vec(c-a)|*sin(theta) ... (1)
# dist = |vec(c-a)|*sin(theta) ... (2)
# by (1) and (2), dist = |vec(b-a) X vec(c-a)|/|vec(b-a)|
def diam(a,b,c):
    v,w=[b[0]-a[0],b[1]-a[1]],[c[0]-a[0],c[1]-a[1]]
    return abs(v[0]*w[1]-w[0]*v[1])/(v[0]**2+v[1]**2)**0.5

d=10**9 # large value. like inf.
n=len(r)
for i in range(n):
    e=0
    for j in range(n-2): # naive implementation with time complexity O(n^2)
        e=max(e,diam(r[i],r[(i+1)%n],r[(i+2+j)%n]))
    d=min(d,e)
print(d)