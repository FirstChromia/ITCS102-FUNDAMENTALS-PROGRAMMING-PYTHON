print("MULTIPLICATION TABLE MAKER")
num = eval(input("Enter a number: "))
print("\nMultiplication table for ",num ,)
for x in range(1, 11):
  n_num = num * x
  print(num ,"x",x ,"=",n_num,)
