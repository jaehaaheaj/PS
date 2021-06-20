# naive, but short implementation
import datetime
now = datetime.datetime.now

t = now()

n = 10**6
q = [1 for _ in range(n)]
p = []
for i in range(2,n):
    if q[i]: p+=[i]
    for j in range(i,n,i):q[j]=0
print(p[:10])

print(now()-t)

        
