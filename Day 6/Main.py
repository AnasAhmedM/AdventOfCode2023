times = [52, 94, 75, 94]
distances = [426, 1374, 1279, 1216]


def PartOne():
    wins = []
    for i in range(0, len(times)):
        time = times[i]
        win = distances[i]

        
        count = 0
        for hold in range(1, time):
            t = time - hold
            distance = t * hold

            if distance > win:
                count += 1

        print(count)
        wins.append(count)

    total = 1
    for win in wins:
        total *= win

    print(total)

def PartTwo():
    time = ""
    for i in times:
        time += str(i)
    
    win = ""
    for i in distances:
        win += str(i)

    time = int(time)
    win = int(win)
    
    count = 0
    for hold in range(1, time):
        t = time - hold
        distance = t * hold

        if distance > win:
            count += 1

    print(count)

PartTwo()
    


