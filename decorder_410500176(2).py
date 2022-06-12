import math

def decorder(callback):
    def area_cal():
        r = int(input('半徑'))
        area = r * r * math.pi
        callback(area)
    return area_cal

@decorder
def fun(area):
    print('Area %.4f' % area)
    print('面積 %.4f' % area)
    print('면적 %.4f' % area)

fun()