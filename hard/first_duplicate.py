"""
You need to create a method to identify the first duplicate integer in an array of numbers.

For example:
    |   input   |   output  |
    |[1,2,1,2,3,3]| 1   |
    |[2,1,3,5,3,2]| 3   |
    |[1,2,3,4,5,6]| -1  |

for inputs in which there are no duplicates just return '-1'.

1 - yeah brute force try a for and a count
2 - but what about pointers? we could use 2 pointers to pinpoint the pivot and just find a possible second duplicate
3 - 
"""

def firstDuplicate(input):


a = [1,2,1,2,3,3]

print(firstDuplicate(a))