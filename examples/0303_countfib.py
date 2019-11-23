#!/usr/bin/env python3
"""
File: 0303_countfib.py
Prints the number of calls of a recursive Fibonacci function with problem
sizes that double.
"""


class Counter(object):
  """Tracks a count."""

  def __init__(self):
    self._number = 0

  def increment(self):
    self._number += 1

  def __str__(self):
    return str(self._number)


def fib(n, cnt):
  """Count the number of calls of the Fibonacci function"""
  cnt.increment()
  if n < 3:
    return 1
  else:
    return fib(n - 1, cnt) + fib(n - 2, cnt)


problemSize = 2
print(f'{"Problem Size":>12}{"Calls":>12}')
for count in range(5):
  counter = Counter()
  # The start of the algorithm
  fib(problemSize, counter)
  # The end of the algorithm
  print(f'{problemSize:>12}{str(counter):>12}')
  problemSize *= 2
