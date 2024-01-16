'''
Defining what a student is. def __init__(self). You then add the values you want the student to have. A student has all the attributes listed below.
'''

class student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation