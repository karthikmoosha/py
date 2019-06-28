k1,m1=map(int,input().split())
for g in range(k1+1,m1):
  z=0
  s=g
  while(s>0):
    a=s%10
    s=s//10
    b=a**3
    z=z+b
  if(g==z):
      print(z,end=" ")
