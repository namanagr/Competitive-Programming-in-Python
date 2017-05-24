#!/usr/bin/python
'''
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10
'''

matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]

def sumRegion(r1,c1,r2,c2):
    sum = 0
    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
           sum += matrix[i][j]
    return sum

def update(r,c,val):
    matrix[r][c] = val

if __name__ == "__main__":
    print sumRegion(2,1,4,3)
    update(3,2,2)
    print sumRegion(2,1,4,3)
