n = int(input("How many strings:"))
list=[]
sum = 0
total=0

for i in range(n):
    list.append(input(f"Enter string {i+1}:"))
    for j in list[i]:
        total+=len(j)

avrg = total/n
print(avrg)