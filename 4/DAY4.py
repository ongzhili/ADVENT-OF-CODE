import regex as re

file = open('C:/Users/Admin/Desktop/ADVENT OF CODE/day4input.txt')
lines = file.readlines()

def handleData(line):
  noNewLine = line.replace("\n", "")
  removeCard = noNewLine.split(": ")[1]
  winningNumbers, cardNumbers = removeCard.split(" | ")

  # Get winning numbers
  winningNumbers = winningNumbers.split(" ")
  cardNumbers = cardNumbers.split(" ")
  
  # Remove " "
  winningNumbers = list(filter(lambda x: x != "", winningNumbers))
  cardNumbers = list(filter(lambda x: x != "", cardNumbers))

  return winningNumbers, cardNumbers


def part1(lines):
  sum = 0

  for line in lines:
    winningNumbers, cardNumbers = handleData(line)

    matches = len(set(winningNumbers) & set(cardNumbers))
    if matches > 0:
      sum += pow(2, matches-1)

  return sum

def part2(lines):
  counts = {}
  counts = dict.fromkeys(range(len(lines)), 1)

  for i in range(len(lines)):
    line = lines[i]
    winningNumbers, cardNumbers = handleData(line)

    matches = len(set(winningNumbers) & set(cardNumbers))
    currCount = counts[i]
    if matches > 0:
      for k in range(1,matches+1,1):
        counts[k+i] += currCount
  
  ans = sum(counts.values())
  return ans

answer = part1(lines)
print(answer)
answer = part2(lines)
print(answer)
  