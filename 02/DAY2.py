



file = open('C:/Users/Admin/Desktop/ADVENT OF CODE/day2input.txt')

lines = file.readlines()

# Limits

limits = {
  "red": 12,
  "green": 13,
  "blue": 14
}
sum = 0

# Part 1
for line in lines:
  # Removes "Game: "
  id = line[5:]
  # Removes newline (\n)
  id = id.replace("\n", "")
  idSeparated = id.partition(": ")
  # format: [id, ": ", data]
  separatedResults = idSeparated[2].split("; ")
  validSet = True

  for gameSet in separatedResults:

    cubes = gameSet.split(", ")
    for count in cubes:
      val, color = count.split(" ")
      if limits[color] < int(val):
        validSet = False
  if validSet:
    sum += int(idSeparated[0])


# Part 2
for line in lines:
  # Removes "Game: "
  id = line[5:]
  # Removes newline (\n)
  id = id.replace("\n", "")
  idSeparated = id.partition(": ")
  # format: [id, ": ", data]
  separatedResults = idSeparated[2].split("; ")

  mins = {
    "red": 0,
    "green": 0,
    "blue": 0
  }
  for gameSet in separatedResults:

    cubes = gameSet.split(", ")
    for count in cubes:
      val, color = count.split(" ")
      if mins[color] < int(val):
        mins[color] = int(val)
  sum += mins["red"] * mins["green"] * mins["blue"]

print(sum)

  




