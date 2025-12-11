mySet = {'peach', 'chips', 'pizza', 'orange', 'apple', 'banana', 'cherry'}
myList = {"apple", "pizza", "banana"}

for i in range(len(myList)):
    mySet.discard(myList[i])

    print(mySet)