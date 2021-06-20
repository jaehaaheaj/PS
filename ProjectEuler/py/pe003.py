# tag: prime factor
n=600851475143
for i in range(3, n+1, 2):
    if i>n: break
    while 1:
        if n%i==0:
            print(i)
            n//=i
        else: break
# 71
# 839
# 1471
# 6857

# ans: 6857