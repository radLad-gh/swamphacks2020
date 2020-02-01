class Course:

    def __init__(self, name, subject, grade):
        self.name = name
        self.subject = subject
        self.grade = grade
    

class Sutdent:

    def __init__(self, name):
        self.name = name
        self.gpa = None
        self.courseHistory = []

    def getAvg(self, subject):
        pass
    
    def addCourse(self, course):
        self.courseHistory.append(course)
    
