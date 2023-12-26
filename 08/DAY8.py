import math

file = open('C:/Users/Admin/Desktop/ADVENT OF CODE/8/day8input.txt')
lines = file.readlines()

def nodeify(lines, dictionary):
  for line in lines:
    node, children = line.split(" = ")
    children = children.replace(",", "")
    children = children.replace("(", "")
    children = children.replace(")", "")
    children = children.replace("\n", "")
    left, right = children.split(" ")
    dictionary[node] = (left, right)
    
def search1(sequence, dictionary):
  curr = 'AAA'
  count = 0

  while curr != 'ZZZ':
    for i in range(len(sequence)):
      print(sequence[i])
      if sequence[i] == 'R':
        print("Went Right")
        curr = dictionary[curr][1]
        count += 1
      else:
        print("Went Left")
        curr = dictionary[curr][0]
        count += 1
    
  return count

# def search2(sequence, dictionary):
#   kys = list(dictionary.keys())
#   starts = []
#   next = []
#   count = 0
#   for key in kys:
#     if 'A' in key:
#       print(key)
#       starts.append(key)
    
#   allFound = False
  
#   while not allFound:
#     for i in range(len(sequence)):
#       end = True
#       for node in starts:
#         # print(sequence[i])
#         if sequence[i] == 'R':
#           # print("Went Right")
#           nxt = dictionary[node][1]
#           next.append(nxt)
#         else:
#           # print("Went Left")
#           nxt = dictionary[node][0]
#           next.append(nxt)
#       count += 1
#       for child in next:
#         if 'Z' not in child:
#           end = False
#         else:
#           print(child)
#       if end:
#         return count
#       starts = next
#       next = []
  
#   return count

def search1modified(start, sequence, dictionary):
  curr = start
  count = 0

  while 'Z' not in curr:
    for i in range(len(sequence)):
      print(sequence[i])
      if sequence[i] == 'R':
        curr = dictionary[curr][1]
        count += 1
      else:
        curr = dictionary[curr][0]
        count += 1
    
  return count


def search2(sequence, dictionary):
  kys = list(dictionary.keys())
  starts = []
  period = []
  for key in kys:
    if 'A' in key:
      print(key)
      starts.append(key)
  for start in starts:
    period.append(search1modified(start, sequence, part1))
  
  return math.lcm(*period)




part1 = {}

sequence = lines[0]
sequence = sequence.replace("\n", "")
nodes = lines[2:]
nodeify(nodes, part1)
print(sequence)
# print(search1(sequence, part1))
print(search2(sequence, part1))
