x = 0
dicci = {}
while True:
    x += 1
    var = 0
    for z in range(1,x+1):
        var += z
    factors = []
    for num in range(1,var+1):
        if var%num==0:
            factors.append(var)
    if len(factors)>500:
        print(var)
        break
