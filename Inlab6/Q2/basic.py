# AUTHOR: ASHWIN ABRAHAM

def binarySearch(arr, val):
    '''This function does a binary search for an element in the array.

    :param arr: An homogenous iterable of totally ordered objects
    :param val: An object of the same type as the array elements
    :return: The index at which the element occurs (-1 if the element is not present in the list)
    :rtype: Integer
    '''
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l+r) // 2
        if arr[m] > val:
            r = m-1
        elif arr[m] < val:
            l = m+1
        else:
            return m
    return -1