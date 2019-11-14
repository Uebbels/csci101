#Brendan Uebelhoer
#CSCI 1p2 Scotion C
#Week 9 Part B

import csv
studentpresent = False
studentaverage = 0.0
studentmax = 0.0
studentmin = 100.0
grades = 0

filename = input('Please enter the CSV file name with student grades:\nFILE>')
studentname = input('Please enter the name of the student to calculate grades:\nSTUDENT>')

with open(filename, 'r') as csvfile:
    grade_file = csv.reader(csvfile)
    
    for row in grade_file:
        if row[0] == studentname:
            first = True
            studentpresent = True
            for i in row:
                if first:
                    first = False
                    continue
                grade = float(i)
                studentaverage += grade
                if grade > studentmax:
                    studentmax = grade
                if grade < studentmin:
                    studentmin = grade
            gradecount = len(row) - 1
            studentaverage /= gradecount

if studentpresent:
    with open('output.csv','x') as outfile:
        gradewriter = csv.writer(outfile)
        gradewriter.writerow([studentname,studentaverage,studentmax,studentmin])
        
    print('The average grade for %s is: %d\nOUTPUT %d' % (studentname,studentaverage,studentaverage))
    print('The maximum grade for %s is: %d\nOUTPUT %d' % (studentname,studentmax,studentmax))
    print('The minimum grade for %s is: %d\nOUTPUT %d' % (studentname,studentmin,studentmin))
else:
    print('Student not found. No output file created\nOUTPUT error')