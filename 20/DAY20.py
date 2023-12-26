
from queue import Queue

file = open('C:/Users/Admin/Desktop/ADVENT OF CODE/20/day20input.txt')
lines = file.readlines()

# String handling
for i in range(len(lines)):
  line = lines[i]
  line = line.replace("\n","")
  line = line.split(" -> ")
  line[1] = line[1].split(", ")
  lines[i] = line

# print(lines)


# PULSE: HIGH = True, Low = FALSE

class flipflop: 
  # STATE: False = OFF, True = ON
  def __init__(self, nme, toSend) -> None:
    self.state = False
    self.name = nme
    self.recieve = {}
    self.send = toSend

  def getPulse(self, pulse, module):
    if pulse == False:
      self.state = not self.state
      q.put(lambda: self.pulse())

  def pulse(self):
    for reciepient in self.send:
      # print("{} Sending {} to: {}".format(self.name, self.state, reciepient))
      reciepientObj = modules[reciepient]
      counts[self.state] += 1
      reciepientObj.getPulse(self.state, self)

  

class con:
  # STATE: False = Low, True = High
  def __init__(self, nme, toSend) -> None:
    self.state = False
    self.name = nme
    self.recieve = {}
    self.send = toSend

  def getPulse(self, pulse, module):
    self.recieve[module] = pulse

    if module.name in found.keys() and pulse:
      found[module.name] = True

    if all(self.recieve.values()):
      self.state = False
    else:
      self.state = True
    # for signal in self.recieve.values():
    #   if signal == False:
    #     self.state = True
    q.put(lambda: self.pulse())

  def pulse(self):
    for reciepient in self.send:
        
      # print("{} Sending {} to: {}".format(self.name, self.state, reciepient))
      reciepientObj = modules[reciepient]
      counts[self.state] += 1
      reciepientObj.getPulse(self.state, self)


class broadcaster:
  def __init__(self, nme, toSend) -> None:
    self.state = False
    self.name = nme
    self.recieve = {}
    self.send = toSend
  
  def getPulse(self, pulse, module):
    self.state = pulse
    q.put(lambda: self.pulse())

  def pulse(self):
    for reciepient in self.send:
      # print("{} Sending {} to: {}".format(self.name, self.state, reciepient))
      reciepientObj = modules[reciepient]
      counts[self.state] += 1
      reciepientObj.getPulse(self.state, self)

class nothingburger:
  def __init__(self, nme, toSend) -> None:
    self.state = False
    self.name = nme
    self.recieve = {}
    self.send = toSend

  def getPulse(self, pulse, module):
    self.state = pulse
    if pulse == False and self.name == 'rx':
      rxFound = True
    q.put(lambda: self.pulse())

  def pulse(self):
    for reciepient in self.send:
      reciepientObj = modules[reciepient]
      counts[self.state] += 1
      reciepientObj.getPulse(self.state, self)




modules = {}
counts = {False: 0, True: 0}
conProcessing = []
num_presses = 1000
found = {'pv': False, 'qh': False, 'xm': False, 'hz': False}
q = Queue()

for line in lines:
  if line[0] == 'broadcaster':
    modules[line[0]] = broadcaster(line[0], line[1])
  elif line[0][0] == '%':
    modules[line[0][1:]] = flipflop(line[0][1:], line[1])
  else:
    modules[line[0][1:]] = con(line[0][1:], line[1])
    conProcessing.append(line[0][1:])


for line in lines:
  for reciepient in line[1]:
    if reciepient not in modules:
      modules[reciepient] = nothingburger(reciepient, [])

for line in lines:
  for ln in line[1]:
    if ln in conProcessing:
      modules[ln].recieve[modules[line[0][1:]]] = False


# # Part 1
# for i in range(num_presses):
#   counts[False] += 1

#   q.put(lambda: modules['broadcaster'].getPulse(False, None))

#   while not q.empty():
#     func = q.get()
#     func()
#     if rxFound == True:
#       print(i + 1)

# print(counts[False] * counts[True])


# Part 2
p1 = False
p2 = False
p3 = False
p4 = False
a = 0
b = 0
c = 0
d = 0

i = 0

while (not p1) or (not p2) or (not p3) or (not p4):
  i += 1
  q.put(lambda: modules['broadcaster'].getPulse(False, None))
  # print(i)

  while not q.empty():
    func = q.get()
    func()
  if found['pv'] and not p1:
    print("pvHigh: {}".format(i))
    p1 = True
    a = i
  if found['qh'] and not p2:
    print("qhHigh: {}".format(i))
    p2 = True
    b = i
  if found['xm'] and not p3:
    print("xmHigh: {}".format(i))
    p3 = True
    c = i
  if found['hz'] and not p4:
    print("hzHigh: {}".format(i))
    p4 = True
    d = i

print(a * b * c * d)