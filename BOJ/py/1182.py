# tag: DP
n,s=map(int,input().split())
l=[*map(int,input().split())]
d={0:1}
for i in l:
    e={k+i:d[k]for k in d}
    for k in e:
        if k in d: d[k]+=e[k]
        else: d[k]=e[k]
d[0]-=1 # empty subset case
print(d.get(s,0))