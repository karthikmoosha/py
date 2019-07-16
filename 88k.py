k12,m22=map(int,input().split())
if(k12>m22):
  great=k12
else:
  great=m22
while(True):
  if((great%k12) == 0 and (great%m22) == 0):
    lcm=great
    break
  great=great+1
print(lcm)
