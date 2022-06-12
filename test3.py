import math
g = 9.80665
i = 45
j = 90
v0_ = 10

# while True:
#     if i<55:
#         a = (v0_**2* math.sin(math.radians(2*i))) / g
#         print(a)
#         i+=1
#     else : 
#         break

a = (v0_**2* math.sin(math.degrees(2*i))) / g
b = (v0_**2* math.sin(math.radians(2*i))) / g
c = 10**2*math.sin(90)
d = math.sin(math.radians(90))
print(a)
print(b)
print(c)
print(d)
