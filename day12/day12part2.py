import sys

sys.stdin = open("input12.txt", "r")
sys.stdout = open("output12.txt", "w")

heights = []

height = 41
width = 154

for i in range(height):
  heights.append([[char] for char in input()])

for i in range(height):
  for j in range(width):
    if heights[i][j][0] == "S":
      start = [i, j]
    if heights[i][j][0] == "E":
      end = [i, j]

heights[end[0]][end[1]].append(0)
heights[start[0]][start[1]][0] = "a"
heights[end[0]][end[1]][0] = "z"

distance = 0
while len(heights[start[0]][start[1]]) == 1:

  # iterate through all locations
  for i in range(height):
    for j in range(width):

      # check if this location was "recently" reached
      if len(heights[i][j]) == 2:
        if heights[i][j][1] == distance:

          index = ord(heights[i][j][0]) - 97

          # check up
          if i > 0:
            if len(heights[i - 1][j]) == 1 and ord(heights[i - 1][j][0]) - 97 >= index - 1:
              heights[i - 1][j].append(distance + 1)

          # check down
          if i < height - 1:
            if len(heights[i + 1][j]) == 1 and ord(heights[i + 1][j][0]) - 97 >= index - 1:
              heights[i + 1][j].append(distance + 1)

          # check left
          if j > 0:
            if len(heights[i][j - 1]) == 1 and ord(heights[i][j - 1][0]) - 97 >= index - 1:
              heights[i][j - 1].append(distance + 1)

          # check right
          if j < width - 1:
            if len(heights[i][j + 1]) == 1 and ord(heights[i][j + 1][0]) - 97 >= index - 1:
              heights[i][j + 1].append(distance + 1)

  distance += 1

maximum = 9999999

for i in range(height):
  for j in range(width):
    if len(heights[i][j]) == 2:
      if heights[i][j][0] == "a":
        if heights[i][j][1] < maximum:
          maximum = heights[i][j][1]

print(maximum)
