# -*- coding: utf-8 -*-

import unittest

import ExperimentsOnSimpleKML

class TestsForExperimentsOnSimpleKML(unittest.TestCase):
    
    def test_itShouldReadALatLongFileAndReturnListOfLatLongStrings(self):
        print("Executing test")
        pathOfFile = "/home/kapil/SpyderWorkspace/ExperimentsOnSimpleKML/LatLongFiles/LatLongFile1.txt"
        expectedOutPutList = ["13.1986, 77.7066\n", "28.556160, 77.100281"]
        ListOfLatLongStrings = ExperimentsOnSimpleKML.ReadLatLongFile(pathOfFile)
        
        self.assertListEqual(expectedOutPutList, ListOfLatLongStrings)
        print("DONE: itShouldReadALatLongFileAndReturnListOfLatLongStrings")
        
        

if __name__ == "__main__":
    print("Execute test")
    unittest.main()