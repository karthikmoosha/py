pp1,mm1=map(int,input().split())
nnn=[]
tt=[]
gcd=1
for i in range(1,pp1+1):
    if(pp1%i==0):
        nnn.append(i)
for j in range(1,mm1+1):
    if(mm1%j==0):
        tt.append(j)
for y in nnn:
    if y in tt:
        gcd=gcd*y
print(gcd)
