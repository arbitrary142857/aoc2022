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

total = 0

for X in range(-1000001, 6000000):
  hit = 0
  for sensor in distances:
    if distance(X, 2000000, sensor[0], sensor[1]) <= distances[sensor]:
      hit = 1
      break
  if hit == 1:
    total += 1

print(total - 1)
