print("ODD NUMBER SUMMARAZATION")
odd = 0
for x in range(10):
    number = eval(input("Input a number "))
    if number % 2 != 0:
        odd += number
        
print("The sum of all odd numbers are", odd,)
