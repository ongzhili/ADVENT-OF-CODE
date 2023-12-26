import regex as re

file = open('C:/Users/Admin/Desktop/ADVENT OF CODE/day3input.txt')

lines = file.readlines()
# for line in lines:
#   line = list(line.replace("\n", ""))

sum = 0
reg = "\d+"
symbols = ["@","$","#","%","*","+","-","=","&","/"]
limx = len(lines[0])
limy = len(lines)

# Part 1

# for i in range(len(lines)):
#   line = lines[i]
#   matches = re.finditer(reg,line)
#   for match in matches:
#     indices = match.span()
#     print(indices)
#     gear = False
#     for j in range(max(indices[0],1), min(indices[1], limx-2),1):
#       for k in range(-1,2,1):
#         if i >= 1:
#           if lines[i-1][j + k] in symbols:
#             gear = True
#         if lines[i][j + k] in symbols:
#           gear = True
#         if i < limy -1:
#           if lines[i+1][j + k] in symbols:
#             gear = True
#     if gear == True:
#       val = 0
#       mult = 1
#       for l in range(indices[1]-1, indices[0]-1, -1):
#         val += int(line[l]) * mult
#         mult *= 10
#       print(val)
#       sum += val


# Part 2

gears = {}

def add_or_append(dictionary, key, value):
  if key not in dictionary:
    dictionary[key] = [value]
  else:
    dictionary[key].append(value)

def findValue(i,j,k):
  line = lines[i]
  value = 0
  mult = 1
  for l in range(k-1, j-1,-1):
    value += mult * int(line[l])
    mult *= 10
  return value



for i in range(len(lines)):
  line = lines[i]
  matches = re.finditer(reg,line)
  for match in matches:
    indices = match.span()
    print(indices)
    # gear = False
    for j in range(max(indices[0],1), min(indices[1], limx-2),1):
      for k in range(-1,2,1):
        if i >= 1:
          if lines[i-1][j + k] in symbols:
            add_or_append(gears, (i-1, j+k), (i, indices))
        if lines[i][j + k] in symbols:
          add_or_append(gears, (i, j+k), (i, indices))
        if i < limy -1:
          if lines[i+1][j + k] in symbols:
            add_or_append(gears, (i+1, j+k), (i, indices))

for key, values in gears.items():
  gears[key] = list(set(values))
for key, values in gears.items():
  if len(values) >= 2:
    this = 1
    print(key)
    for tup in values:
      this *= findValue(tup[0], tup[1][0], tup[1][1])
    sum += this



print(sum)



      
      



