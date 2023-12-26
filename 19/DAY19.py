import re
import copy
from queue import Queue

file = open('C:/Users/Admin/Desktop/ADVENT OF CODE/19/day19input.txt')
lines = file.readlines()

def strHandling(lines):
  # String handling
  for i in range(len(lines)):
    line = lines[i]
    line = line.replace("\n","")
    lines[i] = line

  for i in range(len(lines)):
    gap = 0
    if lines[i] == '':
      workflows = lines[0:i]
      parts = lines[i+1:]
      parts = xmas(parts)
      workflows = workflow(workflows)
      return workflows, parts
    
def xmas(parts):
  for i in range(len(parts)):
    part = parts[i]
    part = part[1:-1]
    part = part.split(",")
    dic = {}
    for prt in part:
      key, value = prt.split('=')
      dic[key] = int(value)
    parts[i] = dic

  return parts

def workflow(workflows):
  workflowDic = {}
  for wf in workflows:
    wf = wf[:-1]
    location, rules = wf.split("{")
    rules = rules.split(",")
    workflowDic[location] = rules
  return workflowDic

def evaluate(part, rules):
  x, m, a, s = part.values()
  for rule in rules:
    if ':' in rule:
      fnc, destination = rule.split(":")
      if eval(fnc):
        print(destination)
        return destination
    # Means it is the last thing in the list
    else:
      return rule
    
def evaluatep2(rules, rnge):
  contRanges = []
  currRange = copy.deepcopy(rnge)
  for rule in rules:
    if ':' in rule:
      _, destination = rule.split(":")
      intVal = re.findall('\d+', rule)
      intVal = int(intVal[0])
      variable = rule[0]
      conditionMet = copy.deepcopy(currRange) 
      if '<' in rule:
        # value lies in the range [a,b]
        if intVal > conditionMet[variable][0] and intVal < conditionMet[variable][1]:
          conditionMet[variable] = [conditionMet[variable][0], intVal - 1]
          currRange[variable] = [intVal, currRange[variable][1]]
          contRanges.append((destination, conditionMet))
        # b < value (all go, no need to process further rules)
        elif intVal > conditionMet[variable][1]:
          contRanges.append((destination, conditionMet))
          break
        # a > value (nothing goes)
        else:
          continue

      elif '>' in rule:
        # value lies in the range [a,b]
        if intVal > conditionMet[variable][0] and intVal < conditionMet[variable][1]:
          conditionMet[variable] = [intVal+1, conditionMet[variable][1]]
          currRange[variable] = [currRange[variable][0], intVal]
          contRanges.append((destination, conditionMet))
        # a > value (all go, no need to process further rules)
        elif intVal < conditionMet[variable][0]:
          contRanges.append((destination, conditionMet))
          break
        # b < value (nothing goes)
        else:
          continue
      # 'A' or 'R'
    else:
      contRanges.append((rule, currRange))
    
  return contRanges

def sumRange(rnge):
  print(rnge)
  return (rnge['x'][1] - rnge['x'][0] + 1) * (rnge['m'][1] - rnge['m'][0] + 1) * (rnge['a'][1] - rnge['a'][0] + 1) * (rnge['s'][1] - rnge['s'][0] + 1) 

def p2evaluateLoop(rules, start='in', rnge={'x': [1,4000], 'm': [1,4000], 'a': [1,4000], 's': [1,4000]}):
  startingRule = rules[start]

  q = Queue()
  q.put((start,rnge))
  Sum = 0

  while not q.empty():
    loc, currRange = q.get()
    if loc == 'A':
      Sum += sumRange(currRange)
    elif loc != 'R':
      currRules = rules[loc]
      toAdd = evaluatep2(currRules, currRange)
      for item in toAdd:
        q.put((item[0], item[1]))
  
  return Sum

      




def part1(parts, rules, start='in'):
  accepted = []
  for part in parts:
    print(part)
    currentLoc = start
    while currentLoc != 'A' and currentLoc != 'R':
      print(currentLoc)
      currentLoc = evaluate(part, rules[currentLoc])

    if currentLoc == 'A':
      accepted.append(part)

  Sum = 0
  print(accepted)
  for a in accepted:
    Sum += sum(list(a.values()))
  return Sum


workflows, parts = strHandling(lines)
# print(part1(parts, workflows))
print(p2evaluateLoop(workflows))
