# IMPLEMENTED BY: ASHWIN ABRAHAM

##############################################
"""
Extra functions or variables if required

"""
##############################################


def rotate(arr):

    rotated_array = []

    """
    This function takes a list of lists as input and returns the rotated verion 
    (rotated 90 degrees anti-clockwise)

    Input arguments:
    arr : List of lists

    Returns: rotated_array

    """
    '''m = len(arr)
    if m == 0:
        return []
    elif m == 1:
        return arr
    n = len(arr[0])'''
################################### Add your code here ###################################
    for i in range(len(arr)):
        rotated_array.append([arr[j][len(arr)-1-i] for j in range(len(arr))])
##########################################################################################

    return rotated_array


# Use the main() function only for testing your code

if __name__ == "__main__":
    
    """
    Main function

    Example call:
    You can use the following matrix "test_arr" for testing your solution.
    For running the code, use the command "python q1.py" 
    
    test_arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    rotated_array = rotate(test_arr)
    print(rotated_array)

    Console output should be: [[4, 8, 12, 16], [3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13]]

    """