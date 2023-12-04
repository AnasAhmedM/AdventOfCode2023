def PartOne():
    with open("game_data.txt", 'r') as file:
        gameData = file.readlines()
        score = 0
        for ln, line in enumerate(gameData, 1):
            numbers = line.split(':')[1]
            wNumbers = numbers.split('|')[0].split(' ')
            mNumbers = numbers.split('|')[1].rstrip().split(' ')

            while '' in wNumbers:
                wNumbers.remove('')

            while '' in mNumbers:
                mNumbers.remove('')

            matches = len(set(wNumbers).intersection(mNumbers))
        
            cardV = 0
            if matches >= 1:
                cardV = 1
                for i in range(matches-1):
                    cardV *= 2
            
            score += cardV
        
        
        print(score)

def PartTwo():
    with open("game_data.txt", 'r') as file:
        gameData = file.readlines()
        matches = {}
        for card, line in enumerate(gameData, 1):
            numbers = line.split(':')[1]
            wNumbers = numbers.split('|')[0].split(' ')
            mNumbers = numbers.split('|')[1].rstrip().split(' ')

            while '' in wNumbers:
                wNumbers.remove('')

            while '' in mNumbers:
                mNumbers.remove('')

            match = len(set(wNumbers).intersection(mNumbers))
            matches[card] = match
        
        cards = {i:1 for i in matches.keys()}
        print(cards)
        for card, m in matches.items():
            instances = cards[card]
            for i in range(instances):
                for j in range (m):
                    next = card + j + 1
                    cards[next] = cards[next] + 1
        
        print(sum(cards.values()))

PartOne()
PartTwo()