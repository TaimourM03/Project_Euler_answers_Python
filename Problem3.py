number = 600851475143
numbers=[]
while number != 1:
    for num in range(2,99999):
        if number%num==0:
            numbers.append(num)#num is a prime factor of number
            number /= num
            break
print(max(numbers))#final result
