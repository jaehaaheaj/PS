# modular multiplicative inverse
mod=10**9+7
size=10**5

# f: list of (n! % mod)
f=[1 for _ in range(size+1)]
for i in range(2,size+1): f[i]=f[i-1]*i%mod

# p: calc power(a,n) in O(log n)
#def p(a,b):return 1 if b==0 else ((p(a,b//2)**2)*(a if b%2 else 1))%mod
# but, python's internal implementation is stronger.

# use Fermat's little theorem to get
# 'modular multiplicative inverse' of n!
n = 3
print(pow(f[n],mod-2,mod))
