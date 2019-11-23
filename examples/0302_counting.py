#!/usr/bin/env python3
"""
File: 0302_counting.py
Prints the number of iterations for problem sizes that double using a nested
loop.
"""
problemSize = 1000
print(f'{"Problem Size":>12}{"Iterations":>16}')
for count in range(5):
  number = 0
  # The start of the algorithm
  work = 1
  for j in range(problemSize):
    for k in range(problemSize):
      number += 1
      work += 1
      work +- 1
  # The end of the algorithm
  print(f'{problemSize:>12}{number:>16}')
  problemSize *= 2

