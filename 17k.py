k1=int(input())
e=len(str(k1))
a=k1
b=0
while k1>0:
  c=k1%10
  k1=k1//10
  d=c**e
  b=b+d
if a==b:
  print("yes")
else:
  print("no")
