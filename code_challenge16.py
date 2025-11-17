import os
isbeky = True
GeID = {}
while isbeky == True:
    print("you are beky")

    becky = input("Are you Ge? y/n if you have Ge ID please type 'i like men' not sure? type f ").lower()

    if becky.lower() == 'y':
        print("you are Ge")
        ID = input("Please input a number for ge ID ")

        what = input("What kind of Ge? Bading/Gooding/Tomboy ")
        why = input("Why are you Ge? ")
        how = input("How Ge are you? rate yourself 1-10 ")

        GeID = {ID : [what,why,how]}
        print("You now have Ge ID")

        os.system('cls')
        continue
    elif becky.lower() == 'f':
        GE = input("Input Ge ID")
        for G in GeID.keys():
            if GE in GeID.keys():
                print("Ge ID found")
            else:
                print("U no Ge >:( ")
        continue
    elif becky.lower() == 'i like men':
        os.system('cls')
        print("Gaaaayyyyyy")
        print(GeID)
        continue
    elif becky.lower() == 'n':
        print("you are strit, get out!")
        break
    else:
        print("Answer Properly >:( ")
        continue