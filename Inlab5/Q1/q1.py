from exception import Lab5Exception
from student import Student
import json

class StudentBuilder:
    """
        You are expected to define a static method
        by the name build_student_object. It should take in 
        path to a json file and read the contents of the file.

        You are also expected to validate the contents read from 
        the JSON file and raise Exception accordingly
    """
    created = {}
    
    @staticmethod
    def build_student_object(path):
        try:
            my_file = open(path, 'r')
            field = json.load(my_file)
        except:
            raise Lab5Exception('Error in opening the JSON file (are you sure it is in the correct place?)')
        
        for key in field:
            if key == "name":
                if not isinstance(field[key], str) or len(field[key]) == 0:
                    raise Lab5Exception('Name must be a non-empty string')
            elif key == "gender":
                acceptable = ['Male', 'Female', 'Non-Binary', 'Prefer Not To Say']
                if field[key] not in acceptable:
                    raise Lab5Exception('Gender must be Male, Female, Non-Binary or Prefer Not To Say')
            elif key == "age":
                if not (isinstance(field[key], int) or isinstance(field[key], float)) or field[key] <= 0 or field[key] > 35:
                    raise Lab5Exception('Age must be a number between 0 (exclusive) and 35 (inclusive))')
            elif key == "cgpa":
                if not (isinstance(field[key], int) or isinstance(field[key], float)) or field[key] < 0 or field[key] > 10:
                    raise Lab5Exception('CGPA must be a number between 0 and 10 (both inclusive)')
            else: # key == "home_town"
                if not isinstance(field[key], str) or len(field[key]) == 0:
                    raise Lab5Exception('Home Town must be a non-empty string')
        
        if((field['name'], field['age'], field['cgpa'], field['gender'], field['home_town']) in StudentBuilder.created):
            return StudentBuilder.created[(field['name'], field['age'], field['cgpa'], field['gender'], field['home_town'])]
        else:
            StudentBuilder.created[(field['name'], field['age'], field['cgpa'], field['gender'], field['home_town'])] = Student(field['name'], field['age'], field['cgpa'], field['gender'], field['home_town'])
        return StudentBuilder.created[(field['name'], field['age'], field['cgpa'], field['gender'], field['home_town'])]