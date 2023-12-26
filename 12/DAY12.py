file = open('C:/Users/Admin/Desktop/ADVENT OF CODE/12/day12input.txt')
lines = file.readlines()

# # Part 1 string handling
# for i in range(len(lines)):
#   line = lines[i]
#   line = line.replace("\n","")
#   strn, groups = line.split(" ")
#   groups = groups.split(',')
#   groups = tuple(map(lambda x: int(x), groups))
#   lines[i] = [strn, groups]

# test = "33"
# print(test)
# print(len(test[10:]))
# print("test)")


# Part 2 string handling

for i in range(len(lines)):
  line = lines[i]
  line = line.replace("\n","")
  strn, groups = line.split(" ")
  strn = "?".join([strn] * 5)
  print(strn)
  groups = ",".join([groups] * 5)
  print(groups)
  groups = groups.split(',')
  groups = tuple(map(lambda x: int(x), groups))
  lines[i] = [strn, groups]

print(lines)


def validity(spring, damaged):
  idxDmg = 0
  curr = -1
  for i in range(len(spring)):
    currChar = spring[i]
    if currChar == '#':
      if curr == -1:
        if idxDmg >= len(damaged):
          return False
        curr = damaged[idxDmg]
        idxDmg += 1
        curr -= 1
      else:
        curr -= 1
      if curr < 0:
        return False
    else:
      if curr > 0:
        return False
      curr = -1
  if idxDmg < len(damaged):
    return False
  if curr > 0:
    return False
  print(spring)
  print(curr)
  return True


# def solutions(sequence, groups):
#   print(sequence)
#   sum = 0
#   # First, check for '?'
#   for i in range(len(sequence)):
#     if sequence[i] == '?':
      # curr1 = list(sequence)
      # curr1[i] = '.'
      # curr1 = "".join(curr1)
      # sum += solutions(curr1, groups)

      # curr2 = list(sequence)
      # curr2[i] = "#"
      # curr2 = "".join(curr2)
      # sum += solutions(curr2, groups)

#       return sum

#   # If none, validity check
#   return int(validity(sequence, groups))

mem = {}

def solutions(sequence, groups, idx, prevChar):
  if (sequence, groups, idx, prevChar) in mem:
    # print("memo get")
    return mem[(sequence, groups, idx, prevChar)]
  sum = 0
  # Base case: if you reach the end, if tuple is a sequence of zeroes, return 1 (i.e valid)
  if len(sequence) == 0:
    for tp in groups:
      if tp != 0:
        return 0
    return 1
  
  # Length seq not 0.
  if sequence[0] == '.':
    if prevChar == '#':
      if groups[idx] != 0:
        return 0
      idx += 1
    sum = solutions(sequence[1:], groups, idx, '.')
    mem[(sequence, groups, idx-1, prevChar)] = sum
  
  # Else #
  elif sequence[0] == '#':
    # Too many groups
    if idx >= len(groups):
      return 0
    # Too large group
    if groups[idx] <= 0:
      return 0
    lst = list(groups)
    lst[idx] -= 1
    sum = solutions(sequence[1:], tuple(lst), idx, '#')
    mem[(sequence, groups, idx, prevChar)] = sum

  # Else ?
  else:
    curr1 = list(sequence)
    curr1[0] = '.'
    curr1 = "".join(curr1)
    sum += solutions(curr1, groups, idx, prevChar)

    curr2 = list(sequence)
    curr2[0] = "#"
    curr2 = "".join(curr2)
    sum += solutions(curr2, groups, idx, prevChar)

  return sum



sum = 0
for line in lines:
  a = solutions(line[0], line[1], 0, None)
  print(a)
  sum += a

print(sum)
# print(mem)

# print(solutions(lines[0][0], lines[0][1], 0, None))
# print(mem)
# # #Debug
# print(validity(".....######..#####.",(1,6,5)))

