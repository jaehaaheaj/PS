# tag: heap
import heapq
import sys
input=sys.stdin.readline
l=[]
for _ in range(int(input())):
    x=int(input())
    if x!=0:heapq.heappush(l,(abs(x),x>0))
    else:
        t=heapq.heappop(l) if l else (0,0)
        print(t[0]*(1 if t[1] else -1))

# comment: 
# 힙에 넣을때는 절대값으로 넣고 다시 꺼낼 때는 부호를 
# 살려야 해서 위와 같이 (값,부호)쌍을 힙에 넣었다.