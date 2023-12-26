import numpy as np
from collections import deque
from queue import LifoQueue

file = open('C:/Users/Admin/Desktop/ADVENT OF CODE/18/day18input.txt')
lines = file.readlines()

# String handling
for i in range(len(lines)):
  line = lines[i]
  line = line.replace("\n","")
  line = line.split(" ")
  line[1] = int(line[1])
  # line = list(line)
  lines[i] = line

print(lines)

def edge(lines):
  edges = []
  edges.append((0,0))
  pos = [0,0]
  for line in lines:
    distance = line[1]
    match line[0]:
      case 'L':
        pos[1] -= distance
        edges.append((pos[0],pos[1]))
      case 'R':
        pos[1] += distance
        edges.append((pos[0],pos[1]))
      case 'U':
        pos[0] -= distance
        edges.append((pos[0],pos[1]))
      case 'D':
        pos[0] += distance
        edges.append((pos[0],pos[1]))
  edges = list(reversed(edges))
  return edges

def shoelace(edges): 
  sum = 0
  for i in range(len(edges)-1):
    sum += edges[i][0] * edges[i+1][1]
    sum -= edges[i][1] * edges[i+1][0]
  return sum / 2

def perimeter(edges):
  sum = 0
  for i in range(len(edges)-1):
    y2 = pow(edges[i][0] - edges[i+1][0], 2)
    x2 = pow(edges[i][1] - edges[i+1][1], 2)
    sum += pow(x2 + y2, 0.5)
  return sum

    
def hexadec(lines):
  directions = {'0': 'R',
                '1': 'D',
                '2': 'L',
                '3': 'U'}
  fixed = []
  for line in lines:
    dist = int("0x" + line[2][2:7], 16)
    dir = line[2][7]
    fixed.append([directions[dir], dist])
  return fixed


def part1():
  edges = edge(lines)
  ans = shoelace(edges)
  ans += perimeter(edges)/2 + 1

  print(ans)

def part2():
  lns = hexadec(lines)
  edges = edge(lns)
  ans = shoelace(edges)
  ans += perimeter(edges)/2 + 1

  print(ans)


part1()
part2()


