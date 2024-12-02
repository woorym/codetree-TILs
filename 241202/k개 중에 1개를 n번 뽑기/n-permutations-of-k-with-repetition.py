k, n = map(int, input().split())

arr = []

def print_answer():
    for elem in arr:
        print(elem, end = " ")
    print()
    return

def choose(curr_num):
    if curr_num == n + 1:
        print_answer()
        return
    
    for i in range(1, k + 1):
        arr.append(i)
        choose(curr_num + 1)
        arr.pop()

choose(1)