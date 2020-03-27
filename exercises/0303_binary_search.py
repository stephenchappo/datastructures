#!/usr/bin/env python3

def binarySearch(target, sortedLyst):
  left = 0
  right = len(sortedLyst)-1
  while left <= right:
    midpoint = (left + right) // 2
    print(f'Indexes: Left {left} Right {right} Midpoint {midpoint}')
    print(f'Values:  Left {sortedLyst[left]} Right {sortedLyst[right]} '
          f'Midpoint {sortedLyst[midpoint]}')
    if target == sortedLyst[midpoint]:
      return midpoint
    elif target < sortedLyst[midpoint]:
      right = midpoint - 1
    else:
      left = midpoint + 1
  return -1


print(binarySearch(90, [20, 44, 28, 55, 82, 66, 75, 88, 93]))
print()
print(binarySearch(44, [20, 44, 28, 55, 82, 66, 75, 88, 93]))

# Output
# Indexes: Left 0 Right 8 Midpoint 4
# Values:  Left 20 Right 93 Midpoint 82
# Indexes: Left 5 Right 8 Midpoint 6
# Values:  Left 66 Right 93 Midpoint 75
# Indexes: Left 7 Right 8 Midpoint 7
# Values:  Left 88 Right 93 Midpoint 88
# Indexes: Left 8 Right 8 Midpoint 8
# Values:  Left 93 Right 93 Midpoint 93
# -1
#
# Indexes: Left 0 Right 8 Midpoint 4
# Values:  Left 20 Right 93 Midpoint 82
# Indexes: Left 0 Right 3 Midpoint 1
# Values:  Left 20 Right 55 Midpoint 44
# 1