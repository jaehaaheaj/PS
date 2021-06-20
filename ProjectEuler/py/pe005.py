# tag: prime factor

def pf(n):
    res = {}
    for i in range(2, n+1):
        if i>n: break
        while 1:
            if n%i==0:
                if i in res: res[i]+=1
                else: res[i]=1
                n//=i
            else: break
    return res

d={}
for i in range(2,20):
    t=pf(i)
    for k in t:
        if k in d: d[k]=max(d[k],t[k])
        else: d[k]=t[k]

x=1
for k in d:
    i=d[k]
    while i:
        x*=k
        i-=1
print(x) # ans: 232792560