import sys

sys.stdin = open("input09.txt", "r")
sys.stdout = open("output09.txt", "w")

def findPath(pathHead):
  
  tail = [0, 0]
  listPositions = [[0, 0]]

  for location in pathHead:
    
    if location[0] == tail[0] and location[1] == tail[1] + 2:
      tail[1] += 1
      listPositions.append(tail[:])
      continue

    if location[0] == tail[0] and location[1] == tail[1] - 2:
      tail[1] -= 1
      listPositions.append(tail[:])
      continue

    if location[1] == tail[1] and location[0] == tail[0] + 2:
      tail[0] += 1
      listPositions.append(tail[:])
      continue

    if location[1] == tail[1] and location[0] == tail[0] - 2:
      tail[0] -= 1
      listPositions.append(tail[:])
      continue

    horDistance = location[0] - tail[0]
    verDistance = location[1] - tail[1]

    if horDistance + verDistance >= 3:
      tail[0] += 1
      tail[1] += 1
      listPositions.append(tail[:])
      continue

    if horDistance - verDistance >= 3:
      tail[0] += 1
      tail[1] -= 1
      listPositions.append(tail[:])
      continue

    if horDistance + verDistance <= -3:
      tail[0] -= 1
      tail[1] -= 1
      listPositions.append(tail[:])
      continue

    if 0 - horDistance + verDistance >= 3:
      tail[0] -= 1
      tail[1] += 1
      listPositions.append(tail[:])
      continue

  return listPositions

listPath = [[0, 0]]
headLocation = [0, 0]

for i in range(2000):
  information = input().split()
  
  if information[0] == "U":
    for j in range(int(information[1])):
      headLocation[1] += 1
      listPath.append(headLocation[:])

  if information[0] == "D":
    for j in range(int(information[1])):
      headLocation[1] -= 1
      listPath.append(headLocation[:])

  if information[0] == "R":
    for j in range(int(information[1])):
      headLocation[0] += 1
      listPath.append(headLocation[:])

  if information[0] == "L":
    for j in range(int(information[1])):
      headLocation[0] -= 1
      listPath.append(headLocation[:])

for i in range(9):
  listPath = findPath(listPath)

newPath = []
for location in listPath:
  if not location in newPath:
    newPath.append(location)

print(len(newPath))
