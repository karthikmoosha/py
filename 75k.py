strgs1=list(input())
if len(strgs1)%2==0:
    strgs1[int(len(strgs1)/2)] ='*'
    strgs1[int(len(strgs1)/2)-1]='*'
else:
    strgs1[int(len(strgs1)/2)] ='*'
for i in range(0,len(strgs1)):
    print(strgs1[i],end='')
