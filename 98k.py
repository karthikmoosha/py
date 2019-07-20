k1=int(input())
m2=list(map(int,input().split()))
for q in range(len(m2)-1):
     if(m2[q]>m2[q+1]):
           print(q)
           break
