num = 20
while True:
    numbers = []
    for x in range(1,21):
        if num%x==0:
            numbers.append(num)
        else:
            num +=1
            break
    if len(numbers) == 20:
        print(num, "is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20")
        break
