#################################################
######## YOUR NAME HERE                 #########
######## Lab 10B - Function Definitions #########
######## Section - YOUR SECTION HERE    #########
#################################################
        
# Imports
import math
from math import pi

################################################
########   Function 1 : PrintOutput    #########
################################################

def PrintOutput(input):
    output = 'OUTPUT ' + str(input)
    print(output)

################################################
########   Function 2 : TriangleArea   #########
################################################

def TriangleArea(h,w):
    a = h*w*.5
    PrintOutput(a)

################################################
########   Function 3 : FeetToMeters   #########
################################################

def FeetToMeters(l):
    PrintOutput(l * 0.3048)

################################################
########   Function 4 : PolarCoords    #########
################################################

def PolarCoords(x,y):
    r = math.sqrt(x**2 + y**2)
    theta = math.atan(y / x) * (180/pi)
    PrintOutput('%.1f' %r)
    PrintOutput('%.1f' % theta)

################################################
########   Function 5 : EurosToDollars #########
################################################

def EurosToDollars(eamount):
    damount = round(eamount * 1.12, 2)
    PrintOutput('%.2f' %damount)
    