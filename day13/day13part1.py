# NOTE: REPLACE ALL OCCURENCES OF "10" WITH "T" IN INPUT 


import sys

sys.stdin = open("input13.txt", "r")
sys.stdout = open("output13.txt", "w")

total = 0

for j in range(150):
  input1 = input().split(",")
  input2 = input().split(",")
  
  runningOpen1 = 0
  runningOpen2 = 0
  right = 0
  wrong = 0
  i = 0
  
  while right == 0 and wrong == 0:

    open1 = 0
    open2 = 0
    
    num1 = "X"
    num2 = "X"
  
    ### computes runningOpen's and num's ###
    for char in input1[i]:
      if char == "[":
        runningOpen1 += 1
        open1 += 1
      elif char == "]":
        runningOpen1 -= 1
      else:
        if char == "T":
          num1 = 10
        else:
          num1 = int(char)
  
    for char in input2[i]:
      if char == "[":
        runningOpen2 += 1
        open2 += 1
      elif char == "]":
        runningOpen2 -= 1
      else:
        if char == "T":
          num2 = 10
        else:
          num2 = int(char)
    ### computes runningOpen's and num's ###
  
    ### checks cases in which an empty set [] appears ###
    if num1 == "X" and num2 == "X":
      if open1 > open2:
        wrong = 1
        continue
      if open1 < open2:
        right = 1
        continue
  
    elif num1 == "X":
      right = 1
      continue
  
    elif num2 == "X":
      wrong = 1
      continue
    ### checks cases in which an empty set [] appears ###
  
    ### checks cases in which num1 and num2 are not the same ###
    if num1 > num2:
      wrong = 1
      continue
    if num1 < num2:
      right = 1
      continue
    ### checks cases in which num1 and num2 are not the same ###
  
    ### checks the other case by comparing runningOpen's ###
    if runningOpen1 > runningOpen2:
      wrong = 1
    if runningOpen1 < runningOpen2:
      right = 1
    ### checks the other case by comparing runningOpen's ###

    i += 1

  input()
  if right == 1:
    total += j + 1

print(total)
