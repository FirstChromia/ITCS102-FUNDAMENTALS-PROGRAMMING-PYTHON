print("Welcome to Manhwa king")
print("Please choose a Manhwa of your taste!")
genre = input("Action/Romance/Historical: ")

if genre == "Action":
	print("You selected Action")
	chap = input("How long? short, medium, long: ")
	if chap == "short":
		print("You selected short")
		year = input("What year? 1990,2000,2010: ")
		if year == "1990":
			print("You selected 1990")
			print("Les Bijoux")
		elif year == "2000":
			print("You selected 2000")
			print("Angel Cup")
		elif year == "2010":
			print("You selected 2010")
			print("Return of the Mount Hua Sect")
	elif chap == "medium":
		print("You selected medium")
		year = input("What year? 1990,2000,2010: ")
		if year == "1990":
			print("You selected 1990")
			print("Cheollang Yeoljeon")
		elif year == "2000":
			print("You selected 2000")
			print("The Breaker")
		elif year == "2010":
			print("You selected 2010")
			print("The Boxer")
	elif chap == "long":
		print("You selected long")
		year = input("What year? 1990,2000,2010: ")
		if year == "1990":
			print("You selected 1990")
			print("Sorry no Manhwa available")
		elif year == "2000":
			print("You selected 2000")
			print("Tower of God")
		elif year == "2010":
			print("You selected 2010")
			print("The Northern Blade")

elif genre == "Romance":
	print("You selected Romance")
	chap = input("How long? short, medium, long: ")
	if chap == "short":
		print("You selected short")
		year = input("What year? 1990,2000,2010: ")
		if year == "1990":
			print("You selected 1990")
			print("Lights Out")
		elif year == "2000":
			print("You selected 2000")
			print("11th Cat, Aflame Inferno")
		elif year == "2010":
			print("You selected 2010")
			print("Love at First sight")
	elif chap == "medium":
		print("You selected medium")
		year = input("What year? 1990,2000,2010: ")
		if year == "1990":
			print("You selected 1990")
			print("Queen's Knight,Let Dai")
		elif year == "2000":
			print("You selected 2000")
			print("13th Boy")
		elif year == "2010":
			print("You selected 2010")
			print("Villainess is a Marionette")
	elif chap == "long":
		print("You selected long")
		year = input("What year? 1990,2000,2010: ")
		if year == "1990":
			print("You selected 1990")
			print("Faeries' Landing")
		elif year == "2000":
			print("You selected 2000")
			print("Cheese in the trap")
		elif year == "2010":
			print("You selected 2010")
			print("The Remarried Empress")

elif genre == "Historical":
	print("You selected Historical")
	chap = input("How long? short, medium, long: ")
	if chap == "short":
		print("You selected short")
		year = input("What year? 1990,2000,2010: ")
		if year == "1990":
			print("You selected 1990")
			print("Nambul:War Stories")
		elif year == "2000":
			print("You selected 2000")
			print("Sorry no Manhwa available")
		elif year == "2010":
			print("You selected 2010")
			print("Absurd Armada")
	elif chap == "medium":
		print("You selected medium")
		year = input("What year? 1990,2000,2010: ")
		if year == "1990":
			print("You selected 1990")
			print("Threads of Time")
		elif year == "2000":
			print("You selected 2000")
			print("Snow drop")
		elif year == "2010":
			print("You selected 2010")
			print("Sorry no Manhwa available")
	elif chap == "long":
		print("You selected long")
		year = input("What year? 1990,2000,2010: ")
		if year == "1990":
			print("You selected 1990")
			print("Faeries' Landing")
		elif year == "2000":
			print("You selected 2000")
			print("The Antique gift shop")
		elif year == "2010":
			print("You selected 2010")
			print("Absurd Armada")

else:
	print("Error, Please input the right instructions")
