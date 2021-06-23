# tag: convex hull
def f(a,b,c):
    v,w=[b[0]-a[0],b[1]-a[1]],[c[0]-a[0],c[1]-a[1]]
    return v[0]*w[1]-w[0]*v[1]

l = sorted([[*map(int,input().split())]for _ in range(int(input()))])
r=[]
h=[]
for i in l:
    while len(h)>=2 and f(h[-2],h[-1],i)<=0: h.pop()
    h+=[i]
r+=h
h=[]
for i in l[::-1]:
    while len(h)>=2 and f(h[-2],h[-1],i)<=0: h.pop()
    h+=[i]
r+=h[1:-1]
print(len(r))

# related to: BOJ-4225