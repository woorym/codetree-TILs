def gsd(n, m):
    num = 1
    if n >= m:
        big_num, small_num = n, m
    else:
        big_num, small_num = m, n
    
    for i in range(big_num,0,-1):
        if small_num % i == 0 and big_num % i == 0:
            num = i
            print(num)
            break

num1, num2 = map(int, input().split())
gsd(num1, num2)