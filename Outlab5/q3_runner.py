from q3 import *

if __name__ == '__main__':
    file_name = 'q3_test_case.txt'

    parsed_pairs = parse_file(file_name)

    test_union = set_union([1, 2, 3], ['a', 'b'])
    print(test_union)
    test_intersection = set_intersection((1, 2, 3), ('a', 'b'))
    print(test_intersection)
    print(set_equality((1, 2, 3), ['a', 'b']))