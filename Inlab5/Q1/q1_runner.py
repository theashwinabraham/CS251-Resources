from q1 import StudentBuilder

if __name__ == '__main__':
    """
        This file is just for your testing purposes.
        An autograder will do a similar thing.
        You DONOT need to submit this file.
    """
    json_file_path = 'test_case_q1.json'
    student_obj = StudentBuilder.build_student_object(json_file_path)
    # Run tests as per your need
    print('Name:', student_obj.get_name())
    print('Age:', student_obj.get_age())
    print('Gender:', student_obj.get_gender())
    print('CGPA:', student_obj.get_cgpa())
    print('Home Town:', student_obj.get_home_town())