MK1=int(input())
n=0
i=0
while(MK1>0):
    i=MK1%10
    n=n+i
    MK1=MK1//10
print(n)
