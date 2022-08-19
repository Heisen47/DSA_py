def binary_search(list ,target):
    first = 0
    last = len(list)-1
    while first <= last:
        midpoint = (first + last) // 2
        if list[midpoint]== target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint +1
        else:
            last = midpoint -1

    return None

list = [2,5,6,7,8,9,35,54,66]
print("the index of the value is:",binary_search(list , 35))
