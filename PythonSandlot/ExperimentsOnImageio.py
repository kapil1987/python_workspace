import imageio
import matplotlib.pyplot as plt
import numpy as np

''' Load an image file '''

def fnLoadAnImageFile(pathToImageFile):
    imageData = imageio.imread(pathToImageFile)
    return imageData


def fnShowAnImage(imageArray):
    plt.imshow(imageArray)
    plt.show()
    return

def fnHighlightImageBorder(imageArray):
    numRows = imageArray.shape[0]
    numCols = imageArray.shape[1]
    newImage = np.ndarray(shape=(28,28), dtype=float)
    
    prevVal = -1
    averagedVal = 0
    
    for row in range(numRows):
        for col in range(numCols):
            currentVal = imageArray[row, col]
            if (-1 != prevVal):
                averagedVal = (currentVal +  prevVal)/2
            else:
                averagedVal = currentVal
            
            newImage[row, col] = averagedVal
                
            prevVal = currentVal
            
    fnShowAnImage(newImage)
            
    return

if __name__=="__main__":
    imageData = fnLoadAnImageFile("/home/kapil/Workspace/Udacity/DeepLearning_Google/tensorflow/tensorflow/examples/udacity/notMNIST_small/A/SVRDIEF2YW50IEdhcmRlIERlbWkgT2JsaXF1ZSBTV0EudHRm.png")
    print("imageData type", type(imageData))
    print("imageData shape", imageData.shape)
    fnShowAnImage(imageData)
    
    fnHighlightImageBorder(imageData)
    
    