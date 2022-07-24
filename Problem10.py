prime_numbers =[]
num = 2
def calculation(prime_numbers,num):
    while True:
        for x in range(1,num+1):
            if num%x==0 and x!=1 and x!=num:
                num += 1
                break
            elif x==num:
                if num < 2000000:
                    prime_numbers.append(num)
                    num +=1
                else:
                    return prime_numbers
print(sum(calculation(prime_numbers,num)))

