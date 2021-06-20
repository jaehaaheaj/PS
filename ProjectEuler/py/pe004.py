# tag: brute force
s=-1
for i in range(1000):
    for j in range(1000-1,-1,-1):
        if str(i*j)==str(i*j)[::-1]: s=max(s,i*j)
print(s) # ans: 906609
