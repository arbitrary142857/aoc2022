import sys

sys.stdin = open("input09.txt", "r")
sys.stdout = open("output09.txt", "w")

head = [0, 0]
tail = [0, 0]
listPositions = [[0, 0]]
dictDirection = {
  "U": [0, 1],
  "D": [0, -1],
  "L": [-1, 0],
  "R": [1, 0]
}

for i in range(2000):
  information = input().split(" ")
  movement = [0, 0]
  movement[0] = int(information[1]) * dictDirection[information[0]][0]
  movement[1] = int(information[1]) * dictDirection[information[0]][1]
  head[0] += movement[0]
  head[1] += movement[1]

  if information[0] == "U" or information[0] == "D":
    
    if head[1] > tail[1] + 1:
      for k in range(tail[1] + 1, head[1]):
        if not [head[0], k] in listPositions:
          listPositions.append([head[0], k])
      tail[1] = head[1] - 1
      tail[0] = head[0]
          
    if head[1] < tail[1] - 1:
      for k in range(head[1] + 1, tail[1]):
        if not [head[0], k] in listPositions:
          listPositions.append([head[0], k])
      tail[1] = head[1] + 1
      tail[0] = head[0]
          
    continue

  if information[0] == "R" or information[0] == "L":

    if head[0] > tail[0] + 1:
      for k in range(tail[0] + 1, head[0]):
        if not [k, head[1]] in listPositions:
          listPositions.append([k, head[1]])
      tail[0] = head[0] - 1
      tail[1] = head[1]
          
    if head[0] < tail[0] - 1:
      for k in range(head[0] + 1, tail[0]):
        if not [k, head[1]] in listPositions:
          listPositions.append([k, head[1]])
      tail[0] = head[0] + 1
      tail[1] = head[1]
          
    continue

print(len(listPositions))
