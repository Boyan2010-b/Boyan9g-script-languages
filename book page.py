count = int(input("How many digits are used to number the pages:"))
pages = 0
digits =1
start = 1

while(count>0):
    end =start*10-1
    pages_in_range = end-start+1
    digit_cost = pages_in_range*digits
    if count>= digit_cost:
        pages+=pages_in_range
        count-=digit_cost
    else:
        pages+= count//digits
        break
    digits += 1
    start*=10

print("Pages",pages)