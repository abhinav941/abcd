n = int(input())
if n % 400 == 0:
    print("Yes")
else:
    if n%100!=0 and n%4==0:
        print('yes')
    else:
        print('no')
