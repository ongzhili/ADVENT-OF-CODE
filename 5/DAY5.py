import regex as re

file = open('C:/Users/Admin/Desktop/ADVENT OF CODE/day5example.txt')
lines = file.readlines()

def separateMap(lines):
  # Separates the text input into an array of maps.
  components = []
  previousi = 0

  for i in range(len(lines)):
    if lines[i] == '\n':
      components.append(lines[previousi:i])
      previousi = i+1
  components.append(lines[previousi:len(lines)-1])

  # for component in components:
  # print(components[1])
  return components

def getSeeds(seeds):
  seeds = seeds.split(": ")[1]
  seeds = seeds.split(" ")
  for i in range(len(seeds)):
    seeds[i] = int(seeds[i])

  return seeds

def convertMaps(maps):
  tuplemap = []
  # Start from 1, as 1st element is seeds
  for i in range(1, len(maps)):
    map = maps[i]
    addToMap = []
    # Start from 1, as 1st element is title of map
    for j in range(1, len(map)):
      values = map[j]
      values = values.split(" ")
      for k in range(len(values)):
        values[k] = int(values[k])
      addToMap.append(values)
    maps[i] = addToMap
  return maps

def seedToLocation(seed, map):
  print(seed)
  currentValue = seed
  # Per map loop
  for i in range(1, len(map)):
    currentMap = map[i]
    print(currentValue)
    print(currentMap)
    # Per component in map
    converted = False
    for component in currentMap:
      # c[1] = starting, c[0]= end, c[2] = range
      if (currentValue >= component[1]) and (currentValue < component[1] + component[2]) and (not converted):
        # print(component)
        print("Converted")
        offset = component[0] - component[1]
        currentValue = currentValue + offset
        converted = True
      
  
  print((seed, currentValue))
  return currentValue

def part2(startingSeed, seedRange, map):
  ranges = []
  newranges = []
  initialRange = (startingSeed, startingSeed + seedRange - 1)
  newranges.append(initialRange)
  # Per map loop
  for i in range(1, len(map)):
    ranges = newranges
    newranges = []
    currentMap = map[i]
    print(currentMap)
    for rnge in ranges:
      leftovers = []
      leftovers.append(rnge)
      # print(component)
      # print(ranges)
      for component in currentMap:
        for leftover in leftovers:
        # if lowest value of map > highest value of range or highest value of map < lowest value of range: no match!
        # if not ((component[1] > rnge[1]) or (component[1] + component[2] < rnge[0])):
          intersectL = max(component[1], leftover[0])
          intersectR = min(component[1] + component[2], leftover[1])
          if intersectL <= intersectR:
            print((intersectL, intersectR))
            print("Converted to: ")
            offset = component[0] - component[1]
            print((intersectL + offset, intersectR + offset))
            newranges.append((intersectL + offset, intersectR + offset))

            # Handles unmapped
            print("Range removed: ")
            print(leftover)
            leftovers.remove(leftover)
            if intersectL > leftover[0]:
              leftovers.append((leftover[0], intersectL-1))
            if intersectR < leftover[1]:
              leftovers.append((intersectR+1, leftover[1]))

      # Deal with unconverted
      for rnge in leftovers:
        newranges.append(rnge)

    print(newranges)
    print("Done with component \n")
    
  return newranges



map = separateMap(lines)
seeds = map[0][0]
map[0] = getSeeds(seeds)
seeds = map[0]
map = convertMaps(map)

answers = []
for j in range(1,len(seeds), 2):
  print(j)
  print((seeds[j-1], seeds[j-1] + seeds[j]-1))
  mapped = part2(seeds[j-1], seeds[j], map)
  # print(mapped)
  for tup in mapped:
    answers.append(tup[0])


print(min(answers))





# print(map[0])

# # Part 1
# answers = []
# for seed in map[0]:
#   # print(seed)
#   ans = seedToLocation(seed, map)
#   answers.append(ans)
# print(answers)
# print(min(answers))




  
  