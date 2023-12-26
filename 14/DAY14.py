import copy

# O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#....

file = open('C:/Users/Admin/Desktop/ADVENT OF CODE/14/day14input.txt')
lines = file.readlines()

# String handling
for i in range(len(lines)):
  line = lines[i]
  line = line.replace("\n","")
  line = list(line)
  lines[i] = line

def moveNorth(rocks):
  length = len(rocks[0])
  for horiz in range(length):

    for vert in range(len(rocks)):
      if rocks[vert][horiz] == 'O':
        # print("aaaaaaaaaaaa")
        # print(vert)
        i = vert - 1
        swap = False
        while i >= 0:
          # print(i)
          if rocks[i][horiz] == 'O' or rocks[i][horiz] == '#':
            # print("Swap")
            swap = True
            rocks[vert][horiz] = '.'
            rocks[i+1][horiz] = 'O'
            break
          i -= 1
        if swap == False:
          rocks[vert][horiz] = '.'
          rocks[0][horiz] = 'O'

  return rocks
      
def weights(moved):
  idx = len(moved)
  sum = 0
  for i in range(idx):
    row = moved[i]
    for chr in row:
      if chr == 'O':
        sum += idx - i
  
  print(sum)

def rotate(rocks):
  transposed_reversed_array = [list(reversed(row)) for row in zip(*rocks)]
  return transposed_reversed_array


seenBefore = []
def cycle(rocks, times):
  curr = rocks

  for j in range(times):
    seenBefore.append(copy.deepcopy(curr))
    for i in range(4):
      curr = moveNorth(curr)
      curr = rotate(curr)

    if curr in seenBefore:
      print("griddy hit")
      cyclestart = seenBefore.index(curr)
      cycleLength = len(seenBefore) - cyclestart
      griddy = seenBefore[((times - cyclestart) % cycleLength) + cyclestart]
      return griddy
  return curr


# # Part 1
# part1 = moveNorth(lines)
# weights(part1)

# # Part 2
# lines = cycle(lines, 1000000000)

# weights(lines)