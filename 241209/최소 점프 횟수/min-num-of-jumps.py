import sys
input = sys.stdin.readline
max_num = sys.maxsize


n = int(input())
num_list = list(map(int, input().split()))
arr= [max_num]
cnt = 0
def again(current, cnt):
    if current == n - 1:
        arr.append(cnt) 
        return
    if current < n:
        for i in range(1, num_list[current] + 1):
            cnt += 1
            again(current + i, cnt)
            cnt -= 1



again(0, 0)
if len(arr) == 1:
    print(-1)
else:
    print(min(arr))