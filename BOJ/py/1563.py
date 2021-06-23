# tag: DP
a=b=d=i=1
c=e=f=0
n=int(input())
while i<n:a,b,c,d,e,f,i=a+b+c,a,b,a+b+c+d+e+f,d,e,i+1
print((a+b+c+d+e+f)%10**6)

# related to: PE-191