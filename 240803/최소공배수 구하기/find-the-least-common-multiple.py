n, m = tuple(map(int, input().split()))

def lcm(n, m):
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            gcd_num = i
            break
    
    lcm_num = (n // gcd_num) * (m // gcd_num) * gcd_num
    return lcm_num

result = lcm(n, m)
print(result)