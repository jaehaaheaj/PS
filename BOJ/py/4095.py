# tag: DP
while 1:
    a,b=map(int,input().split())
    if a==0:break
    l=[[*map(int,input().split())]for _ in range(a)]
    m=max([i[0] for i in l]+l[0])
    for i in range(1,a):
        for j in range(1,b):
            l[i][j]*=min(l[i-1][j],l[i][j-1],l[i-1][j-1])+1
            m=max(l[i][j],m)
    print(m)

# related to: BOJ-1915