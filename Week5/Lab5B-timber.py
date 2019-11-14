#Brendan Uebelhoer
#CSCI 101 Section B
#Python Lab 5B

print('enter the number of years for the table:')
years = int(input('YEARS>'))

acres = [0] * (years + 1)
percent = [0] * (years + 1)
done = False
num3 = 0

for num in range(years + 1):
    #print(num,num-1)

    if num == 0:
        acres[0] = 2500
    else:
        acres[num] = acres[num - 1] * 1.02
    percent[num] = round((acres[num] / 14000)*100,2)
    acres[num] = round(acres[num],2)

    #print(num, acres, percent)

print('\nYour table is printed below')
print('OUTPUT    YEAR    # Acres in Forest    % of forest')

for num in range(years+1):
    print('OUTPUT    %d       %.1f               %.2f' % (num, acres[num], percent[num]))

print('OUTPUT 87')

#while done == False:
    #print(num3)
    #final_acres = [2500]
    #final_percent = [17.86]
    #final_acres.append(acres[num3 - 1] * 1.02)
    #final_percent.insert((acres[num3 - 1] / 14000)*100,-1)
    #print(final_percent)

    #if final_percent[num3 - 1] >= 100:
        #done = True
    #else:
        #num3 += 1
    
#print(num3)
