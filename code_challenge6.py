print("FACTORIAL PROGRAM")
number = eval(input("Input a number "))
r = 1
for x in range(number, 0, -1):
    r1 = r
    r *= x 
    print(r1, "*", i, "=", r)
print("Factorial of ",number," is ", r)
