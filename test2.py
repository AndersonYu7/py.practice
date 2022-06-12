a = input("")
b = input("")
c = input("")

if b<c:
    b,c = c,b
    print(b)
    print(c)
if a<c:
    a,c = c,a
    print(a)
    print(c)
if a<b:
    a,b = b,a
    print(a)
    print(b)

print(a,b,c)