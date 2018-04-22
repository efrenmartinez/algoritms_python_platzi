xs = [()]
res = [False] * 2
if xs:
    res[0] = True
    print(1)
if xs[0]:
    res[1] = True
    print(0)