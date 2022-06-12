import time
import math
g = 9.81
def distance(v0, degree):
    return (v0**2*math.sin(math.radians(2*degree)))/g

def velocity(distance,degree):
    return ((distance*g)/(math.sin(math.radians(2*degree))))**0.5

print('estimated velocity=%.2f' % velocity(0.54,41))

dis = 0.38
i = 0
while (dis - distance(velocity(0.54,41),i)) >= 0.0001:
    print('estimated_distance=%.2f' % distance(velocity(0.54,41),i))
    time.sleep(1)
    i+=1
print('estimated_distance=%.2f' % distance(velocity(0.54,41),i))
print('Theda',i)