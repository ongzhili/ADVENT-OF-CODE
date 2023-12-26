from queue import Queue
import math

file = open('C:/Users/Admin/Desktop/ADVENT OF CODE/21/day21input.txt')
lines = file.readlines()

# String handling
for i in range(len(lines)):
  line = lines[i]
  line = line.replace("\n","")
  line = list(line)
  lines[i] = line

print(lines)

def findS(lines):
  for i in range(len(lines)):
    for j in range(len(lines[0])):
      if lines[i][j] == 'S':
        return (i,j)


dirs = {
  # 0 UP, 1 DOWN, 2 LEFT, 3 RIGHT
  0: (-1, 0),
  1: (1, 0),
  2: (0, -1),
  3: (0, 1)
}

def valid(dir, lines, current, depth):
  newRow = (current[0] + dirs[dir][0] ) % len(lines)
  newCol = (current[1] + dirs[dir][1]) % len(lines[0])
  # if newRow < 0 or newRow > (len(lines) - 1) or newCol < 0 or newCol > (len(lines[0]) -1):
  #   return False

  if lines[newRow][newCol] == '.' or lines[newRow][newCol] == 'S':
    # print("({},{}) at {}".format(newRow,newCol, depth))
    return True
  return False

def bfs(lines, start, steps):
  h = len(lines)
  w = len(lines[0])
  count = 0
  visited = {}
  q = Queue()
  q.put((start, 0))
  visited[(start, 0)] = True

  while not q.empty():
    coords, depth = q.get()
    if depth >= steps:
      break

    for i in range(4):
      if valid(i, lines, coords, depth):
        dir = dirs[i]
        newCoords = ((coords[0] + dir[0]) , (coords[1] + dir[1]))
        nextDepth = depth + 1
        if (newCoords, depth+1) not in visited:
          q.put((newCoords, depth + 1))
          visited[(newCoords, depth + 1)] = True
          if nextDepth == steps:
            count += 1
  
  return count



row, col = findS(lines)
print("S Coordinates are: ({},{})".format(row, col))

print("({},{})".format(len(lines), len(lines[0])))

# Part 1
# print(bfs(lines, (row,col), 64))


# Part 2
h, w = len(lines), len(lines[0])

x1, x2, x3 = 65, 65+131, 65+131+131

y1 = bfs(lines, (row,col), h // 2)
y2 = bfs(lines, (row,col), (h // 2) + 131)
y3 = bfs(lines, (row,col), (h // 2) + (2*131))


def lagrange(x):
  return (y1 * ( ((x - x2) * (x - x3)) / ((x1 - x2) * (x1 - x3)) ) + 
          y2 * ( ((x - x1) * (x - x3)) / ((x2 - x1) * (x2 - x3)) ) + 
          y3 * ( ((x - x1) * (x - x2)) / ((x3 - x1) * (x3 - x2)) ))

print(math.floor(lagrange(26501365)))