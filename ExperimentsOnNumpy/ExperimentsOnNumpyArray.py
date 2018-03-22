import numpy as np

# Numpy array (1 dimensional)
NumpyArray = np.array([1,2,3])

print("Numpy Array is", NumpyArray)


# Numpy array indexing. Get second element
# Indexing starts from 0
SecondElement = NumpyArray[1]
print("Second Element of numpy array is", SecondElement)

# Array Slicing
# Get first 2 elements of the array
FirstTwoElementsOfNumpyArray = NumpyArray[:2]
print("First 2 elements of numpy array", FirstTwoElementsOfNumpyArray)

# Negative indexing
# Last element of numpy array
LastElementOfNumpyArray = NumpyArray[-1]
print("Last element of numpy array", LastElementOfNumpyArray)


# Numpy 2 dimensional array
Numpy2DArray = np.array([[1,2],[3,4]])

# Print numpy 2D array
print("Numpy 2D array", Numpy2DArray)

# Shape of array
ShapeOf2DArray = np.shape(Numpy2DArray)
ShapeOf1DArray = np.shape(NumpyArray)

print("Shape of 1D array", ShapeOf1DArray)
print("Shape Of 2D array", ShapeOf2DArray)

# Array slicing 2D Array

# Get first row of 2D array
FirstRow_Numpy2DArray = Numpy2DArray[0,:]
print("First row of numpy 2D array", FirstRow_Numpy2DArray)

# Get First column of numpy 2D array
FirstColumn_Numpy2DArray = Numpy2DArray[:,0]
print("First column numpy 2D array", FirstColumn_Numpy2DArray)
