def calculation():
    candidates=[]
    for number1 in range(1,333):
        for number2 in range(1,1001):
            for number3 in range(1,1001):
                if number1<number2<number3 and number1+number2+number3==1000:
                    square_oper = (number1 * number1) + (number2 * number2)
                    if square_oper == (number3*number3):
                        candidates.append([number1,number2,number3])
                        return candidates
candidates = calculation()
print("The numbers are:",*candidates,"and the product abc equals to:",candidates[0][0]*candidates[0][1]*candidates[0][2])
