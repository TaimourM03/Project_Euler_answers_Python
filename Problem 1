multiples= []
below = 0
total = 0
v1m = 0
v2m = 0
while ((3*(below+1)) < 1000) or ((5*(below+1)) < 1000):
    below += 1
    v1m = 3*below
    v2m = 5*below
    if v2m < 1000 and v1m <1000:
        if v1m not in multiples:
            multiples.append(v1m)
        if v2m not in multiples:
            multiples.append(v2m)
    else:
        if v1m not in multiples:
            multiples.append(v1m)
print(multiples)#all the multiple numbers of 3 and 5
for num in multiples:
    total += num
print(total)#final result
