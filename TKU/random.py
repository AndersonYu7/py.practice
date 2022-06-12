import random

cnt = int(input('亂數個數:'))
num_min = int(input('最小值:'))
num_max = int(input('最大值:'))

print(random.sample(range(num_min,num_max+1),cnt))


