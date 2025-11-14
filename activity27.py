def ani():
    for anime in empt.items():
        print(f"Anime {anime}")
def search(keys):
    print("Searching")
    print(f"Result {empt[keys]}")
cont = True
empt = {}
while cont == True:
    keys= input("key")

    value = input("Val")

    empt[keys] = value

    choice = input("select").lower()

    if choice.lower() == 'y':
        print("Cont")
        continue
    elif choice.lower() == 'n':
        print("program stops")
        break
    elif choice.lower() == 'p':
        ani()
        continue
    elif choice.lower() == 's':
        search(keys)
        continue
    else:
        ("invalid")
        continue