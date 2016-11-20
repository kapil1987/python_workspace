# -*- coding: utf-8 -*-

import unittest

import ExperimentsOnSimpleKML

class TestsForExperimentsOnSimpleKML(unittest.TestCase):
    
    def test_itShouldReadALatLongFileAndReturnListOfLatLongStrings(self):
        print("Executing test")
        pathOfFile = "/home/kapil/workspace/python_workspace/ExperimentsOnSimpleKML/LatLongFiles/LatLongFileInDegrees.txt"
        expectedOutPutList = ["13.1986, 77.7066\n", "28.556160, 77.100281"]
        ListOfLatLongStrings = ExperimentsOnSimpleKML.ReadLatLongFile(pathOfFile, 0)
        
        self.assertListEqual(expectedOutPutList, ListOfLatLongStrings)
        print("DONE: itShouldReadALatLongFileAndReturnListOfLatLongStrings")
        
    def test_itShouldReadALatLongFileAndReturnListOfLatLongStringsInRadians(self):
        print("Executing test")
        pathOfFile = "/home/kapil/workspace/python_workspace/ExperimentsOnSimpleKML/LatLongFiles/LatLongFileInRadians.txt"
        expectedOutPutList = ["0.23035902665, 1.35623602053"]
        ListOfLatLongStrings = ExperimentsOnSimpleKML.ReadLatLongFile(pathOfFile, 1)
        
        self.assertListEqual(expectedOutPutList, ListOfLatLongStrings)
        print("DONE: itShouldReadALatLongFileAndReturnListOfLatLongStrings")
        
        

if __name__ == "__main__":
    print("Execute test")
    unittest.main()