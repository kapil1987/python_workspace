# -*- coding: utf-8 -*-

'''
Read a lat long file whose path is provided as an argument and
return a list of the lat-long
'''
import simplekml

def ReadLatLongFile(pathOfFile):
    with open(pathOfFile,'r') as LatLongFileObj:
        ListOfLatLongs = LatLongFileObj.readlines()
    return ListOfLatLongs
    
def CreateKMLFromListOfLatLongStrings(LatLongKML, ListOfLatLongStrings):
    LengthOfListofLatLongStrings = len(ListOfLatLongStrings)
    for i in range(LengthOfListofLatLongStrings):
        lat,long = ListOfLatLongStrings[i].split(",")
        kml_point = LatLongKML.newpoint(name = "", coords = [(long, lat)])
        kml_point.style.labelstyle.color = simplekml.Color.red  # Make the text red
        kml_point.style.labelstyle.scale = 2  # Make the text twice as big
        kml_point.style.iconstyle.scale=10
        kml_point.style.iconstyle.color="red"
        kml_point.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png'
    

if __name__ == "__main__":
    pathOfFile = '/home/kapil/SpyderWorkspace/ExperimentsOnSimpleKML/LatLongFiles/LatLongFile1.txt'
    LatLongKML = simplekml.Kml()    
    ListOfLatLongs = ReadLatLongFile(pathOfFile)
    CreateKMLFromListOfLatLongStrings(LatLongKML, ListOfLatLongs)
    LatLongKML.save("/home/kapil/SpyderWorkspace/ExperimentsOnSimpleKML/Points.kml")

    