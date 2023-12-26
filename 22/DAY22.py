from queue import Queue

file = open('C:/Users/Admin/Desktop/ADVENT OF CODE/22/day22input.txt')
lines = file.readlines()

# String handling
for i in range(len(lines)):
  line = lines[i]
  line = line.replace("\n","")
  line = line.split("~")
  for j in range(len(line)):
    ln = line[j]
    ln = ln.split(",")
    ln = (int(ln[0]), int(ln[1]), int(ln[2]))
    print(ln)
    line[j] = ln
    
  lines[i] = tuple(line)

sorter = lambda x: (x[0][2], x[1][2])
lines = sorted(lines, key=sorter)

print(lines)

class brick:
  def __init__(self, coords) -> None:
    self.x1, self.y1, self.z1 = coords[0]
    self.x2, self.y2, self.z2 = coords[1]
    self.bricksItIsOn = []
    self.bricksSupporting = []
  
  def supported(self, brck):

    if brck.z1 != (1 + max(self.z1,self.z2)) and brck.z2 != (1 + max(self.z1,self.z2)):
      return False
    else:
      for i in range(brck.x1, brck.x2+1):
        for j in range(brck.y1, brck.y2+1):
          if i >= self.x1 and i <= self.x2 and j >= self.y1 and j <= self.y2:
            self.bricksSupporting.append(brck)
            return True
      return False
  
  def falling(self):
    Found = False
    while self.z1 > 1 and self.z2 > 1:
      if not Found:
        for brck in fallenBricks:
          if brck.supported(self):
            self.bricksItIsOn.append(brck)
            Found = True
      if Found:
        break
      self.z1 -= 1
      self.z2 -= 1
    # print("BRICK OF {},{},{} ~ {},{},{} ADDED:".format(self.x1,self.y1,self.z1,self.x2,self.y2,self.z2))
      
  
fallenBricks = []

for brickCoords in lines:
  # print(brickCoords)
  brck = brick(brickCoords)
  brck.falling()
  fallenBricks.append(brck)

for brck in fallenBricks:
  a=1
  # print("BRICK OF {},{},{} ~ {},{},{}:".format(brck.x1,brck.y1,brck.z1,brck.x2,brck.y2,brck.z2))
  # print(len(brck.bricksSupporting))
  # print(len(brck.bricksItIsOn))

count = 0

# Part 1
for brck in fallenBricks:
  supporting = brck.bricksSupporting
  supportedBy = brck.bricksItIsOn
  # print("BRICK OF {},{},{} ~ {},{},{}:".format(brck.x1,brck.y1,brck.z1,brck.x2,brck.y2,brck.z2))
  if len(supporting) == 0:
    # print("Not supporting")
    count += 1
  else:
    safe = True
    for supportingBrick in supporting:
      if len(supportingBrick.bricksItIsOn) == 1:
        safe = False
    if safe:
      # print("Safe")
      count += 1
    else:
      a=1
      # print("Other blocks depend on it")


# Part 2
Sum = 0

for brck in fallenBricks:
  # print("BRICK OF {},{},{} ~ {},{},{}:".format(brck.x1,brck.y1,brck.z1,brck.x2,brck.y2,brck.z2))
  chain = 0
  seen = []
  q = Queue()
  q.put(brck)

  while not q.empty():
    curr = q.get()
    if curr not in seen:
      seen.append(curr)
      for supportingBrick in curr.bricksSupporting:
        if all(a in seen for a in supportingBrick.bricksItIsOn):
          chain += 1
          # print("{},{},{} ~ {},{},{} chained".format(supportingBrick.x1,supportingBrick.y1,supportingBrick.z1,supportingBrick.x2,supportingBrick.y2,supportingBrick.z2))
          q.put(supportingBrick)
  print("BRICK OF {},{},{} ~ {},{},{}: {}".format(brck.x1,brck.y1,brck.z1,brck.x2,brck.y2,brck.z2, chain))
  Sum += chain

print("Part 1: {}".format(count))
print("Part 2: {}".format(Sum))