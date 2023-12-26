import numpy as np
from queue import PriorityQueue

file = open('C:/Users/Admin/Desktop/ADVENT OF CODE/17/day17test.txt')
lines = file.readlines()

# 2413432311323
# 3215453535623
# 3255245654254
# 3446585845452
# 4546657867536
# 1438598798454
# 4457876987766
# 3637877979653
# 4654967986887
# 4564679986453
# 1224686865563
# 2546548887735
# 4322674655533

# String handling
for i in range(len(lines)):
  line = lines[i]
  line = line.replace("\n","")
  line = list(map(int, list(line)))
  lines[i] = line

# print(lines)

d = {'HORIZONTAL': 0, 'VERTICAL': 1}

def dijkstras(lines, starting, ending, min_moves_before_turn, max_moves_before_turn):
  colLimit = len(lines[0]) - 1
  rowLimit = len(lines) - 1

  visited = set()
  q = PriorityQueue()
  q.put((0, (starting[0],starting[1], 0)))
  q.put((0, (starting[0],starting[1], 1)))

  while not q.empty():
    
    cost, coords = q.get()
    if (coords[0], coords[1]) == ending:
      print('found')
      break
    if coords in visited:
      continue
    visited.add(coords)
    test = cost
    match coords[2]:
      case 0:
        # HORIZONTAL
        # This range gives -1,1 (turn up/down)
        for j in range(-1,2,2):
          cumSum = test
          for i in range(1, max_moves_before_turn + 1):
            # Horizontal, so turn = row +- moves
            toAdd = coords[0] + (i * j)
      
            if toAdd > rowLimit or toAdd < 0:
              break

            cumSum += lines[toAdd][coords[1]]
            if ((toAdd, coords[1], 1)) in visited:
              continue
            if i > min_moves_before_turn:
              q.put((cumSum, (toAdd, coords[1], 1)))
        
      case 1:
        # VERTICAL
        for j in range(-1,2,2):
          cumSum = test
          for i in range(1, max_moves_before_turn + 1):
            # VERTICAL, so turn = col +- moves
            toAdd = coords[1] + (i * j)
      
            if toAdd > colLimit or toAdd < 0:
              break

            cumSum += lines[coords[0]][toAdd]
            if ((coords[0], toAdd, 0)) in visited:
              continue
            if i > min_moves_before_turn:
              q.put((cumSum, (coords[0], toAdd, 0)))
  return cost




def part1():

  answer = dijkstras(lines, (0,0), (len(lines)-1, len(lines[0])-1),0,3)
  print(answer)

def part2():

  answer = dijkstras(lines, (0,0), (len(lines)-1, len(lines[0])-1), 3,10)
  print(answer)


part1()
part2()

for j in [-1,1]:
  print(j)
