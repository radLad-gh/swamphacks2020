import student


def makeSchedule(s=student.Student):
    print(
        "Rank the following 1-3, with 3 being most important to you: Course Difficulty, Past Success in Subject, "
        "Taking PreReqs for Other Courses -\n")

    coursePriorityIndex = int(input("Course Difficulty: "))
    pastSuccessIndex = int(input("Past Success in Subject: "))
    bottleneckIndex = int(input("PreReqs for Other Courses: "))

    print("\nWhat credit range do would you like for your semester? ")

    creditNumLow = int(input("Lower end: "))
    creditNumHigh = int(input("Upper end: "))

    semesterDifficulty = 0.0
    curCreditNum = 0

    courseList = []
    # CourseList is a list of courses which the student must take to graduate AND is eligible to take

    for c in courseList:
        courseRanking = coursePriorityIndex * c.difficulty + pastSuccessIndex * s.getAvg(c.category) + bottleneckIndex
            # * number of classes in CourseList this course is a prereq for
        c.curRank = courseRanking

    courseList.sort(key=lambda x: x.curRank, reverse=True)

    i = 0
    schedule = []

    while curCreditNum < creditNumHigh and i < len(courseList):
        if curCreditNum + courseList[i].credits > creditNumHigh:
            i += 1
            continue
        else:
            schedule.append(courseList[i])
            curCreditNum += courseList[i].credits
            updateCourseRanking(courseList[i], courseList)
            i += 1
    return schedule

makeSchedule(student.myStudent_01)

def updateCourseRanking(course, courseList):
    for c in courseList:
        if course.category == c.category:
            c.curRank -= course.difficulty
