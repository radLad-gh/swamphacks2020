"""
Main student file - contains class Object constructors for classData and Student
Available functions:
    getAvg
    addClass
    hasPrereq
    hasCoreq
    pathToCourse
    clearPrereqList
    nextSteps
    clearNextClassesList
"""
import sqlite3

class classData(object): #Constructor for classes
    def __init__(self, name, category, credits, prereq, coreq):
        self.name = name
        self.category = category
        self.credits = credits
        self.prereq = prereq
        self.coreq = coreq
        self.grade = 0
        self.difficulty = None
        self.curRank = 0

myClass_01 = classData('COP3502', 'Programming', 3, 'MAC2311', '')
print(myClass_01.name)
myClass_01.grade = 3.0

class Student: #Constructor for class, gpa dictionary is current placeholder
    def __init__(self, name):
        self.name = name
        self.semestersLeft = None

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

classList = []

conn = sqlite3.connect('userDatabase.sqlite')
cursor = conn.cursor()
print("Opened database successfully")
for row in cursor.execute("SELECT courses, credits, prereqs, coreqs from courses"):
    print("Course = ", row[0], "Credits = ", row[1], "Prereqs = ", row[2], "Coreqs = ", row[3])
    classList.append(classData(row[0], 'Programming', row[1], [row[2]], row[3]))
conn.commit()
conn.close()

grade = 4.0 #testing input for grade

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
myClass_03 = classData('MAC2312', 'Math', 3, 'MAC1105', '')
myClass_04 = classData('MAC2313', 'Math', 3, 'MAC2312', '')

addClass(4.0, myClass_02, myStudent_01)
addClass(3.0, myClass_03, myStudent_01)
addClass(3.0, myClass_04, myStudent_01)
print("Math Avg: " + str(myStudent_01.getAvg("Math")))

def hasPrereq(c=classData):
    if c.prereq == '':
        return False
    else:
        return True

def hasCoreq(c=classData):
    if c.coreq == '':
        return False
    else:
        return True

prereqList = [] #List for prereq classes

def pathToCourse(c=classData): #Recursive function that finds all prerequisites for higher level class
    if c.prereq == '':
        return False
    else:
        prereqClass = c.prereq
        for i in classList:
            if i.name == prereqClass:
                prereqList.append(i)
                pathToCourse(i)
            else:
                continue
pathToCourse(classList[47])
print("prereqlist")
for i in range(len(prereqList)):
    print(prereqList[i].name)

def clearPrereqList():
    global prereqList
    prereqList = []

nextClasses = [] #Temporary array for classes that open up after taking a certain class
nextClassesCounter = 0
firstRun = True #Boolean for nextSteps
def nextSteps(c=classData): #Recursive function that adds next classes to an array
    checkClass = c.name
    for i in classList:
        if i.prereq == checkClass:
            next_class = i
            global nextClassesCounter
            nextClassesCounter += 1
            if firstRun == False:
                for j in nextClasses:
                    if j.name == checkClass:
                        continue
                    else:
                        nextClasses.append(next_class)
                        break
            else:
                nextClasses.append(next_class)
            nextSteps(next_class)

def clearNextClassesList():
    global nextClasses
    nextClasses = []

print("Class 46: " + classList[53].name + " with prereq's: "+ classList[53].prereq[0])
nextSteps(classList[53])
print(nextClassesCounter)

for i in range(len(nextClasses)):
    print(nextClasses[i].name)

