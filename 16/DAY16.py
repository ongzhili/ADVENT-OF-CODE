import numpy as np
from collections import deque
from queue import LifoQueue

# .|...\....
# |.-.\.....
# .....|-...
# ........|.
# ..........
# .........\
# ..../.\\..
# .-.-/..|..
# .|....-|.\
# ..//.|....

file = open('C:/Users/Admin/Desktop/ADVENT OF CODE/16/day16input.txt')
lines = file.readlines()

# String handling
for i in range(len(lines)):
  line = lines[i]
  line = line.replace("\n","")
  line = list(line)
  lines[i] = line


def pathNoRecursion(lines, initialCoords, initialDir):

  visitedDict = set()
  visited = np.empty_like(lines)
  vertLimit = len(visited)
  horizLimit = len(visited[0])
  # queue = deque()
  queue = LifoQueue()
  # Coords are in row,col format
  queue.put((initialCoords[0], initialCoords[1], initialDir))

  while not queue.empty():
    # curr = queue.popleft()
    curr = queue.get()
    row = curr[0]
    col = curr[1]
    dir = curr[2]

    if col >= 0 and col < horizLimit and row >= 0 and row < vertLimit and curr not in visitedDict:
      visitedDict.add(curr)
      visited[row][col] = '#'
      tile = lines[row][col]
      match dir:
        case "up":
          match tile:
            case "\\":
              queue.put((row, col-1, "left"))
              continue
            case "/":
              queue.put((row, col+1, "right"))
              continue
            case ".":
              queue.put((row-1, col, "up"))
              continue
            case "|":
              queue.put((row-1, col, "up"))
              continue
            case "-":
              queue.put((row, col-1, "left"))
              queue.put((row, col+1, "right"))
              continue
          continue
        case "down":
          match tile:
            case "\\":
              queue.put((row, col+1, "right"))
              continue
            case "/":
              queue.put((row, col-1, "left"))
              continue
            case ".":
              queue.put((row+1, col, "down"))
              continue
            case "|":
              queue.put((row+1, col, "down"))
              continue
            case "-":
              queue.put((row, col-1, "left"))
              queue.put((row, col+1, "right"))
              continue
          continue
        case "left":
          match tile:
            case "\\":
              queue.put((row-1, col, "up"))
              continue
            case "/":
              queue.put((row+1, col, "down"))
              continue
            case ".":
              queue.put((row, col-1, "left"))
              continue
            case "|":
              queue.put((row-1, col, "up"))
              queue.put((row+1, col, "down"))
              continue
            case "-":
              queue.put((row, col-1, "left"))
              continue
          continue
        case "right":
          match tile:
            case "\\":
              queue.put((row+1, col, "down"))
              continue
            case "/":
              queue.put((row-1, col, "up"))
              continue
            case ".":
              queue.put((row, col+1, "right"))
              continue
            case "|":
              queue.put((row-1, col, "up"))
              queue.put((row+1, col, "down"))
              continue
            case "-":
              queue.put((row, col+1, "right"))
              continue
          continue
  unique, counts = np.unique(visited, return_counts=True)
  d = dict(zip(unique,counts))
  return d['#']

# part1
def part1():
  return pathNoRecursion(lines, (0,0), "right")

print(part1())

# part2
def part2():
  counts = []
  horizLimit = len(lines[0])
  vertLimit = len(lines)
  
  for i in range(horizLimit):
    counts.append(pathNoRecursion(lines,(0,i),"down"))
    counts.append(pathNoRecursion(lines,(vertLimit-1,i),"up"))

  for i in range(vertLimit):
    counts.append(pathNoRecursion(lines,(i,0),"right"))
    counts.append(pathNoRecursion(lines,(i,horizLimit-1), "left"))
  
  print(counts)
  return max(counts)

print(part2())
