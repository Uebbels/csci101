#Brendan Uebelhoer
#CSCI 102 Section C
#Week 8 Part B

s = ''
t = ''
locations = []

s = input('Please input the full DNA string, s:\nS>')
t = input('Please input the substring t:\nT>')

for i in range(len(s)):
    if s[i:i + len(t)] == t:
        locations.append(i+1)

print('OUTPUT',*locations)