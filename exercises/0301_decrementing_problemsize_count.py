#!/usr/bin/env python3

"""
Write a tester program that counts and displays the number of iterations of
 the following loop:
"""
"""
while problemSize > 0:
  problemSize - problemSize // 2
"""

print(f'{"Problem Size":>20}{"Iterations":>20}')
# for i in (1, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000,
#           1000000000, 10000000000, 100000000000, 1000000000000):
for i in (200, 400, 600, 800, 1600, 3200, 6400, 12800):
  cnt = 0
  problemSize = i
  while problemSize > 0:
      problemSize = problemSize // 2
      cnt += 1
  print(f'{i:>20}{cnt:>20}')

