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
import difflib

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
c = 0
for row in cursor.execute("SELECT courses, credits, prereqs, coreqs, category from courses"):
    #print("Course = ", row[0], "Credits = ", row[1], "Prereqs = ", row[2], "Coreqs = ", row[3])
    classList.append(classData(row[0], row[4], row[1], [row[2]], row[3]))
    c += 1
conn.commit()
conn.close()
print("FIND ME: " + str(c))


def splitAnd(arr):
    andLocator = arr.find('AND')
    if andLocator == -1:
        return arr
    else:
        test = arr.replace("(", "").replace(")", "").split(" AND ")
        return test

def splitOr(arr):
    orLocator = arr.find('OR')
    if orLocator == -1:
        return arr
    else:
        test = arr.replace("(", "").replace(")", "").split(" OR ")
        return test

tempPrereqArr = []
def splitOrAnd(arr):
    if arr == None:
        return arr
    andLocator = arr.find('AND')
    orLocator = arr.find('OR')
    if andLocator != -1 and orLocator != -1:
        temp = splitAnd(arr)
        for i in temp:
            temp = splitOr(i)
            tempPrereqArr.append(temp)
        return tempPrereqArr
    elif andLocator != -1 and orLocator == -1:
        test = arr.replace("(", "").replace(")", "").split(" AND ")
        return test
    elif orLocator != -1 and andLocator == -1:
        test = arr.replace("(", "").replace(")", "").split(" OR ")
        return test
    else:
        return arr



classList.pop(0)
counter = 0
for i in classList:
    tempPrereqArr = []
    i.prereq = splitOrAnd(i.prereq[0])
    counter += 1

counter = 0
for i in classList:
    print(str(counter) + ". " + str(i.name) + " "  + str(i.prereq))

    counter += 1

print("Prereqs: " + str(tempPrereqArr))

grade = 4.0 #testing input for grade

addClass(grade, myClass_01, myStudent_01)

def printClass(s=Student): #Placeholder to show class information
    print("Name: " + s.classes[0].name)
    print("Category: " + s.classes[0].category)
    print("Credits: " + str(s.classes[0].credits))
    print("Prerequisite/s: " + s.classes[0].prereq)
    print("Corequisite/s: " + s.classes[0].coreq)
    print("Grade: " + str(s.classes[0].grade))

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

pathToCourse(classList[2])
print(classList[2].name)
print("prereqlist")
for i in range(len(prereqList)):
    print(prereqList[i].name)


def clearPrereqList():
    global prereqList
    prereqList = []

nextClasses = [] #Temporary array for classes that open up after taking a certain class
nextClassesCounter = 0

firstRun = True #Boolean for nextSteps

def nextClass(_classCheck, _classInput, _next_class):
    if len(_classInput) == 0:
        nextClasses.append(_next_class)
    else:
        for j in _classInput:
            if (j.name[:3] + j.name[4:]) == (_classCheck[:3] + _classCheck[4:]):
                continue
            else:
                nextClasses.append(_next_class)
                print("Next class", _classInput[0])
                print("BREAK")
                break

def nextSteps(c=classData): #Recursive function that adds next classes to an array
    checkClass = c.name
    c = 0
    for i in classList:
        c += 1
        if isinstance(i.prereq, list):
            for j in i.prereq:
                if isinstance(j, list):
                    for m in j:
                        if (m[:3] + m[4:]) == (checkClass[:3] + checkClass[4:]):
                            nextClass(checkClass, nextClasses, i)
                        else:
                            continue
                else:
                    temp1 =  j[:3] + j[4:]
                    temp2 = checkClass[:3] + checkClass[4:]

                    if temp1 == temp2:
                        nextClass(checkClass, nextClasses, i)
                    else:
                        continue
        elif i.prereq == checkClass:
            next_class = i

            global nextClassesCounter
            nextClassesCounter += 1
            global firstRun
            if firstRun == False:
                #nextClass(checkClass, nextClasses, next_class)
                for j in nextClasses:
                    if (j.name[:3] + j.name[4:]) == (checkClass[:3] + checkClass[4:]):
                        continue
                    else:
                        nextClasses.append(next_class)
                        break
            else:
                nextClasses.append(next_class)
            firstRun = True
            print("NEXT CASE:", next_class.name)
            nextSteps(next_class)

def clearNextClassesList():
    global nextClasses
    nextClasses = []

print("TEST CASE: " + str(classList[46].name))
nextSteps(classList[46])

count = 0
while count < len(nextClasses):
    print(nextClasses[count].name)
    count += 1