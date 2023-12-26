file = open('C:/Users/Admin/Desktop/ADVENT OF CODE/day6input.txt')
lines = file.readlines()


def splitData1(lines):
  time = lines[0]
  distance = lines[1]

  time = time.split()
  distance = distance.split()
  time = time[1:]
  distance = distance[1:]
  time = map(lambda x: int(x), time)
  distance = map(lambda x: int(x), distance)
  
  return list(time), list(distance)

def splitData2(lines):
  time = lines[0]
  distance = lines[1]

  time = time.split(": ")
  time = time[1]
  time = time.replace(" ", "")
  time = int(time)

  distance = distance.split(": ")
  distance = distance[1]
  distance = distance.replace(" ", "")
  distance = int(distance)
  
  return time, distance


def formula(time, record):
  count = 0

  for i in range(time + 1):
    buttonTime = i
    moveTime = time - i
    distance = buttonTime * moveTime
    if distance > record:
      count += 1

  return count

def part1(time, distance):
  product =  1
  for i in range(len(time)):
    product *= formula(time[i], distance[i])
  
  return product


time, distance = splitData2(lines)
print(formula(time, distance))
# time, distance = splitData1(lines)
# print(part1(time, distance))



  

