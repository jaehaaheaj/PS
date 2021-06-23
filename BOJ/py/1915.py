# tag: DP
a,b=map(int,input().split())
l=[[int(i)for i in input()]for _ in range(a)]
m=max([i[0] for i in l]+l[0])
for i in range(1,a):
    for j in range(1,b):
        l[i][j]*=min(l[i-1][j],l[i][j-1],l[i-1][j-1])+1
        m=max(l[i][j],m)
print(m*m)

# related to: BOJ-4095