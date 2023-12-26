import numpy as np
from collections import deque
from queue import Queue
import sys


file = open('C:/Users/Admin/Desktop/ADVENT OF CODE/23/day23test.txt')
lines = file.readlines()

# String handling
for i in range(len(lines)):
  line = lines[i]
  line = line.replace("\n","")
  line = list(line)
  lines[i] = line

print(lines)


class StraightPath:
  def __init__(self, start, end, secondlast) -> None:
    self.secondlast = secondlast
    self.weight = -1
    self.start = start
    self.end = end
    self.neighbours = []
  
  def getNeighbours(self):
    for arrow in arrows.keys():
      newCoord = move(self.end, arrow)
      validity = valid(newCoord, self.secondLast, arrow)
      if validity:
        self.neighbours.append(newCoord)

  
START = (0,1)
END = (len(lines)-1, len(lines[0])-2)
print(END)
arrows = {'>':(0,1), '<':(0,-1), 'v':(1,0), '^':(-1,0)}
upslope = {'>':'<', '<':'>', 'v':'^', '^':'v'}
nodes = []

def collapse(lines):
  q = Queue()
  q.put(START)

  while not q.empty():
    curr = q.get()
    strt = curr
    qinq = Queue()
    qinq.put(strt)
    qinqPrevious = None
    pathL = 0
    while not qinq.empty():
      neighbours = []
      curr2 = qinq.get()
      pathL += 1
      if curr2 == END:
        break
      for arrow in arrows.keys():
        newCoord = move(curr2, arrow)
        next = None
        validity = valid(newCoord, qinqPrevious, arrow)
        if validity:
          next = newCoord
          neighbours.append(newCoord)
      if len(neighbours) == 0:
        print("Dead end")
      if len(neighbours) == 1:
        print("Straight")
        qinq.put(next)
      if len(neighbours) > 1:
        print("Junction")
    nodes.append(StraightPath(strt, curr2, neighbours))


    # neighbours = [curr]
    # straight = True
    # while straight:
    #   prevNode = pathNode
    #   pathNode = neighbours[0]
    #   neighbours = []
      # for arrow in arrows.keys():
      #   newCoord = move(curr, arrow)
      #   validity = valid(newCoord, prevNode, arrow)
    #     if validity:
    #       neighbours.append(newCoord)
      
          



def valid(coords, secondLast, arrow):
  # OOB
  if coords[0] < 0 or coords[1] < 0 or coords[0] >= len(lines) or coords[1] >= len(lines[0]):
    return False
  # UPSLOPE
  if lines[coords[0]][coords[1]] == upslope[arrow]:
    return False
  # IN PATH
  if coords == secondLast:
    return False
  # FOREST
  return lines[coords[0]][coords[1]] != '#'


def move(coord, arrow):
    drow, dcol = arrows[arrow]
    newRow = coord[0] + drow
    newCol = coord[1] + dcol
    return (newRow, newCol)

collapse(lines)
