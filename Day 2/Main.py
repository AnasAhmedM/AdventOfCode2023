import re
rgb = {'r': 12, 'g': 13, 'b': 14}

def PartOne():
    with open("games_played.txt", 'r') as gameValues:
        total = 0
        game = 0
        for line in gameValues:
            game += 1
            win = 1
            for item in re.findall(r'( [0-9]+ [rbg])', line):
                numberAndColor = item.lstrip().split(' ')
                if rgb[numberAndColor[1]] < int(numberAndColor[0]):
                    win = 0
                    break
            if win:
                total += game
        print(total)

def PartTwo():
    with open("games_played.txt", 'r') as gameValues:
        total = 0
        for line in gameValues:
            colorValues = {'r': 0, 'g': 0, 'b': 0}
            for item in re.findall(r'( [0-9]+ [r])', line):
                number = item.lstrip().split(' ')[0]
                if colorValues['r'] < int(number):
                    colorValues['r'] = int(number)
            for item in re.findall(r'( [0-9]+ [g])', line):
                number = item.lstrip().split(' ')[0]
                if colorValues['g'] < int(number):
                    colorValues['g'] = int(number)
            for item in re.findall(r'( [0-9]+ [b])', line):
                number = item.lstrip().split(' ')[0]
                if colorValues['b'] < int(number):
                    colorValues['b'] = int(number)
            total += colorValues['r'] * colorValues['g'] * colorValues['b']   
        print(total)

PartOne()
PartTwo()