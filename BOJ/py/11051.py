# tag: modular multiplicative inverse
mod=10007
size=1000
f=[1 for _ in range(size+1)]
for i in range(2,size+1): f[i]=f[i-1]*i%mod
a,b=map(int,input().split())
print(f[a]*pow(f[a-b],mod-2,mod)*pow(f[b],mod-2,mod)%mod)