# Brendan Uebelhoer
# ​CSCI 101 – Section A
# Python Lab 10
import csv

def get_gdp_data(fileName, year):
    gdp = []
    with open(fileName, 'r') as gdpfile:
        gdpcontents =  gdpfile.readlines()
    for i in gdpcontents:
        if i[0:4] == str(year):
            yeardata = i.split()
            gdp.append(yeardata[1])
    return gdp

def get_unemp_data(fileName, year):
    unemp = []
    with open(fileName, 'r') as csvfile:
        grades_reader = csv.reader(csvfile)
        for i in grades_reader:
            if i[0] == str(year):
                unemp = i[1:]
    return unemp

yearvalid = False

#GDPfilename = input('Enter the GDP file name:\nGDP>')
#UEfilename = input('Enter the unemployment file name:\nUNEMPLOYMENT>')

print('REMOVE ME    !')
GDPfilename = 'gdp.txt'
UEfilename = 'unemp.csv'

while yearvalid == False:
    year = int(input('Enter year to examine:\nYEAR>'))
    if (1948 <= year <= 2018):
        yearvalid = True
    else:
        print('invalid year, please try again')

print(get_gdp_data(GDPfilename,year))
print(get_unemp_data(UEfilename, year))

