ka1=int(input())
mrr=list(map(int,input().split()[:ka1]))
rrm=sorted(mrr)
for i in rrm:
    print(i,end=" ")
