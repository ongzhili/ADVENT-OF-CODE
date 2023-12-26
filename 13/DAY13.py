file = open('C:/Users/Admin/Desktop/ADVENT OF CODE/13/day13input.txt')
lines = file.readlines()

# String handling
for i in range(len(lines)):
  line = lines[i]
  line = line.replace("\n","")
  lines[i] = line

partitioned = []
curr = 0
prev = 0
for i in range(len(lines)):
  line = lines[i]
  if line == '':
    curr = i + 1
    partitioned.append(lines[prev:curr-1])
    prev = i + 1
partitioned.append(lines[curr:])

print(partitioned)


def horizLine(pattern):
  indices = []
  for i in range(len(pattern)-1):
    Lpointer = i
    Rpointer = i + 1
    mirrored = True
    while(Lpointer >= 0 and Rpointer < len(pattern)):
      if pattern[Lpointer] != pattern[Rpointer]:
        mirrored = False
      Lpointer -= 1
      Rpointer += 1 
    if mirrored:
      indices.append(i)
  return indices

def vertLine(pattern):
  indices = []
  for i in range(len(pattern[0]) - 1):
    Lpointer = i
    Rpointer = i+1
    mirrored = True
    while(Lpointer >= 0 and Rpointer < len(pattern[0])):
      for ln in pattern:
        if ln[Lpointer] != ln[Rpointer]:
          mirrored = False
      Lpointer -= 1
      Rpointer += 1
    if mirrored:
      indices.append(i)
  return indices



def horizLine2(pattern):
  indices = []
  for i in range(len(pattern)-1):
    Lpointer = i
    Rpointer = i + 1
    mistakes = 0
    while(Lpointer >= 0 and Rpointer < len(pattern)):
      if pattern[Lpointer] != pattern[Rpointer]:
        for j in range(len(pattern[Lpointer])):
          if pattern[Lpointer][j] != pattern[Rpointer][j]:
            mistakes += 1
        
      Lpointer -= 1
      Rpointer += 1 
    if mistakes == 1:
      indices.append(i)
  return indices

def vertLine2(pattern):
  indices = []
  for i in range(len(pattern[0]) - 1):
    Lpointer = i
    Rpointer = i+1
    mistakes = 0
    while(Lpointer >= 0 and Rpointer < len(pattern[0])):
      for ln in pattern:
        if ln[Lpointer] != ln[Rpointer]:
          mistakes += 1
      Lpointer -= 1
      Rpointer += 1
    if mistakes == 1:
      indices.append(i)
  return indices


sum = 0
for pattern in partitioned:
  hL = horizLine(pattern)
  vL = vertLine(pattern)
  for h in hL:
    sum += 100 * (h+1)
  for v in vL:
    sum += v+1

print(sum)

sum2 = 0
for pattern in partitioned:
  hL = horizLine2(pattern)
  vL = vertLine2(pattern)
  print(hL)
  print(vL)
  for h in hL:
    sum2 += 100 * (h+1)
  for v in vL:
    sum2 += v+1

print(sum2)







