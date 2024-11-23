n = int(input())
arr = list(map(int, input().split()))

def bubble_sort(arr):
    size = len(arr)
    check = False

    while check != True:
        check = True

        for i in range(size - 1):
            if arr[i] > arr[i + 1]:
                tmp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = tmp

                check = False

bubble_sort(arr)

for i in arr:
    print(i, end = " ")