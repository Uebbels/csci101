# Brendan Uebelhoer
# CSCI 102 Section C
# Week 1 Part C
print('How tall are you, in inches?')
heightin = int(input('HEIGHT>'))
print('How much do you weight, in pounds?')
weightlb = int(input('WEIGHT>'))
heightm = heightin * 0.0254
#print(heightm)
weightkg = weightlb * 0.454
#print(weightkg)
bmi = weightkg / heightm**2
print('Your BMI is')
print('OUTPUT' , bmi)
