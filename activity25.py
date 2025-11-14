iscont = True

while iscont == True:
    print("welcome AM")
    print("you will be put under a test.")

    iscont = choose = input("choose between a/b/c/d ").lower()
    if choose.lower() == ("a"):
        print("you choose a")
        pass
        continue
    elif choose.lower() ==("b"):
        print("you choose b")
        pass
        continue
    elif choose.lower() ==("c"):
        print("you choose c")
        pass
        continue
    elif choose.lower() ==("d"):
        print("you choose d")
        pass
        break
    else:
        ("invalid answer")
        pass
        continue