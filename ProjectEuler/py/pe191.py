# tag: DP
a=b=d=i=1
c=e=f=0
while i<30:a,b,c,d,e,f,i=a+b+c,a,b,a+b+c+d+e+f,d,e,i+1
print(a+b+c+d+e+f) # ans: 1918080160

# related to: