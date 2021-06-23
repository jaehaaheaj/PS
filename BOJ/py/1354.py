# tag: DP
n,p,q,x,y=map(int,input().split())
d={0:1}
def f(n):
    d[n]=d[n] if n in d else f(max(n//p-x,0))+f(max(n//q-y,0))
    return d[n]
print(f(n))

# related to: BOJ-1351