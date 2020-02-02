from .student import Student
from .student import classData

def makeSchedule(s=Student):
    choice = input("Would you like to create a schedule for you with default settings or would you like to input "
                       "custom settings? ")

    if choice == "manual":

        print(
            "Rank the following 3 options on a 1-5 scale, with 1 being 'I strongly disagree' and 5 being 'I strongly "
            "agree': 'I would like to take a rigorous courseload'; 'I would like to take courses in subjects I "
            "have had success with in the past'; 'I would like to take courses that are prerequisites for many other "
            "courses' -\n")

        coursePriorityIndex = int(input("'I would like to take a rigorous courseload': "))
        pastSuccessIndex = int(input("'I would like to take courses in subjects I have had success with in the past': "))
        bottleneckIndex = int(input("'I would like to take courses that are prerequisites for many other courses': "))

    elif choice == "default":
        totalCreditsTaken = 0
        for c in s.classes:
            totalCreditsTaken += c.credits
        if totalCreditsTaken <= 30:
            coursePriorityIndex = 2
            pastSuccessIndex = 1
            bottleneckIndex = 5
        elif totalCreditsTaken <= 60:
            coursePriorityIndex = 3
            pastSuccessIndex = 3
            bottleneckIndex = 4
        elif totalCreditsTaken <= 90:
            coursePriorityIndex = 5
            pastSuccessIndex = 4
            bottleneckIndex = 3
        else:
            coursePriorityIndex = 4
            pastSuccessIndex = 5
            bottleneckIndex = 2


    creditNumHigh = int(input("\nWhat is the maximum number of credits you would like to take your next semester? "))

    curCreditNum = 0

    genEdBio = ["AST 1002", "AST 3108", "AST 3019", "BOT 2011C", "BSC 2005", "BSC 2010", "CHM 1020", "CHM 2045",
                "CHM 2046", "CHM 2051", "CHM 2096", "ESC 1000", "EVR 2001", "PHY 2020", "PHY 2048", "PHY 2049",
                "PHY 2053", "PHY 2054"]
    genEdComp = ["ENC 1101" , "ENC 1102", "ENC 2210", "ENC 2305", "ENC 3246", "ENC 3254", "ENC 3453", "ENC 3459",
                 "ENC 3464", "ENC 3465"]
    genEdMath = ["MAC 1105", "MAC 1140", "MAC 1147", "MAC 2233", "MAC 2311", "MAC 2312", "MGF 1106", "MGF 1107",
                 "STA 2023"]
    genEdHum = ["ARH 200", "LIT 2000", "MUL 2010", "PHI 2010", "THE 2000"]
    genEdSoc = ["AMH 2020", "ANT 2000", "ECO 2013", "POS 2041", "PSY 2012", "SYG 2000"]
    compSciMain = ["CEN 3031", "COT 3100", "COP 3530", "CIS 4301", "CEN 3031", "CDA 3101", "COT 4501", "COP 3502",
                   "COP 3503", "COP 4600", "EEL 3701C", "CNT 4007C"]
    compSciElec = ["CAP 4053", "COT 5405", "CAP 5510", "CEN 4914", "CNT 5410", "CDA 4102", "CDA 5155",
                   "CAP 5705", "CNT 5106C", "COP 5416", "CIS 4930", "CNT 6885", "CDA 5636", "CDA 4630", "CIS 6930",
                   "CAP 5100", "CEN 4721", "CIS 5371", "CAP 5771", "CAP 4770", "CAP 6610", "CAP 6516", "CIS 6930",
                   "CIS 6930", "COP 5556", "CIS 4914", "CEN 5035", "CIS 4930", "CEN 4722"]
    preReqClasses = ["CHM 2045", "CHM 2046", "PHY 2048", "PHY 2049", "MAC 2311", "MAC 2312"]

    genEdBioBool, genEdCompBool, genEdHumBool, genEdMathBool, genEdSocBool = False
    coursesTaken = []
    # list of all courses student has taken

    courseEligibility = []
    # list of all courses student is eligible to take

    elecNum = 0
    for c in coursesTaken:
        if genEdBioBool == False:
            for g in genEdBio:
                if c.name == g:
                    genEdBioBool == True
                    break
        if genEdCompBool == False:
            for g in genEdComp:
                if c.name == g:
                    genEdCompBool == True
                    break
        if genEdMathBool == False:
            for g in genEdMath:
                if c.name == g:
                    genEdMathBool == True
                    break
        if genEdHumBool == False:
            for g in genEdHum:
                if c.name == g:
                    genEdHumBool == True
                    break
        if genEdSocBool == False:
            for g in genEdSoc:
                if c.name == g:
                    genEdSocBool == True
                    break
        if elecNum < 5:
            for g in compSciElec:
                if c.name == g:
                    elecNum += 1

    for c in courseEligibility:
        if genEdBioBool == True:
            for g in genEdBio:
                if c.name == g:
                    check = False
                    for g in preReqClasses:
                        if c.name == g:
                            check = True
                    if check == False:
                        courseEligibility.remove(c)
        if genEdCompBool == True:
            for g in genEdComp:
                if c.name == g:
                    check = False
                    for g in preReqClasses:
                        if c.name == g:
                            check = True
                    if check == False:
                        courseEligibility.remove(c)
        if genEdMathBool == True:
            for g in genEdMath:
                if c.name == g:
                    check = False
                    for g in preReqClasses:
                        if c.name == g:
                            check = True
                    if check == False:
                        courseEligibility.remove(c)
        if genEdHumBool == True:
            for g in genEdHum:
                if c.name == g:
                    check = False
                    for g in preReqClasses:
                        if c.name == g:
                            check = True
                    if check == False:
                        courseEligibility.remove(c)
        if genEdSocBool == True:
            for g in genEdSoc:
                if c.name == g:
                    check = False
                    for g in preReqClasses:
                        if c.name == g:
                            check = True
                    if check == False:
                        courseEligibility.remove(c)
        if elecNum >= 5:
            for g in compSciElec:
                if c.name == g:
                    courseEligibility.remove(c)

    courseList = courseEligibility

    # CourseList is a list of courses which the student must take to graduate AND is eligible to take


    for c in courseList:
        courseRanking = coursePriorityIndex * c.difficulty + pastSuccessIndex * s.getAvg(c.category) + bottleneckIndex
        # * number of classes in CourseList this course is a prereq for
        c.curRank = courseRanking

    courseList.sort(key=lambda x: x.curRank, reverse=True)

    i = 0
    schedule = []

    while curCreditNum < creditNumHigh and i < len(courseList):
        if curCreditNum == creditNumHigh:
            break
        elif curCreditNum + courseList[i].credits > creditNumHigh:
            i += 1
            continue
        else:
            schedule.append(courseList[i])
            curCreditNum += courseList[i].credits
            course = courseList[i].pop
            updateCourseRanking(course, courseList)
    for c in schedule:
        c.curRank = 0
    for c in courseList:
        c.curRank = 0
    return schedule


