def base0(func):
    def base1(r):
        print(f"面積: {func(r)}")
        print(f"Area: {func(r)}")
        print(f"範囲: {func(r)}")
    return base1

@base0
def t(R):
    return R*R*3.14159

r = int (input("Enter the radius"))
t(r)