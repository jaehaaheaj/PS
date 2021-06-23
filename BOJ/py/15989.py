# tag: DP
l = [[0]*10001 for _ in range(3)]
l[0][1]=l[0][2]=l[0][3]=l[1][2]=l[1][3]=l[2][3]=1

for i in range(4,10001):
    l[0][i]=l[0][i-1]
    l[1][i]=l[0][i-2]+l[1][i-2]
    l[2][i]=l[0][i-3]+l[1][i-3]+l[2][i-3]

for _ in range(int(input())):
    n=int(input())
    print(l[0][n]+l[1][n]+l[2][n])