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
            for item in re.findall(r'( [0-9]+ [rbg])', line):
                nc = item.lstrip().split(' ')
                number = nc[0]
                color = nc[1].strip()
                if colorValues[color] < int(number):
                    colorValues[color] = int(number)
            total += colorValues['r'] * colorValues['g'] * colorValues['b']   
        print(total)

PartOne()
PartTwo()