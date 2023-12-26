from collections import Counter

file = open('C:/Users/Admin/Desktop/ADVENT OF CODE/day7input.txt')
lines = file.readlines()

# print(lines)

def determineHandType(hand, part):
  print(hand)
  if part == 2:
    # Handles J
    j = hand['J']
    if j != 0:
      print(j)
      if "J" in hand:
        del hand['J']
  counts = hand.most_common()
  length = len(counts)
  if part == 2:
    if length == 0:
      # Edge case where 5 Js
      counts.append(('J', 5))
    else:
      counts[0] = (counts[0][0], counts[0][1] + j)
  print(counts)

  match length:
    case 5:
      print("High Card")
      return 0
    case 4:
      print("One pair")
      return 1
    case 3:
      # Two pair / three of a kind
      if counts[0][1] == 2:
        print("Two pair")
        return 2
      else:
        print("3 of a kind")
        return 3
    case 2:
      # 4 of a kind / full house
      if counts[0][1] == 3:
        print("Full House") 
        return 4
      else:
        print("4 of a kind")
        return 5
    case 1:
      print("5 of a kind")
      return 6
    case 0:
      print("5 of a kind J")
      return 6


def lineToDicts(lines, dictionary, part):
  for i in range(len(lines)):
    line = lines[i]
    hand, bid = line.split(" ")
    bid = int(bid)
    order = list(map(lambda x : dictionary[x],list(hand)))

    counts = Counter(hand)
    handType = determineHandType(counts, part)
    order.insert(0, handType)
    order.append(bid)
    lines[i] = tuple(order)
  return lines



def valuecount(lst):
  print(lst)
  sum = 0
  lst = sorted(lst)
  for i in range(len(lst)):
    value = lst[i][-1]
    sum += (i+1) * value
  return sum


p1dictionary = {"2":2,
                "3":3,
                "4":4,
                "5":5,
                "6":6,
                "7":7,
                "8":8,
                "9":9,
                "T":10,
                "J":11,
                "Q":12,
                "K":13,
                "A":14}

p2dictionary = {"2":2,
                "3":3,
                "4":4,
                "5":5,
                "6":6,
                "7":7,
                "8":8,
                "9":9,
                "T":10,
                "J":0,
                "Q":12,
                "K":13,
                "A":14}

handled = lineToDicts(lines, p2dictionary,2)
# print(handled)
part2ans = valuecount(handled)
print(part2ans)
# print(handled)
