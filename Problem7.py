prime_numbers =[]
num = 2
while len(prime_numbers) < 10001:
    prime_num = []
    for x in range(1,num+1):
        if num%x==0 and x!=1 and x!=num:
            num += 1
            break
        else:
            prime_num.append(x)
    if len(prime_num)==num:
        prime_numbers.append(num)
        num += 1
        print(len(prime_numbers))
print(prime_numbers[-1])#the 10001st prime number
