# tag: DP
n,p,q=map(int,input().split())
d={0:1}
def f(n):
    x=d[n] if n in d else f(n//p)+f(n//q)
    d[n]=x
    return x
print(f(n))

# related to: BOJ-1354