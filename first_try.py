arr = [1, 2, 3, 4]

'''
last = arr[-1]
arr[-1]=arr[0]
arr[0] = last
'''


def replace_first(array):
    if len(arr) <=1:
        return array
    else:
        array.append(arr[0])
        array.pop(0)
        return array

replace_first(arr)
