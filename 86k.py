k1=list(input())
p1=[]
for i in k1:
    if i not in p1:
        p1.append(i)
if(k1==p1):
    print("Yes")
else:
    print("No")
