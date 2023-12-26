import regex as re



file = open('C:/Users/Admin/Desktop/ADVENT OF CODE/input.txt')
lines = file.readlines()


# PART 1
# sum = 0
# for str in lines:
#   pointerA = 0
#   pointerB = len(str) - 1
#   digitL = False
#   digitR = False
#   digitValL = -1
#   digitValR = -1
#   while not digitL:
#     curr = str[pointerA]
#     if curr.isdigit():
#       digitL = True
#       digitValL = int(curr)
#     else:
#       pointerA += 1
#   while not digitR:
#     curr = str[pointerB]
#     if curr.isdigit():
#       digitR = True
#       digitValR = int(curr)
#     else:
#       pointerB -= 1
#   sum += (10* digitValL) + digitValR

# print(sum)

#PART 2 
sum = 0
stra = "zerofive3one1"
strToInt = {
  "zero": 0,
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9,
  "0": 0,
  "1": 1,
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9
}
reg = ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
rega = "|".join(reg)
print(rega)
for str in lines:
  matches = re.findall(rega,str, overlapped = True)
  print(matches)
  L = strToInt[matches[0]]
  R = strToInt[matches[-1]]
  sum += (10*L) + R

print(sum)



# Using positive lookahead for overlapping matches
file.close()


