#Brendan Uebelhoer
#CSCI 101-Section A
#Python Lab 2B
dollars = 0.0
conversion_rate = 0.0
item_cost = 0.0
currency = 'EUR'
print('Input Currency:')
currency = input('CURRENCY>')
#print(currency)
print('Input conversion:')
conversion_rate = int(input('RATE>'))
#print(conversion_rate)
print('input item cost:')
item_cost = int(input('COST>'))
#print(item_cost)
dollars = conversion_rate * item_cost
#print(dollars)
dollars = str(dollars)
output = '$' + dollars
print('your item is worth', output, 'dollars')
print('OUTPUT', output)
