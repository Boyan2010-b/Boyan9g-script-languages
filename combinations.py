def find_combinations(numbers, k):
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] > k:
                print(f"{numbers[i]} {numbers[j]}")
if __name__ == "__main__":

    n = int(input())
    k = int(input())
    numbers = int(input())

    print(f"Input datas:")
    print(f"N = {n}")
    print(f"K = {k}")
    print(f"Numbers: {numbers}")
    print("\nExit:")
    find_combinations(numbers, k)

