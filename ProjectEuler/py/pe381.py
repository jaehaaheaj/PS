# tag: prime, Wilson's Theorem, modular multiplicative inverse
def gen_primes_short():
    D,q={},2
    while 1:
        if q not in D:
            yield q;D[q*q]=[q]
        else:
            for p in D[q]:D.setdefault(p+q,[]).append(p)
            del D[q]
        q += 1

n=10**8
g = gen_primes_short()
r=0
cnt=0
while 1:
    p = next(g)
    if p<5:continue
    if p>n:break
    
    s=q=-1
    for i in range(4):
        q*=pow(p-1-i,p-2,p)
        s+=q
    r+=s%p
    cnt+=1
    if cnt%10000==0:print(p)

print(r)