list = []
sum = 0
n = int(input("How many numbers do you want to enter? "))
for i in range(n):
    list.append(int(input("Enter a number: ")))
    sum = sum + list[i]**2
print("The sum of squares is:", sum)