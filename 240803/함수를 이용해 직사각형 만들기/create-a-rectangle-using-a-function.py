def rectangle(n, m):
    for _ in range(n):
        print("1" * m)

num1, num2 = map(int, input().split())
rectangle(num1, num2)