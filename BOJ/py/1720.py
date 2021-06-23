# tag: DP
n=int(input())
l=[1,1]
for _ in range(30):l+=[2*l[-2]+l[-1]]
print((l[n]+l[n//2])//2+l[n//2-1]*(1-n%2))