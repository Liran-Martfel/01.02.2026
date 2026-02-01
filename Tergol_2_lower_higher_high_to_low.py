lower: int = int(input("please enter a low number: "))
higher: int = int(input("please enter a high number: "))
for i in range(higher, lower -1, -1):
    print (i, end = " ")