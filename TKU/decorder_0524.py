import math

def decorder(fun):
    def print_(R):
        area = fun(R)
        print('Area %.4f' % area)
        print('面積 %.4f' % area)
        print('면적 %.4f' % area)
    return print_

@decorder
def fun(r):
    return r*r*math.pi

r = int(input('半徑'))
fun(r)