from six.moves import cPickle as pickle
import matplotlib.pyplot as plt
import imageio



def fnReadAPickleFile(pickleFile):
    with open(pickleFile, "rb") as pickleFileObj:
        imageData = pickle.load(pickleFileObj)
     
    print("Size of image data", imageData.size)
    print("Shape of image data", imageData.shape)
    
    return imageData
    

def fnSerializeImageData(imageFile):
    ''' read image file '''
    imageData = imageio.imread(imageFile)
    
    ''' Dump image data into a pickle file '''
    OutputFile = 'TestImage.pickle'
    with open(OutputFile, 'wb') as f:
        pickle.dump(imageData, f, pickle.HIGHEST_PROTOCOL)
        
    return

def fnDisplayAnImage(imageArray):
    plt.imshow(imageArray)
    plt.show()

    return
    

if __name__=="__main__":
    pickleFile = "/home/kapil/Workspace/Udacity/DeepLearning_Google/tensorflow/tensorflow/examples/udacity/notMNIST_large/A.pickle"
    fnReadAPickleFile(pickleFile)
    
    imageFile = "/home/kapil/Workspace/Udacity/DeepLearning_Google/tensorflow/tensorflow/examples/udacity/notMNIST_large/A/Q2luZGVyZWxsYS5vdGY=.png"
    fnSerializeImageData(imageFile)
    
    ''' Read the test image pickle file created in the step above and display it'''
    pickleFile = 'TestImage.pickle'
    imageData = fnReadAPickleFile(pickleFile)
    
    fnDisplayAnImage(imageData)