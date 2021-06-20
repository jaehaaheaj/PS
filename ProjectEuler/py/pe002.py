# tag: simple DP
a,b,n=1,2,0
while 1:
    if b>4*10**6:break
    if b%2==0:n+=b
    a,b=b,a+b
print(n) # ans: 4613732
