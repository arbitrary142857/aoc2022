# NOTE: REPLACE ALL OCCURENCES OF "10" WITH "T" IN INPUT


import sys

sys.stdin = open("input13.txt", "r")
sys.stdout = open("output13.txt", "w")

total2 = 0
total6 = 0

for j in range(450):
  input1 = input().split(",")

  if j % 3 == 2:
    continue
  
  runningOpen1 = 0

  open1 = 0
  
  num1 = "X"

  ### computes runningOpen's and num's ###
  for char in input1[0]:
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
  ### computes runningOpen's and num's ###

  ### checks cases in which an empty set [] appears ###
  if num1 == "X":
    total2 += 1
    total6 += 1
    continue
  ### checks cases in which an empty set [] appears ###

  ### checks cases in which num1 and num2 are not the same ###
  if num1 < 2:
    total2 += 1
    total6 += 1
    continue

  if num1 < 6:
    total6 += 1
    continue
  ### checks cases in which num1 and num2 are not the same ###
    
print((total2 + 1) * (total6 + 2))
