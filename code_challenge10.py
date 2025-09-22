print("\t\t   *")
for x in range(1,11,1):
    for y in range(11,x,-1):
        print(" ", end=' ')
    for z in range(1,x,1):
        print("*", end=" ")
    for t in range(1,x,1):
        print("*", end=" ")
    print()