import sys,random

size = int(input("size: "))
min = int(input("min: "))
max = int(input("max: "))
a=[None for i in range(size)]

i=0
while (i<size):
    repeat=0
    a[i]=random.randint(min,max)
    for k in range(1,i+1):
        if(a[i]==a[i-k]):
            repeat=1
    if (repeat==1):
        i=i-1
    i=i+1


for i in range(size):
    print(a[i])


