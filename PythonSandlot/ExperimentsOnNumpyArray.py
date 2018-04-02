import numpy as np
from numpy import dtype



def fnNumpy2DArrayTraversal():
    numpy2DArray = np.array([[1,2, 3], [4,5,6]])
    rows = numpy2DArray.shape[0]
    cols = numpy2DArray.shape[1]
    print("rows - ", rows, "cols - ", cols)
    
    for row in range(rows):
        for col in range(cols):
            print("element [{row}, {col}] is {element}".format(row = row, col=col, element=numpy2DArray[row, col]))
    return
    
def fnExpOnNumpyArray():
    ''' Numpy array (1 dimensional) '''
    NumpyArray = np.array([1,2,3])
    
    print("Numpy Array is", NumpyArray)
    
    ''' Numpy array indexing. Get second element
     Indexing starts from 0'''
    SecondElement = NumpyArray[1]
    print("Second Element of numpy array is", SecondElement)
     
    ''' Array Slicing 
     Get first 2 elements of the array'''
    FirstTwoElementsOfNumpyArray = NumpyArray[:2]
    print("First 2 elements of numpy array", FirstTwoElementsOfNumpyArray)
     
    ''' Negative indexing
    Last element of numpy array'''
    LastElementOfNumpyArray = NumpyArray[-1]
    print("Last element of numpy array", LastElementOfNumpyArray)
    
    ''' Numpy 2 dimensional array '''
    Numpy2DArray = np.array([[1,2],[3,4]])
    
    ''' Print numpy 2D array '''
    print("Numpy 2D array", Numpy2DArray)

    ''' Shape of array '''
    ShapeOf2DArray = np.shape(Numpy2DArray)
    ShapeOf1DArray = np.shape(NumpyArray)
    
    print("Shape of 1D array", ShapeOf1DArray)
    print("Shape Of 2D array", ShapeOf2DArray)
    
    ''' Array slicing 2D Array
    
     Get first row of 2D array '''
    FirstRow_Numpy2DArray = Numpy2DArray[0,:]
    print("First row of numpy 2D array", FirstRow_Numpy2DArray)
    
    ''' Get First column of numpy 2D array '''
    FirstColumn_Numpy2DArray = Numpy2DArray[:,0]
    print("First column numpy 2D array", FirstColumn_Numpy2DArray)
    
    return


def fnExpOnNumpy_ND_Array():
    ''' Numpy ND array '''
    NumpyMultiDimensionalArray = np.ndarray(shape=(2,2,2), dtype=np.float)
    print("\n\nNumpy nd array with shape (2,2,2\n", NumpyMultiDimensionalArray)
    
    ''' Take two 2x2 matrices and assign them to the nd array '''
    A_2_2 = np.array([[1,2], [3,4]])
    B_2_2 = np.array([[5,6], [7,8]])
    
    NumpyMultiDimensionalArray[0, :, :] = A_2_2
    NumpyMultiDimensionalArray[1, :, :] = B_2_2
    
    print("Numpy nd array(2,2,2) after assigning the values\n", NumpyMultiDimensionalArray)
    
    ''' Access second column of second matrix '''
    SecondColOfSecondMatrix = NumpyMultiDimensionalArray[1, :, 1]
    print("Second column of second matrix is", SecondColOfSecondMatrix)

    return

if __name__=="__main__":
    fnExpOnNumpyArray()
    fnExpOnNumpy_ND_Array()
    fnNumpy2DArrayTraversal()
    
    