def updateCourseRanking(course, courseList):
    for c in courseList:
        if course.category == c.category:
            c.curRank -= course.difficulty
        if course.difficulty > c.difficulty:
            c.curRank -= 2 * (c.difficulty - course.difficulty)
    courseList.sort(key=lambda x: x.curRank, reverse=True)

def removeClass(schedule, courseList):
    print("Current Schedule:")
    for c in schedule:
        print(c.name)
    choice = input("What class would you like to remove? (in format XXX ####")
    for c in schedule:
        if choice == c.name:
            courseList.append(c)
            schedule.remove(c)
            break
    print("New Schedule:")
    for c in schedule:
        print(c.name)

def addClass(schedule, courseList):
    print("Current Schedule:")
    for c in schedule:
        print(c.name)
    choice = input("What class would you like to add? (in format XXX ####")
    for c in courseList:
        if choice == c.name:
            schedule.append(c)
            courseList.remove(c)
            break
    print("New Schedule:")
    for c in schedule:
        print(c.name)

def changeSchedule(schedule, courseList):
    print("Current Schedule:")
    for c in schedule:
        print(c.name)
    choice = input("What class would you like to replace? (in format XXX ####")
    for c in schedule:
        if choice == c.name:
            courseList.append(c)
            schedule.remove(c)
            break
    choice2 = input("What class would you like to add? (in format XXX ####")
    for c in courseList:
        if choice2 == c.name:
            schedule.append(c)
            courseList.remove(c)
            break
    print("New Schedule:")
    for c in schedule:
        print(c.name)
