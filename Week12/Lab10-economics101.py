# Brendan Uebelhoer
# ​CSCI 101 – Section A
# Python Lab 10

def get_gdp_data(fileName, year):
    gdp = []
    with open(fileName, 'r') as gdpfile:
        gdpcontents =  gdpfile.readlines()
    for i in gdpcontents:
        #print(i[0:4], year)
        if i[0:4] == str(year):
            yeardata = i.split()
            gdp.append(yeardata[1])
    return gdp

def get_unemp_data(fileName, year):
    unemp = []
    

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


