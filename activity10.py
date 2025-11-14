name = input("What is you name? ")
isStudent = input("Are you a Student? (Yes/No) ").lower()
fare = eval(input("bayad "))

if isStudent.lower() == "yes" :
	discount = fare * .2
	new_fare = fare - discount
	print("Hi", name," student discount is ", discount," your fare is ", new_fare)
else:
	print("Sorry but you are not a Student")