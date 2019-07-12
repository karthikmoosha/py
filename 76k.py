noy1 = int(input())
if noy1 > 2:
    for i in range(2, noy1):
        if noy1 % i == 0:
            print('yes')
            break
    else:
        print('no')
elif noy1 == 2:
    print('no')
