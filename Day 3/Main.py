symbols = {"@","#","$","%","&","*","+","-", "/", "="}

def PartOne():
    with open("engine_schematic.txt", "r") as f:
        engineValues = f.readlines()
        total = 0
        for ln, line in enumerate(engineValues):
            cn = 0
            while cn < len(line):
                char = line[cn]
                if char.isdigit():
                    number = char
                    while cn+1 != len(line)-1 and line[(cn+1)].isdigit():
                        number += line[cn+1]
                        cn += 1
                    
                    passed = False
                    if cn+1 != len(line)-1 and line[(cn+1)] in symbols:
                        passed = True

                    if cn-len(number) >= 0 and line[(cn-len(number))] in symbols:
                        passed = True

                    if ln != 0:
                        line2 = engineValues[ln-1]
                        cn2 = cn+1
                        while cn2 >= cn-len(number):
                            if line2[cn2] in symbols:
                                passed = True
                            cn2 -= 1

                    if ln != len(engineValues)-1:
                        line2 = engineValues[ln+1]
                        cn2 = cn+1
                        while cn2 >= cn-len(number):
                            if line2[cn2] in symbols:
                                passed = True
                            cn2 -= 1
                    
                    if passed:
                        total += int(number)
                
                cn += 1
        print(total)

def PartTwo():
    with open("engine_schematic.txt", "r") as f:
        engineValues = f.readlines()
        total = 0
        for ln, line in enumerate(engineValues):
            cn = 0
            while cn < len(line):
                char = line[cn]
                if char == '*':
                    numbers = []

                    number = ""
                    if cn-1 >= 0:
                        cn2 = cn-1
                        while cn2 >= 0 and line[cn2].isdigit():
                            number = line[cn2] + number
                            cn2 -= 1
                        
                        if number != "":
                            numbers.append(int(number))
                    
                    number = ""
                    if cn+1 < len(line):
                        cn2 = cn+1
                        while cn2 < len(line) and line[cn2].isdigit():
                            number += line[cn2]
                            cn2 += 1
                        
                        if number != "":
                            numbers.append(int(number))
                    
                    if ln != 0:
                        line2 = engineValues[ln-1]
                        left = cn-1 >= 0 and line2[cn-1].isdigit()
                        right = cn+1 < len(line2) and line2[cn+1].isdigit()
                        if line2[cn].isdigit():    
                            if left and right:
                                line2 = line2[cn-1:cn+2]
                            elif left:
                                line2 = line2[cn-2:cn+2]
                            elif right:
                                line2 = line2[cn:cn+3]
                        else:
                            if left and right:
                                line2 = line2[cn-3:cn+4]
                            elif left:
                                line2 = line2[cn-3:cn]
                            elif right:
                                line2 = line2[cn:cn+4]
                            else:
                                line2 = ""
                        cn2 = 0
                        while cn2 < len(line2):
                            char2 = line2[cn2]
                            if char2.isdigit():
                                number = char2
                                while cn2+1 <= len(line2)-1 and line2[(cn2+1)].isdigit():
                                    number += line2[cn2+1]
                                    cn2 += 1
                                numbers.append(int(number))
                            cn2 += 1
                    
                    if ln != len(engineValues)-1:
                        line2 = engineValues[ln+1]
                        left = cn-1 >= 0 and line2[cn-1].isdigit()
                        right = cn+1 < len(line2) and line2[cn+1].isdigit()
                        if line2[cn].isdigit():
                            if left and right:
                                line2 = line2[cn-1:cn+2]
                            elif left:
                                line2 = line2[cn-2:cn+2]
                            elif right:
                                line2 = line2[cn:cn+3]
                        else:
                            if left and right:
                                line2 = line2[cn-3:cn+4]
                            elif left:
                                line2 = line2[cn-3:cn]
                            elif right:
                                line2 = line2[cn:cn+4]
                            else:
                                line2 = ""
                        cn2 = 0
                        while cn2 < len(line2):
                            char2 = line2[cn2]
                            if char2.isdigit():
                                number = char2
                                while cn2+1 <= len(line2)-1 and line2[(cn2+1)].isdigit():
                                    number += line2[cn2+1]
                                    cn2 += 1
                                numbers.append(int(number))
                            cn2 += 1
                    
                    print(numbers)
                    if len(numbers) == 2:
                        total += numbers[0] * numbers[1]
                cn += 1
        print(total)
                        


            

#PartOne()
PartTwo()

#.....*.....
#......434..

#.....*.....
#.....434...

#.....*.....
#....434....

#.....*.....
#...434.....

#.....*.....
#..434......