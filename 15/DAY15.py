
file = open('C:/Users/Admin/Desktop/ADVENT OF CODE/15/day15input.txt')
lines = file.readlines()

lines = lines[0].split(",")

# print(lines)



def hashAlgo(code):
  sum = 0
  for chr in code:
    sum += ord(chr)
    sum *= 17
    sum %= 256
  return sum


def part1(lines):
  sum = 0
  for code in lines:
    sum += hashAlgo(code)
  
  print(sum)

def part2(lines, hshmap):
  sum = 0
  # Hashing
  for code in lines:
    if '=' in code:
      label, focal = code.split('=')
      box = hashAlgo(label)
      hshmap[box][label] = int(focal)

    if '-' in code:
      label = code[:-1]
      box = hashAlgo(label)
      if label in hshmap[box].keys():
        hshmap[box].pop(label)
  # Summing
  for j in range(len(hshmap)):
    dct = hshmap[j]
    kys = list(dct.keys())
    for i in range(len(kys)):
      sum += (j+1) * (i+1) * dct[kys[i]]

  print(sum)

empty_dictionaries = [{} for _ in range(256)]
part2(lines, empty_dictionaries)
