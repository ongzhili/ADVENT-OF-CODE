file = open('C:/Users/Admin/Desktop/ADVENT OF CODE/11/day11test.txt')
lines = file.readlines()

    
def findGalaxies(lines):
  galaxies = []
  for i in range(len(lines)):
    print(len(lines[0]))
    for j in range(len(lines[i])):
      if lines[i][j] == '#':
        galaxies.append((i,j))
  print(galaxies)
  return galaxies

def findIndices(lines):
  horizontals = []
  verticals = []
  verticals2 = []
  horizL = len(lines[0]) -1
  
  # Find expand indices

  for i in range(len(lines)):
    line = lines[i]
    lines[i] = line.replace("\n", "")
    empty = True
    for j in range(len(lines[i])):
      if lines[i][j] == "#":
        empty = False
        verticals.append(j)
    if empty:
      horizontals.append(i)
  
  verticals = list(set(verticals))
  for i in range(horizL):
    if i not in verticals:
      verticals2.append(i)
  verticals = verticals2

  return horizontals, verticals

def dist(expansionFactor, galaxies, horizontals, verticals):
  sum = 0
  for galaxy1 in galaxies:
    for galaxy2 in galaxies:
      dist = 0
      if galaxy1 != galaxy2:
        for spc in horizontals:
          if (galaxy1[0] < spc and galaxy2[0] > spc) or (galaxy1[0] > spc and galaxy2[0] < spc):
            dist += expansionFactor
        for spc in verticals:
          if (galaxy1[1] < spc and galaxy2[1] > spc) or (galaxy1[1] > spc and galaxy2[1] < spc):
            dist += expansionFactor
      sum += abs(galaxy2[0] - galaxy1[0]) + abs(galaxy2[1] - galaxy1[1])
      sum += dist

        
  print(sum/2)


galaxies = findGalaxies(lines)
hor, ver = findIndices(lines)
# part 1
dist(1, galaxies, hor, ver)

# part 2
dist(999999, galaxies, hor, ver)
