import sys


class matrix:

    def __init__(self, initArray):
        """Initialize a two dimensional list as a matrix"""
        for row in initArray:
            for elem in row:
                if type(elem) is not int:
                    raise TypeError

        n = len(initArray[0])
        if not all(len(x) == n for x in initArray):
            raise ArithmeticError

        self.array = initArray
        return



    def __str__(self):
        """Return a string for the array of numbers for this matrix"""
        return str(self.array)



    def __add__(self, otherMatrix):
        """Add two matricies together"""
        sameRows = (len(self.array) == len(otherMatrix.array))
        sameCols = len(self.array[0]) == len(otherMatrix.array[0])
        if not (sameCols and sameRows):
            raise ArithmeticError

        X = len(self.array)
        Y = len(self.array[0])

        retArray = [[0 for x in range(X)] for x in range(Y)]
        for row in range(X):
            for col in range(Y):
                retArray[row][col] = otherMatrix.array[row][col] + self.array[row][col]

        return matrix(retArray)



    def __sub__(self, otherMatrix):
        """Subtract two matricies"""

        newArray = otherMatrix.array

        for row in range(len(newArray)):
            for col in range(len(newArray[0])):
                newArray[row][col] *= -1

        return self.__add__(matrix(newArray))



    def __mul__(self, otherMatrix):
        if not (len(self.array[0]) == len(otherMatrix.array)):
            raise ArithmeticError






################################################################################
#                               Tests
################################################################################

M1 = matrix([[1,2],[3,4]])
M2 = matrix([[1,4],[3,5]])
M3 = M1+M2
M4 = M1-M2
print(M3)
print(M4)
