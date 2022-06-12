def decorderfactory(r):
    def decorder(callback):
        def area():
            AREA = r*r*3.1415926
            callback(AREA)
        return area
    return decorder

@decorderfactory(3)
def fun(AREA):
    print('Area %.4f' % AREA)

@decorderfactory(6)
def fun1(AREA):
    print('面積 %.4f' % AREA)

@decorderfactory(10)
def fun2(AREA):
    print('範圍 %.4f' % AREA)



