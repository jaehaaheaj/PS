# get prime factors of one integer. naive.
def pf(n):
    res = {}
    for i in range(2, n+1):
        if i>n: break
        while 1:
            if n%i==0:
                if i in res: res[i]+=1
                else: res[i]=1
                n//=i
            else: break
    return res
