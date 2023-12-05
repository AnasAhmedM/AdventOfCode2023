package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"sync"
)

func main() {
	file, err := os.Open("seed_data.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Scan()

	seedData := scanner.Text()
	seedStr := strings.Split(strings.Split(seedData, ":")[1], " ")
	var seeds []int
	for _, s := range seedStr {
		seed, err := strconv.Atoi(strings.TrimSpace(s))
		if err != nil {
			continue
		}
		seeds = append(seeds, seed)
	}

	var seedToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTemperature, temperatureToHumidity, humidityToLocation [][]int
	maps := []*[][]int{&seedToSoil, &soilToFertilizer, &fertilizerToWater, &waterToLight, &lightToTemperature, &temperatureToHumidity, &humidityToLocation}

	cur := 0
	for scanner.Scan() {
		line := scanner.Text()

		if line == "" {
			cur++
			continue
		}

		if cur < len(maps) {
			if !strings.Contains(line, "map:") {
				nums := strings.Split(line, " ")
				var intSlice []int
				for _, n := range nums {
					num, err := strconv.Atoi(n)
					if err != nil {
						continue
					}
					intSlice = append(intSlice, num)
				}
				*maps[cur] = append(*maps[cur], intSlice)
			}
		}
	}

	minLocation := int(0)
	var wg sync.WaitGroup
	for i := 0; i < len(seeds); i += 2 {
		wg.Add(1)
		go func(i int) {
			defer wg.Done()
			seedNumber := i/2 + 1
			for seed := seeds[i]; seed < seeds[i]+seeds[i+1]; seed++ {
				temp := seed
				for _, mapping := range maps {
					for _, m := range *mapping {
						if temp >= m[1] && temp <= m[1]+m[2] {
							temp = temp + (m[0] - m[1])
							break
						}
					}
				}
				if minLocation == 0 || temp < minLocation {
					minLocation = temp
				}
			}
			fmt.Println("Seed range ", seedNumber, " done")
		}(i)
	}
	wg.Wait()

	fmt.Println(minLocation)
}
