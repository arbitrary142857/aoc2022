import sys

sys.stdin = open("input07.txt", "r")
sys.stdout = open("output07.txt", "w")

dictDirectories = {}

path = [] # shows current /a/b/c/etc. path

for i in range(1109):
  
  information = input().split(" ")

  # "$ cd" CASE
  if information[0] == "$" and information[1] == "cd":

    # renaming to avoid duplicate ambiguity
    if information[2] in dictDirectories.keys():
      information[2] = information[2] + str(i) 

    if information[2] == "..":
      path = path[:-1]
      continue

    path.append(information[2])

    dictDirectories[information[2]] = 0
    continue

  # "$ ls" CASE
  if information[0] == "$" and information[1] == "ls":
    continue

  # "dir" CASE
  if information[0] == "dir":
    continue

  # "[num] file" CASE
  for directory in path:
    dictDirectories[directory] += int(information[0])

minimum = 70000000

for directory in dictDirectories:
  if dictDirectories[directory] > dictDirectories["/"] - 40000000 and dictDirectories[directory] < minimum:
    minimum = dictDirectories[directory]

print(minimum)
