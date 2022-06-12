import math

# def decorderfactory(r):
#     def decorder(callback):
#         def area():
#             AREA = r*r*math.pi
#             callback(AREA)
#         return area
#     return decorder

# r = input('半徑')

# @decorderfactory(int(r))
# def fun(AREA):
#     print('Area %.4f' % AREA)
#     print('面積 %.4f' % AREA)
#     print('면적 %.4f' % AREA)
    
# fun()

def decorder(fun):
    def print_(r):
        print('Area %.4f' % fun(r))
        print('面積 %.4f' % fun(r))
        print('면적 %.4f' % fun(r))
    return print_

@decorder
def fun(r):
    return r*r*math.pi

r = int(input('半徑'))
fun(r)

# fun(3)
# print(fun(3))
