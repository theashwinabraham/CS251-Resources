# IMPLEMENTED BY: ASHWIN ABRAHAM

import exception

def isSet(iterable):
    my_dict = {}
    for x in iterable:
        if x in my_dict:
            return False
        my_dict[x] = 1
    return True

def set_union(collection_one, collection_two):
    """
        This function, as the name implies, should output 
        the result of union of two sets. Note that the input might not
        be valid sets. You are to check the validity. 

        You are expected to think of all possible corner cases of 
        you code and raise Exception accordingly.
    """
    if not(isSet(collection_one) and isSet(collection_two)):
        raise exception.Lab5Exception('One of the inputs cannot represent a set')
    
    l = []
    for val in collection_one:
        l.append(val)
    for val in collection_two:
        if val not in collection_one:
            l.append(val)
    return l

def set_intersection(collection_one, collection_two):
    """
        This function, as the name implies, should output 
        the result of intersection of two sets. Note that the input might not
        be valid sets. You are to check the validity. 

        You are expected to think of all possible corner cases of 
        you code and raise Exception accordingly.
    """
    if not (isSet(collection_one) and isSet(collection_two)):
        raise exception.Lab5Exception('One of the inputs cannot represent a set')
    
    l = []
    for val in collection_one:
        if val in collection_two:
            l.append(val)
    return l

def set_equality(collection_one, collection_two):
    """
        This function, as the name implies, should check whether
        or not two sets are equal. Note that the input might not
        be valid sets. You are to check the validity. 

        You are expected to think of all possible corner cases of 
        you code and raise Exception accordingly.
    """
    if not(isSet(collection_one) and isSet(collection_two)):
        raise exception.Lab5Exception('One of the inputs cannot represent a set')
    
    for val in collection_one:
        if val not in collection_two:
            return False
    for val in collection_two:
        if val not in collection_one:
            return False
    return True

def parse_file(file_name):
    """
        This function is expected to parse a text (.txt) file
        and extract pairs of collections from it.

        Note that the parsed collections might not be valid sets.
        Please check and accordingly raise Exception. You should also
        think about other corner cases of your code and raise the Exception
        accordingly.
    """
    l = []
    with open(file_name) as f:
        for line in f:
            coll = line.split('    ')
            l.append((eval(coll[0]), eval(coll[1])))
    return l