M1,K1=map(int,input().split())
count=0
arr=list(map(int,input().split()))[:M1]
for i in arr:
  if i==K1:
    count+=1
print(count)
