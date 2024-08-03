def square(n):
    for i in range(1, n * n + 1):
        if i % 9 == 0:
            print(9, end = " ")
        else:
            print(f"{i % 9}", end = " ")

        if i % n == 0:
            print()
            continue

num = int(input())
square(num)