import sys

sys.stdin = open("input15.txt", "r")
sys.stdout = open("output15.txt", "w")

def distance(x1, y1, x2, y2):
  return abs(x1 - x2) + abs(y1 - y2)

distances = { }

for i in range(31):
  info = input().split("=")
  
  x1Info = info[1]
  y1Info = info[2]
  x2Info = info[3]
  y2Info = info[4]

  stop = 0
  for j in range(len(x1Info)):
    if x1Info[j] == ",":
      stop = j
      break
  x1 = int(x1Info[0:stop])

  stop = 0
  for j in range(len(y1Info)):
    if y1Info[j] == ":":
      stop = j
      break
  y1 = int(y1Info[0:stop])

  stop = 0
  for j in range(len(x2Info)):
    if x2Info[j] == ",":
      stop = j
      break
  x2 = int(x2Info[0:stop])

  y2 = int(y2Info)

  distances[tuple([x1, y1])] = distance(x1, y1, x2, y2)

def check(x1, y1):
  hit = 0
  for sensorCheck in distances:
      if distance(x1, y1, sensorCheck[0], sensorCheck[1]) <= distances[sensorCheck]:
        hit = 1
        break
  if hit == 0:
    return True
  else:
    return False

DONE = False

for sensor in distances:

  if DONE:
    break

  d = distances[sensor] + 1
  x = sensor[0]
  y = sensor[1]

  for k in range(d + 1):
    x1 = x - k
    y1 = y - (d - k)
    if 0 < x1 and x1 < 4000000 and 0 < y1 and y1 < 4000000:
      if check(x1, y1):
        DONE = True
        print(4000000 * x1 + y1)
  
  for k in range(d + 1):
    x1 = x - k
    y1 = y + (d - k)
    if 0 < x1 and x1 < 4000000 and 0 < y1 and y1 < 4000000:
      if check(x1, y1):
        DONE = True
        print(4000000 * x1 + y1)
  
  for k in range(d + 1):
    x1 = x + k
    y1 = y - (d - k)
    if 0 < x1 and x1 < 4000000 and 0 < y1 and y1 < 4000000:
      if check(x1, y1):
        DONE = True
        print(4000000 * x1 + y1)
  
  for k in range(d + 1):
    x1 = x + k
    y1 = y + (d - k)
    if 0 < x1 and x1 < 4000000 and 0 < y1 and y1 < 4000000:
      if check(x1, y1):
        DONE = True
        print(4000000 * x1 + y1)
