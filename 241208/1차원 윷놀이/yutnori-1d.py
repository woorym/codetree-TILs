import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
dist = list(map(int, input().split()))


graph = [i for i in range(1, m + 1)]

arr = [0] * k
num = 0

def print_answer(num):
    cnt = 0
    # for i in arr:
    #     print(i, end = " ")
    # print()
    for i in arr:
        if i >= 6:
            cnt += 1
    
    result = max(num, cnt)
    return result

def again(current, check, pt):
    global num
    if current == n + 1:
        num = print_answer(num)
        return

    for i in range(k):
        if pt > i:
            continue
        # print(f"i : {i}, current : {current}, check : {dist[check]}")
        arr[i] += dist[check]
        again(current + 1, check + 1, i)
        arr[i] -= dist[check]

     
again(1, 0, -1)
print(num)

