list = ('apple', 'orange', 'watermelon', 'banana', 'apple')

dublicates = False

for i in range(len(list)):
    if list.count(list(i)) > 1:
        dublicates = True

        if dublicates:
            print("There ARE Dublicates")
        else:
            print("No Dublicates")