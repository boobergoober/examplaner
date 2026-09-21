import random

print("helloword")

examslist = []
listing = True

textOrManual = input("text file or manual?")

if textOrManual == "text":
    f = open("examdates.txt", "r")
    for line in f:
        examslist.append(line.strip("\n"))
    f.close()

elif textOrManual == "birthday":
    print("happy birthday!!!! wish you all the best also in the years to come!!!!")

else:

    print("""
    you must enter your exams as such:
    :[day], [exam], [the difficulty you give the exam], [date]

    when you are done, type:
    :q    """)

    while listing == True:
        exam = input("\n:")
        if exam == "c" or exam == "stop" or exam == "q":
            listing = False
            break
        examslist.append(exam)

for examNum in range(len(examslist)):
    exam = examslist[examNum]
    info = exam.split(", ")
    examslist[examNum] = info

week = [[0,0],[0,0],[0,0],[0,0],[0,0]]
days = ["monday", "tuesday", "wednesday", "thursday", "friday"]

for exam in examslist:
    day = exam[0]
    topic = exam[1]
    difficulty = int(exam[2])
    date = exam[3]

    if day == "monday":
        monday = week[0]
        monday[0] += 1
        monday[1] += difficulty
    elif day == "tuesday":
        tuesday = week[1]
        tuesday[0] += 1
        tuesday[1] += difficulty
    elif day == "wednesday":
        wednesday = week[2]
        wednesday[0] += 1
        wednesday[1] += difficulty
    elif day == "thursday":
        thursday = week[3]
        thursday[0] += 1
        thursday[1] += difficulty
    elif day == "friday":
        friday = week[4]
        friday[0] += 1
        friday[1] += difficulty

print("   -")

for day in range(5):
    if week[day][0] == 0:
        week[day][0] = 1

for dayNum in range(5):
    daySpelled = days[dayNum]
    difficultyScore = week[dayNum][1] / week[dayNum][0]
    amountOfExams = week[dayNum][0]
    print(f"{daySpelled} has the difficulty score of {difficultyScore} / 10 with {amountOfExams} exams \n   -")

if textOrManual == "manual":
    saveYn = input("do you wish to save your exam schedule as a file Y/n \n:")
    if saveYn == "n":
        exit
    fileName = f"myExamSchedule{random.randint(0, 31)}"
    f = open(fileName, "w")

    for exam in examslist:
        currentLine = ""
        for info in exam:
            currentLine = currentLine + info + ", "
        currentLine = currentLine[:-2] + "\n"
        f.write(currentLine)

    print(f"\n you can find your file under the file name {fileName} in the folder where you installed this program")
    print("we advise you rename or move the file! (it might get destroyed if you use this program again)")
    print("hope this was helpful :)")