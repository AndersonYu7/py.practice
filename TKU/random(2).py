import random

cnt = int(input('亂數個數:'))
num_min = int(input('最小值:'))
num_max = int(input('最大值:'))
a=[None for i in range(cnt)]

i=0
while (i<cnt):
    repeat=0
    a[i]=random.randint(num_min,num_max)
    for k in range(i):
        if(a[i]==a[k]):
            repeat=1
    if (repeat==1):
        i=i-1
    i=i+1

print('[',end = '')
for i in range(cnt):
    if i < cnt-1:
        print(a[i],end=', ')
    else : 
        print(a[i],end='')
print(']')


