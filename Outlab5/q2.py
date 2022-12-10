# IMPLEMENTED BY: ASHWIN ABRAHAM

#######################################

"""
Import any libraries if required
Extra functions or variables if required

"""
#######################################
def weirdProblem(L):
    
    converted_string = ""

    """
    This function takes a list of lists as input and returns a string which is a
    concatenation of elements 
    Input arguments:
    L : List of lists

    Returns: converted_string
	string

    """
    if len(L) == 0:
        return converted_string
################################### Add your code here ###################################
    positions = [0 if len(x) > 0 else -1 for x in L]
    curr_list = 0
    num_minus1 = 0
    while True:
        if positions[curr_list] == -1:
            num_minus1 += 1
            if num_minus1 == len(L):
                break
        else:
            num_minus1 = 0
            converted_string += L[curr_list][positions[curr_list]]
            converted_string += " "
            if positions[curr_list] == len(L[curr_list]) - 1:
                positions[curr_list] = -1
            else:
                positions[curr_list] += 1
        curr_list = (1 + curr_list)%len(L)
##########################################################################################
    converted_string = converted_string[:-1]
    return converted_string


if __name__ == "__main__":

    """
    Main function

    Example call:
    You can use the following list of lists "L" for testing your solution.
    For running the code, use the command "python q2.py" 
    
    L = [ ["this", "programming", "is"], ["is", "assignment", "kinda"], ["a", "which", "weird"]  ]
    converted_string = weirdProblem(L)
    print(converted_string)

    Console output should be: this is a programming assignment which is kinda weird

    """
