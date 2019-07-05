km1=input()
h1=0
for i in range(len(km1)):
  if(km1[i].isdigit() or km1[i].isalpha() or km1[i]==(" ")):
    continue
  else:
    h1+=1
print(h1)
