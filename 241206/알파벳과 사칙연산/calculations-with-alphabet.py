import sys
input = sys.stdin.readline

express = list(input())

str_set = []
# 총 문자 개수
for i in range(0, len(express), 2):
    str_set.append(express[i])

# 중복 제거 문자
str_arr = set(str_set)
# 중복 제거 문자 개수
str_num = len(str_arr)
# 부호 개수
sign = len(express) // 2

num_list = []
arr = []

def calculate(arr):
    str_dict = {}
    for i, j in zip(str_arr, arr):
        str_dict[i] = j
    # print(f"str_dict : {str_dict}, str_set[0] : {str_set[0]}, result : {str_dict[str_set[0]]}")
    result = str_dict[str_set[0]]
    for i in range(2, len(express), 2):
        if express[i - 1] == '-':
            result -= str_dict[express[i]]
        elif express[i - 1] == '+':
            result += str_dict[express[i]]
            # print(result)
        elif express[i - 1] == '*':
            result *= str_dict[express[i]]

    return result


def again(current):
    if current == str_num + 1:
        # print(arr)
        num = calculate(arr)
        num_list.append(num)
        return
    
    for i in range(1, 5):
        arr.append(i)
        again(current + 1)
        arr.pop()
        


again(1)

print(max(num_list))