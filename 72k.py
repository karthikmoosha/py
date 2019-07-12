num1 = input()
key = 'aeiou'
for i in key:
    if i in num1:
        num1 = ''
        break
    else:
        continue
if num1 == '':
    print('yes')
else:
    print('no')
