def split(word): #this function will split a word character by character
    return [char for char in word]
def pal_calc():
    palindromes={}
    for num1 in range(999,99,-1):
        for num2 in range(999,99,-1):
            num = split(str(num1*num2))
            palind = []
            if len(num)%2!=0: #even
                num.pop(int(len(num)/2))
            for pos in range(int(len(num)/2)):
                pos2 = pos+(pos+1)
                if num[pos]==num[pos-pos2]:
                    palind.append(True)
            if len(palind)==int(len(num)/2):
                palindromes[num1*num2]=[num1,num2]
    print(palindromes,len(palindromes))
    return max(list(palindromes.keys())), palindromes.get(max(list(palindromes.keys())))
pal, nums = pal_calc()
print("The largest palindrome made from the product of two 3-digit numbers is:",pal,"=",nums[0],"x",nums[1])
