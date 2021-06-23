# tag: constructive
def f(s):
    a,b=s.count('0'),s.count('1')
    if a==b:return str(1-int(s[0]))+f(s[1:])
    else:return(str(int(a>b)))*len(s)
print(f(input()))