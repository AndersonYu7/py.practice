from sys import stdin

for s in stdin:
    s = s.replace('/','//')
    print(eval(s))