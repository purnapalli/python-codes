def fact(n):
    f=1
    while 1<=n:
        f=f*n
        n=n-1
    return f
for i in range(1,6):
    print('factorial of {} is : {}'.format(i,fact(i)))