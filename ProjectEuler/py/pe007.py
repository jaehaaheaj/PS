# tag: prime
n = 10**6
q = [1 for _ in range(n)]
p = []
for i in range(2,n):
    if q[i]: p+=[i]
    for j in range(i,n,i):q[j]=0
print(len(p)) # 78498. n is large enough.

print(p[10000]) # ans: 104743