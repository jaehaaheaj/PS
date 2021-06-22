# tag: convex hull, rotating callipers
from math import ceil

def f(a,b,c):
    v,w=[b[0]-a[0],b[1]-a[1]],[c[0]-a[0],c[1]-a[1]]
    return v[0]*w[1]-w[0]*v[1]

def diag(a,b,c):
    v,w=[b[0]-a[0],b[1]-a[1]],[c[0]-a[0],c[1]-a[1]]
    return abs(v[0]*w[1]-w[0]*v[1])/(v[0]**2+v[1]**2)**0.5

cn=1
while 1:
    t=int(input())
    if t==0:break
    l = sorted([[*map(int,input().split())]for _ in range(t)])    
    
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

    d=10**9
    n=len(r)
    for i in range(n):
        e=0
        for j in range(n-2):
            e=max(e,diag(r[i],r[(i+1)%n],r[(i+2+j)%n]))
        d=min(d,e)
    print(f'Case {cn}: '+ '{0:.2f}'.format(ceil(d*100)/100))
    cn+=1