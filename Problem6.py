total_sq = 0
total_sq2 = 0
for num in range(1,101):
    total_sq+=num
    total_sq2+=num*num
total_sq *= total_sq
print("The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is:",total_sq-total_sq2)
