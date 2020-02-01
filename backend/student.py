"""
Main student file - contains class Object constructors for classData and Student
Available functions:
    getAvg
    addClass
"""

class classData: #Constructor for classes
    def __init__(self, name, category, credits, prereq, coreq):
        self.name = name
        self.category = category
        self.credits = credits
        self.prereq = prereq
        self.coreq = coreq
        self.grade = 0

myClass_01 = classData('COP3502', 'Programming', 3, 'MAC2311', '')
print(myClass_01.name)
myClass_01.grade = 3.0

class Student: #Constructor for class, gpa dictionary is current placeholder
    def __init__(self, name):
        self.name = name
        self.gpa = {
            'Math': 4.0,
            'English': 3.5
        }
        self.classes = [
        ] #classes will be array that holds classData objects

    def getAvg(self, category):
        total = 0
        counter = 0
        for x in self.classes:
            if x.category == category:
                total += x.grade
                counter += 1
        if counter == 0:
            return 0
        return total/counter

myStudent_01 = Student('Masen') #test student construction

def addClass(grade, c=classData, s=Student): #adds classData object to class array inside student
    c.grade = grade
    s.classes.append(c)


grade = float(input("Enter your grade: ")) #testing input for grade

addClass(grade, myClass_01, myStudent_01)

def printClass(s=Student): #Placeholder to show class information
    print("Name: " + s.classes[0].name)
    print("Category: " + s.classes[0].category)
    print("Credits: " + str(s.classes[0].credits))
    print("Prerequisite/s: " + s.classes[0].prereq)
    print("Corequisite/s: " + s.classes[0].coreq)
    print("Grade: " + str(s.classes[0].grade))

printClass(myStudent_01)
print("Programming Avg: " + str(myStudent_01.getAvg("Programming"))) #TEST CASE
myClass_02 = classData('MAC1105', 'Math', 3, '', '')
myClass_03 = classData('MAC2312', 'Math', 3, '', '')
myClass_04 = classData('MAC2313', 'Math', 3, '', '')

addClass(4.0, myClass_02, myStudent_01)
addClass(3.0, myClass_03, myStudent_01)
addClass(3.0, myClass_04, myStudent_01)
print("Math Avg: " + str(myStudent_01.getAvg("Math")))