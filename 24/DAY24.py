import numpy as np
from collections import deque
from queue import LifoQueue

file = open('C:/Users/Admin/Desktop/ADVENT OF CODE/16/day16input.txt')
lines = file.readlines()

# String handling
for i in range(len(lines)):
  line = lines[i]
  line = line.replace("\n","")
  line = list(line)
  lines[i] = line

