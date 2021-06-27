import sys
input=sys.stdin.readline
for _ in range(3):
    s=0
    for _ in range(int(input())):s+=int(input())
    print('-'if s<0 else ('+'if s>0 else 0))
