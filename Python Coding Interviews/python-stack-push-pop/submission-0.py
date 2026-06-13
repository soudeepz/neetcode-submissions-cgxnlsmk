from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    rev_arr = []
    n = len(arr)
    while n > 0:
        rev_arr.append(arr.pop())
        n -= 1
    return rev_arr


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
