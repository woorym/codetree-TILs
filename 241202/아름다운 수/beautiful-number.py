n = int(input())

answer = []



def is_beautiful():
    i = 0

    while i < n:

        if i + answer[i] - 1 >= n:
            return False


        for j in range(i, i + answer[i]):
            if answer[j] != answer[i]:
                return False
        
        i += answer[i]

    return True

ans = 0
def choose(curr_num):
    global ans

    if curr_num == n + 1:
        if is_beautiful():
            ans += 1
        
        return
    
    for i in range(1, 5):
        answer.append(i)
        choose(curr_num + 1)
        answer.pop()

choose(1)

print(ans)