isSunny = True

while isSunny == True:
    confirm = input("is it sunny outside? yes/no?").lower()

    if confirm =='yes':
        continue
    elif confirm == 'no':
        break
    else:
        print('invalid answer')
