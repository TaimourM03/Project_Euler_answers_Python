Fib_seq=[1,2]
num = 0
while (Fib_seq[-1]+Fib_seq[-2]) < 4000000:
    Fib_seq.append(Fib_seq[-1] + Fib_seq[-2])  # all the Fib sequence numbers
for number in Fib_seq:
    if number%2==0:
        num += number #final result
print(Fib_seq);print(num)
