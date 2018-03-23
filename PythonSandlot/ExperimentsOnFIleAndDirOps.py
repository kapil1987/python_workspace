import os


def fnRecursiveWalk(pathOfDirToTraverse):
    for root, dirs, files in os.walk(pathOfDirToTraverse):
        print(root, dirs, files)

def fnListDirContents(pathToDirToTraverse):
    for file in os.listdir(pathToDirToTraverse):
        print(file)

if __name__=="__main__":
    pathToDirToTraverse = input("provide the path of directory to traverse\n")
    print(pathToDirToTraverse)
    # fnRecursiveWalk(pathToDirToTraverse)
    fnListDirContents(pathToDirToTraverse)