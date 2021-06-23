# tag: combinatorial
s=0
x=100
# inc: 10Hx = (9+x)C(x)
m=1
for i in range(9):m*=9+x-i
for i in range(9):m//=i+1
s+=m
# dec: 11Hx - 2Hx + 1 = (10+x)C(x) - (1+x)C(x)
m=1
for i in range(10):m*=10+x-i
for i in range(10):m//=i+1
mm=1
for i in range(1):mm*=1+x-i
for i in range(1):mm//=i+1
s+=m-mm
# inc==dec: 9*x+1
s-=9*x+1

print(s) # ans: 51161058134250