n = int(input())
arr = list(map(int, input().split()))

def select_sort(arr):
    size = len(arr)

    for i in range(size - 1):
        min_index = i
        for j in range(i + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j

        tmp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = tmp

select_sort(arr)

for i in arr:
    print(i, end = " ")