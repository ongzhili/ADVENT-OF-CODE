file = open('C:/Users/Admin/Desktop/ADVENT OF CODE/9/day9input.txt')
lines = file.readlines()

# print(lines)


def pars(lines):
  for i in range(len(lines)):
    line = lines[i]
    line = line.replace("\n", "")
    numbers = line.split(" ")
    numbers = map(lambda x: int(x), numbers)
    lines[i] = list(numbers)
  return lines
    

def obtainNextValue(numbers):
  # print(numbers)
  recurs = False
  newSeq = []
  for i in range(len(numbers)-1):
    diff = numbers[i+1] - numbers[i]
    if diff != 0:
      recurs = True
    newSeq.append(diff)
  if not recurs:
    return numbers[-1]
  else:
    return numbers[-1] + obtainNextValue(newSeq)

def obtainPreviousValue(numbers):
  recurs = False
  newSeq = []
  for i in range(len(numbers)-1):
    diff = numbers[i+1] - numbers[i]
    if diff != 0:
      recurs = True
    newSeq.append(diff)
  if not recurs:
    return numbers[0]
  else:
    return numbers[0] - obtainPreviousValue(newSeq)
  
def part1(parsed):
  sum = 0
  for nums in parsed:
    sum += obtainNextValue(nums)
  print(sum)

  
def part2(parsed):
  sum = 0
  for nums in parsed:
    sum += obtainPreviousValue(nums)
  print(sum)

parsed = pars(lines)
# part1(parsed)
part2(parsed)