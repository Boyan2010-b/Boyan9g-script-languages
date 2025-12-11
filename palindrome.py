string = input("Enter your string:")
count = len(string)
palindrom = True;

for i in range(count//2):
    if string[i] != string[count-1-i]:
        palindrom = 0
        break

if palindrom == 0:
    print(f"{string} NO")
else:
    print(f"{string} YES")