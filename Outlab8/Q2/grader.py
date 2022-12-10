# IMPLEMENTED BY: ASHWIN ABRAHAM

class Lab5Exception(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def get_error_messaage(self):
        return self.message

def add(arg1, arg2):
    r"""
        This function accepts two arguments - arg1 and arg2.
        It returns the result of the operation (arg1 + arg2).

        You are expected to think of corner cases,
        and appropriately raise Exception.
    """
    try:
        x = arg1 + arg2
    except TypeError:
        raise Lab5Exception('Arguments of these types cannot be added') from None
    except:
        raise Lab5Exception('These two arguments cannot be added') from None
    else:
        return x

def subtract(arg1, arg2):
    r"""
        This function accepts two arguments - arg1 and arg2.
        It returns the result of the operation (arg1 - arg2).

        As the previous function, you are expected to think of corner cases,
        and appropriately raise Exception.
    """
    try:
        x = arg1 - arg2
    except TypeError:
        raise Lab5Exception('Arguments of these types cannot be subtracted') from None
    except:
        raise Lab5Exception('These two arguments cannot be subtracted') from None
    else:
        return x

def divide(arg1, arg2):
    r"""
        This function accepts two arguments - arg1 and arg2.
        It returns the result of the operation (arg1 / arg2).

        You are expected to think of corner cases, and appropriately raise Exception.
    """
    try:
        x = arg1/arg2
    except TypeError:
        raise Lab5Exception('Arguments of these types cannot be divided') from None
    except ZeroDivisionError:
        raise Lab5Exception('Cannot divide by zero') from None
    except:
        raise Lab5Exception('These two arguments cannot be divided') from None
    else:
        return x

def str_left_rotate(arg1, arg2):
    r"""
        This function should left rotate a string by the specified amount.
        arg1 signifies the input string and arg2 signifies the amount of rotation.

        Example - 
        1. str_left_rotate("hello", 2) should return "llohe"
        2. str_left_rotate("hello", 1) should return "elloh"
        3. str_left_rotate("hello", 4) should return "ohell" and so on

        You are not to use any inbuilt string method, the implementation has to be
        done by you!!

        Again, you are expected to think of corner cases, and appropriately raise Exception.
    """
    if not isinstance(arg1, str):
        raise Lab5Exception('First argument must be a string') from None
    if not isinstance(arg2, int):
        raise Lab5Exception('Second argument must be an integer') from None
    if arg2 < 0 or arg2 >= len(arg1):
        raise Lab5Exception('shift must be between 0 (inclusive) and length of string (exclusive)') from None
    # if len(arg1) == 0:
    #     return arg1
    final = ""
    start = arg2#%len(arg1)
    # if arg2 < 0:
    #     if (-arg2)%len(arg1) == 0:
    #         start = 0
    #     else:
    #         start = len(arg1) - ((-arg2)%len(arg1))
    for i in range(len(arg1)):
        final += arg1[(start+i)%len(arg1)]
    return final
    
    

def apply(fn, args):
    r"""
        This is the API end-point available to the grader.
        The grader will supply the function pointer to this function,
        along with the arguments and expect the return value.

        Example - 
        1. apply(add, (2, 3)) will expect 5 as the answer.
        2. apply(subtract, (2, 3)) will expect -1 as the answer.
    """
    try:
        length = len(args)
    except:
        raise Lab5Exception('Incorrect syntax of passing arguments') from None
    else:
        if(length!=2):
            raise Lab5Exception('Incorrect number of arguments')
        if fn not in [add, subtract, divide, str_left_rotate]:
            raise Lab5Exception('The given function is not in the list of allowed functions (add, subtract, divide, str_left_rotate)')
        try:
            x = args[0]
            y = args[1]
        except:
            raise Lab5Exception('Incorrect syntax of passing arguments') from None
        else:
            return fn(x, y)