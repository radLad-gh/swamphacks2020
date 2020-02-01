class classData:
    def __init__(self, name, category, credits, prereq, coreq):
        self.name = name
        self.category = category
        self.credits = credits
        self.prereq = prereq
        self.coreq = coreq

myClass_01 = classData('COP3502', 'Programming', 3, 'MAC2311', '')
print(myClass_01.name)

class Student:
    def __init__(self, name):
        self.name = name
        self.gpa = {
            'Math': 4.0,
            'English': 3.999999999
        }
        self.classes = [
            ["Programming", 'COP3502', 3.5],
            ["Math", 'MAS3114', 3.0],
            ["Math", 'MAC1105', 4.0],
        ]

    def getAvg(self, category):
        total = 0
        counter = 0
        for x in self.classes:
            if x[0] == category:
                total += x[2]
                counter += 1
        if counter == 0:
            return 0
        return total/counter

myStudent_01 = Student('Masen')
print(myStudent_01.name)
print(list(myStudent_01.gpa.values())[1])
print(myStudent_01.getAvg('Math'))
print(myStudent_01.gpa['Math'])

def addClass(grade, c=classData, s=Student):
    s.classes.append([c.category, c.name, grade])


grade = float(input("Enter your grade: "))

addClass(grade, myClass_01, myStudent_01)
print(myStudent_01.classes)