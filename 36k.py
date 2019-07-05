k1=input()
m1=0
for  i in range(len(k1)):
  if(k1[i].isdigit() or k1[i].isalpha() or k1[i]==(" ")):
    continue
else:
  m1+=1
print(m1)
