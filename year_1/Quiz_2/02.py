# Bubble sort
def merge(a, b):
    merge_list = []
    merge_list.extend(a)
    merge_list.extend(b)  

    if all(isinstance(x, int) for x in merge_list):
        for i in range(len(merge_list)):
            for j in range(0, len(merge_list) - i - 1):
                if merge_list[j] > merge_list[j + 1]:
                    merge_list[j], merge_list[j + 1] = merge_list[j + 1], merge_list[j]
    else:
        for i in range(len(merge_list)):
            for j in range(0, len(merge_list) - i - 1):
                first, second = merge_list[j], merge_list[j + 1]
                minimum_len = min(len(first), len(second))
                index = 0
                while index < minimum_len and first[index] == second[index]:
                    index += 1
                if index < minimum_len:
                    if ord(first[index]) > ord(second[index]):
                        merge_list[j], merge_list[j + 1] = merge_list[j + 1], merge_list[j]
    return merge_list

def getInput():
    a = eval(input('Enter list a: '))
    b = eval(input('Enter list b: '))

    return a, b

a, b = getInput()
res = merge(a, b)

print(res)

