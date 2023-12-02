d = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def PartOne():
    with open("calibration_document.txt", 'r') as calValues:
        total = 0
        for line in calValues:
            first, last = '', ''
            for char in line:
                if not char.isdigit():
                    continue
                
                if first == '':
                    first = char
                last = char

            total += int(first + last)

        print(total)

def PartTwo():
    with open("calibration_document.txt", 'r') as calValues:
        total = 0
        for line in calValues:
            first, last = '', ''
            index = 0
            maximum = len(line)
            while index < maximum:
                if line[index].isdigit():
                    if first == '':
                        first = line[index]
                    last = line[index]
                else:
                    if line[index:index+3] in d:
                        if first == '':
                            first = d[line[index:index+3]]
                        last = d[line[index:index+3]]
                    elif line[index:index+4] in d:
                        if first == '':
                            first = d[line[index:index+4]]
                        last = d[line[index:index+4]]
                    elif line[index:index+5] in d:
                        if first == '':
                            first = d[line[index:index+5]]
                        last = d[line[index:index+5]]
                index += 1
            print(f'L: {line.rstrip()}  N: {str(first) + str(last)}')
            total += int(str(first) + str(last))
        print(total)

PartOne()
PartTwo()