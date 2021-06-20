# tag: prime
n = 2*10**6
q = [1 for _ in range(n)]
p = []
for i in range(2,n):
    if q[i]: p+=[i]
    for j in range(i,n,i):q[j]=0
print(sum(p)) # ans: 142913828922