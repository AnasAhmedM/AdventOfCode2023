def PartOne():
    with open("seed_data.txt", 'r') as file:
        seedData = file.readlines()
        seeds = seedData[0].split(':')[1].strip().split(' ')
        #1 seedToSoil = [[Destination Range],[Source Range]]
        seedToSoil = []
        #2 soilToFertilizer = [[Destination Range],[Source Range]]
        soilToFertilizer = []
        #3 fertilizerToWater = [[Destination Range],[Source Range]]
        fertilizerToWater = []
        #4 waterToLight = [[Destination Range],[Source Range]]
        waterToLight = []
        #5 lightToTemperature = [[Destination Range],[Source Range]]
        lightToTemperature = []
        #6 temperatureToHumidity = [[Destination Range],[Source Range]]
        temperatureToHumidity = []
        #7 HumidityToLocation = [[Destination Range],[Source Range]]
        humidityToLocation = []

        cur = 0
        for line in seedData[1:]:
            if line == '\n':
                cur += 1
                continue
            
            if cur == 1:
                if line.__contains__("seed-to-soil map:"):
                    continue
                seedToSoil.append([int(i) for i in line.strip().split(' ')])
            elif cur == 2:
                if line.__contains__("soil-to-fertilizer map:"):
                    continue
                soilToFertilizer.append([int(i) for i in line.strip().split(' ')])
            elif cur == 3:
                if line.__contains__("fertilizer-to-water map:"):
                    continue
                fertilizerToWater.append([int(i) for i in line.strip().split(' ')])
            elif cur == 4:
                if line.__contains__("water-to-light map:"):
                    continue
                waterToLight.append([int(i) for i in line.strip().split(' ')])
            elif cur == 5:
                if line.__contains__("light-to-temperature map:"):
                    continue
                lightToTemperature.append([int(i) for i in line.strip().split(' ')])
            elif cur == 6:
                if line.__contains__("temperature-to-humidity map:"):
                    continue
                temperatureToHumidity.append([int(i) for i in line.strip().split(' ')])
            elif cur == 7:
                if line.__contains__("humidity-to-location map:"):
                    continue
                humidityToLocation.append([int(i) for i in line.strip().split(' ')])

        location= []
        for seed in seeds:
            
            seed = int(seed)
            temp = seed
            
    
            for i in seedToSoil:
                if seed >= i[1] and seed <= i[1]+i[2]:
                    temp = seed + (i[0]-i[1])
                    break
            
            for i in soilToFertilizer:
                if temp >= i[1] and temp <= i[1]+i[2]:
                    temp = temp + (i[0]-i[1])
                    break
            
            for i in fertilizerToWater:
                if temp >= i[1] and temp <= i[1]+i[2]:
                    temp = temp + (i[0]-i[1])
                    break
            
            for i in waterToLight:
                if temp >= i[1] and temp <= i[1]+i[2]:
                    temp = temp + (i[0]-i[1])
                    break
            
            for i in lightToTemperature:
                if temp >= i[1] and temp <= i[1]+i[2]:
                    temp = temp + (i[0]-i[1])
                    break
            
            for i in temperatureToHumidity:
                if temp >= i[1] and temp <= i[1]+i[2]:
                    temp = temp + (i[0]-i[1])
                    break

            for i in humidityToLocation:
                if temp >= i[1] and temp <= i[1]+i[2]:
                    temp = temp + (i[0]-i[1])
                    break
            
            location.append(temp)
        
        print(min(location))

# I ported this code to golang, it works but it will take probably a day to run.
def PartTwo():
    with open("seed_data.txt", 'r') as file:
        seedData = file.readlines()
        seeds = [int(i) for i in seedData[0].split(':')[1].strip().split(' ')]
        #1 seedToSoil = [[Destination Range],[Source Range]]
        seedToSoil = []
        #2 soilToFertilizer = [[Destination Range],[Source Range]]
        soilToFertilizer = []
        #3 fertilizerToWater = [[Destination Range],[Source Range]]
        fertilizerToWater = []
        #4 waterToLight = [[Destination Range],[Source Range]]
        waterToLight = []
        #5 lightToTemperature = [[Destination Range],[Source Range]]
        lightToTemperature = []
        #6 temperatureToHumidity = [[Destination Range],[Source Range]]
        temperatureToHumidity = []
        #7 HumidityToLocation = [[Destination Range],[Source Range]]
        humidityToLocation = []

        cur = 0
        for line in seedData[1:]:
            if line == '\n':
                cur += 1
                continue
            
            if cur == 1:
                if line.__contains__("seed-to-soil map:"):
                    continue
                seedToSoil.append([int(i) for i in line.strip().split(' ')])
            elif cur == 2:
                if line.__contains__("soil-to-fertilizer map:"):
                    continue
                soilToFertilizer.append([int(i) for i in line.strip().split(' ')])
            elif cur == 3:
                if line.__contains__("fertilizer-to-water map:"):
                    continue
                fertilizerToWater.append([int(i) for i in line.strip().split(' ')])
            elif cur == 4:
                if line.__contains__("water-to-light map:"):
                    continue
                waterToLight.append([int(i) for i in line.strip().split(' ')])
            elif cur == 5:
                if line.__contains__("light-to-temperature map:"):
                    continue
                lightToTemperature.append([int(i) for i in line.strip().split(' ')])
            elif cur == 6:
                if line.__contains__("temperature-to-humidity map:"):
                    continue
                temperatureToHumidity.append([int(i) for i in line.strip().split(' ')])
            elif cur == 7:
                if line.__contains__("humidity-to-location map:"):
                    continue
                humidityToLocation.append([int(i) for i in line.strip().split(' ')])

        location= []
        cur = 0
        while cur < len(seeds):
            for seed in range(seeds[cur], seeds[cur]+seeds[cur+1]):
                temp = seed
        
                for i in seedToSoil:
                    if seed >= i[1] and seed <= i[1]+i[2]:
                        temp = seed + (i[0]-i[1])
                        break
                
                for i in soilToFertilizer:
                    if temp >= i[1] and temp <= i[1]+i[2]:
                        temp = temp + (i[0]-i[1])
                        break
                
                for i in fertilizerToWater:
                    if temp >= i[1] and temp <= i[1]+i[2]:
                        temp = temp + (i[0]-i[1])
                        break
                
                for i in waterToLight:
                    if temp >= i[1] and temp <= i[1]+i[2]:
                        temp = temp + (i[0]-i[1])
                        break
                
                for i in lightToTemperature:
                    if temp >= i[1] and temp <= i[1]+i[2]:
                        temp = temp + (i[0]-i[1])
                        break
                
                for i in temperatureToHumidity:
                    if temp >= i[1] and temp <= i[1]+i[2]:
                        temp = temp + (i[0]-i[1])
                        break

                for i in humidityToLocation:
                    if temp >= i[1] and temp <= i[1]+i[2]:
                        temp = temp + (i[0]-i[1])
                        break
                
                location.append(temp)
            cur += 2
            
        print(min(location))

PartTwo()