class Student: #modelling a student data type

    def __init__(self, name, major, gpa, is_on_probation): # def __init__ and variables, which  self where you reach it you need it define as first
        self.name = name # going to be equal what we pass it, it is referring to the actual object
        self.major = major 
        self.gpa = gpa
        self.is_on_probation = is_on_probation

class Student_2: #modelling a student data type

    def __init__(self, name, major, gpa): # def __init__ and variables, which  self where you reach it you need it define as first
        self.name = name # going to be equal what we pass it, it is referring to the actual object
        self.major = major
        self.gpa = gpa
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return(True)
        else:
            return False