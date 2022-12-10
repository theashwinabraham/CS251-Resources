# IMPLEMENTED BY: ASHWIN ABRAHAM

class Student:
    def __init__(self, name, age, cgpa, gender, home_town):
        self.name = name
        self.age = age
        self.cgpa = cgpa
        self.gender = gender
        self.home_town = home_town

    def get_name(self):
        """
            Returns the name attribute
        """
        return self.name
    
    def get_age(self):
        """
            Returns the age attribute
        """
        return self.age

    def get_cgpa(self):
        """
            Returns the cgpa attribute
        """
        return self.cgpa
    
    def get_gender(self):
        """
            Returns the name attribute
        """
        return self.gender

    def get_home_town(self):
        """
            Returns the home_town attribute
        """
        return self.home_town