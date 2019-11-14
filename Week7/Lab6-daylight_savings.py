#Brendan Uebelhoer
#CSCI 101 Section A
#Python lab 6

def parse(string,elem):
    str = ['*'] * len(string)
    elem = int(elem)
    counter = 0
    for i in string:
        if i != ' ':
            if str[counter] == '*':
                str[counter] = i
            else:
                str[counter] += i
        else:
            counter += 1
    return str[elem]

iterations = 0
iterations = int(input('N>'))

for i in range(iterations):
    direction = ' '
    offset = 0
    hours = 0
    minutes = 0
    abs_time = 0
    final_hours = 0
    final_minutes = 0 
    
    inp = input('INPUT>')
    
    direction = parse(inp,0)
    offset = int(parse(inp, 1))
    hours = int(parse(inp,2))
    minutes = int(parse(inp,3))
    
    '''
    print(direction)
    print(offset)
    print(hours)
    print(minutes)
    '''
    
    if direction == 'B':
        offset *= -1
    
    abs_time = (hours * 60) + minutes
    abs_time += offset
    
    if abs_time >= 1440:
        abs_time -= 1440
    
    if abs_time < 0:
        abs_time += 1440
    
    final_hours = abs_time // 60
    final_minutes = abs_time % 60
    
    print('OUTPUT', final_hours, final_minutes)