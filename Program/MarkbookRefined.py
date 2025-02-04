import os, time, threading, os.path
from tabulate import tabulate
#threading work to make the exit check run in the background
exitList = []
exitCheck = False
global postLoop
postLoop = False
markbook = []
global loopcounter
loopcounter = 0
#exits the program
def backgroundLoop():
    while exitCheck != True:
        for i in exitList:
            if i == 'exit':
                exitMessage = 'Exiting system'
                reps = 2
                loadingLoop(exitMessage, reps)
                clearOutput()
                print("Done")
                os._exit(0)
backthread = threading.Thread(name='backgroundLoop', target=backgroundLoop)
backthread.start()
def clearOutput():
    os.system('cls')
clearOutput()
def loadingLoop(message, reps):
    for i in range (reps):
        clearOutput()
        result = ' '.join([message, '.'])
        print(result)
        time.sleep(0.25)
        clearOutput()
        result = ' '.join([message, '..'])
        print(result)
        time.sleep(0.25)
        clearOutput()
        result = ' '.join([message, '...'])
        print(result)
        time.sleep(0.25)
def validID (ID):
    if len(str(ID)) != 5:
        #clearOutput()
        if len(str(ID)) > 5:
            clearOutput()
            print("--Invalid Student ID (> 5 digits)--")
            #errorHandle1(Fname, Lname)
            return False
        elif len(str(ID)) < 5:
            clearOutput()
            print("--Invalid Student ID (< 5 digits)--")
            #errorHandle1(Fname, Lname)
            return False
    else:
        return True
#handels one of the errors
def errorHandle1(x, y):
    print(f'Enter student id: {x}')
    print(f'Enter first name: {y}')
#checks if a name is alphabetical
def nameCheck(name):
    if name.isalpha():
        return True
def listToString(s):
 
    str1 = " "
 
    return (str1.join(s))       
def loadMarkbook():
    print("TYOPE EXIT INTO ANY INPUT WHEN YOU WISH TO LEAve")
    while True:
        loadOrStart = input("load a pre-esiting markbook or start a new one ('load' or 'new')? ").lower(); exitList.append(str(loadOrStart.lower()))
        if loadOrStart.isalpha() == False:
            clearOutput()
            print("---Incorrect input('load' or 'new')")
        elif loadOrStart == 'new':
            clearOutput()
            addStudent()
        elif loadOrStart == 'load':
            while True:
                markbookName = input("whats the name of the file: "); exitList.append(str(markbookName.lower()))
                markbookName = markbookName + '.txt'
                path = str(markbookName)
                if os.path.exists(path) == True:
                    displaymarkbook(path)
                else:
                    clearOutput()
                    print("invalid File name")
        else:
            clearOutput()
            print("---Incorrect input('load' or 'new')---")

def displaymarkbook(path):
    head = ["Student Number", "First name", "Last name", "grade"]
    with open(path, "r+") as StudentDB:
        while True:
            line = StudentDB.readlines()
            if not line:
                break
            #line = line[:-2]
            line2 = listToString(line)
            mydata = [line2.split()]
            print(tabulate(mydata, headers=head, tablefmt="grid"))
            loadMarkbook()

def addStudent():
    while True:
        studentID = input("Enter student id: "); exitList.append(str(studentID.lower()))
        x=-1
        #post loop only lets the rest occur after the first student is inputed
        if postLoop == True:
            for i in markbook:
                x+=1
                if i[x][:5] == studentID:
                    clearOutput()
                    print("--Student ID already in data base(student ID must be unique)--")
                    addStudent()
                        #addMarks(studentID)
        if studentID.isdigit() == True:
            int(studentID)
            if validID(studentID) == True:
                break
        else:
            clearOutput()
            print("--Invalid student ID Input (Must be Numerical)--")
            #errorHandle1(Fname, Lname)
    while True:
        Fname = input("Enter first name: ").lower(); exitList.append(Fname.lower())
        if nameCheck(Fname) != True:
            clearOutput()
            print("--Incorrect first name (Alphabetical only)--")
            errorHandle1(studentID, ' ')
            print ("\033[A                             \033[A")
        elif nameCheck(Fname) != False:
            break
    while True:
        Lname = input("Enter last name: ").lower(); exitList.append(Lname.lower())
        if nameCheck(Lname) != True:
            clearOutput()
            print("--Incorrect last name (Alphabetical only)--")
            errorHandle1(studentID, Fname)
        elif nameCheck(Lname) != False:
            markbook.append([studentID, Fname, Lname])
            addMarks(studentID)
            print(f'{studentID}, {Fname}, {Lname}')
        

            
def addMarks(studentID):
    clearOutput()
    print("--add marks--")
    print(markbook)
    print(studentID)
    while True:
        Mark = input("Enter marks (0-100): "); exitList.append(str(Mark.lower()))
        if Mark.isdigit() == True and int(Mark) > -1 and int(Mark) < 101:
            calculateGrade(studentID, Mark)
        else:
            clearOutput()
            print('--Invalid Mark (0-100)')


def calculateGrade(studentID, mark):
    grade = 'N/A'
    match mark:
        case mark if int(mark) > 89:
            grade = 'A'
        case mark if int(mark) > 73:
            grade = 'B'
        case mark if int(mark) > 59:
            grade = 'C'
        case mark if int(mark) > 49:
            grade = 'D'
        case mark if int(mark) > -1:
            grade = 'F'
    print(f'calculated grade {grade}')
    global postLoop
    postLoop = True
    global loopcounter
    markbook[loopcounter].append(grade)
    loopcounter += 1
    while True:
        Finish = input("have you finished marking (y/n): ").lower(); exitList.append(str(Finish.lower()))
        if Finish == 'y':
            saveMarkbook()
        elif Finish == 'n':
            clearOutput()
            addStudent()
        clearOutput()
        print("---Invalid answer (y or n)---")
def saveMarkbook():
    clearOutput()
    print("---save markbook---")
    while True:
        markbookName = input("What would you like the name this markbook (nospaces or chacarcters): "); exitList.append(str(markbookName.lower()))
        if markbookName.isalpha() == False:
            clearOutput()
            print("---Inncorect file name(alphabetical characters)---")
        else:
            break
    markbookName = str(markbookName) + '.txt'
    x=-1
    for i in markbook:
        x+=1
        markbookComp = ' '.join(markbook[x])
        markbookComp = markbookComp + '\n'
        print(markbookComp)
        with open(markbookName, "a") as file:
            file.write(markbookComp)
    loadMarkbook()

        
forethread = threading.Thread(name='foregroundStarter', target=loadMarkbook())
forethread.start()
