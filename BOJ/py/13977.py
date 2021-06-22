# tag: modular multiplicative inverse
import sys
input=sys.stdin.readline
mod=10**9+7
m=4*10**6

#def p(a,b):return 1 if b==0 else ((p(a,b//2)**2)*(a if b%2 else 1))%mod
# use python pow instead.
# this impl was about 10 times slower on test sets.

f=[1 for _ in range(m+1)]
for i in range(2,m+1): f[i]=f[i-1]*i%mod
fi=[-1 for _ in range(m+1)]

for _ in range(int(input())):
    n,k=map(int,input().split())
    if fi[n-k]==-1:fi[n-k]=pow(f[n-k],mod-2,mod)
    if fi[k]==-1:fi[k]=pow(f[k],mod-2,mod)
    print(f[n]*(fi[n-k]*fi[k]%mod)%mod)