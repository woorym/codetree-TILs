k, n = map(int, input().split())


arr= []

def print_answer():
    check = [0]
    cnt = 0
    for i in range(len(arr) - 1):        
        if arr[i] == arr[i + 1]:
            cnt += 1
        else:
            cnt = 0
        check.append(cnt)
    # print(check)

    if max(check) < 2:
        for i in arr:
            print(i, end = " ")
        print()
        return

def again(current):
    if current == n + 1:
        print_answer()
        return

    for i in range(1, k + 1):
        arr.append(i)
        again(current + 1)
        arr.pop()


again(1)

