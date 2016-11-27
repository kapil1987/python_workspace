# -*- coding: utf-8 -*-

import sys
import simplekml
import math

TRUE = 1
FALSE = 0

'''
\fn ReadLatLongFile(pathOfFile)

\details Read the file whose full path is provided as argument to the function
and return the list of all the lines raed.
If latitude and longitude are in radians then the second argument of the 
function - angle_in_rads is set to TRUE else it is set to FALSE 

\param [in] pathOfFile Full path of file from where to read the latitude and longitude
                       values
                       
\param [in] angle_in_rads set to TRUE if latitude and longitude are in radians else 
                          set to FALSE
                       
\returns List of latitude, longitude strings
'''

def ReadLatLongFile(pathOfFile, angle_in_rads):
    ListOfLatLongs = []
    with open(pathOfFile,'r') as LatLongFileObj:
        for line in LatLongFileObj:
            lat, long = line.split(",")
            latitudeFloat = float(lat)
            longitudeFloat = float(long)
            if (TRUE == angle_in_rads):
                assert(((math.pi/2) > latitudeFloat) and (-(math.pi/2) < latitudeFloat))
                assert((math.pi > longitudeFloat) and (-(math.pi) < longitudeFloat))
            else:
                assert((90 > latitudeFloat) and (-90 < latitudeFloat))
                assert ((180 > longitudeFloat) and (-180 < longitudeFloat))
            
            ListOfLatLongs.append(line)
    return ListOfLatLongs

'''
\fn CreateKMLFromListOfLatLongStrings(LatLongKML, ListOfLatLongStrings)

\brief Add all the points (Latitude and longitude pair) listed in argument
'ListOfLatLongStrings' to the simplekml object provided as first argument to
the function

\param [in] ListOfLatLongStrings List of latitude and longitude strings
\param [out] LatLongKML simplekml object to which latitude and longitude values from
                        'ListOfLatLongStrings' will be added to
\returns None
'''    
def CreateKMLFromListOfLatLongStrings(LatLongKML, ListOfLatLongStrings):
    LengthOfListofLatLongStrings = len(ListOfLatLongStrings)
    for i in range(LengthOfListofLatLongStrings):
        lat,long = ListOfLatLongStrings[i].split(",")
        kml_point = LatLongKML.newpoint(name = "", coords = [(long, lat)])
        kml_point.style.labelstyle.color = simplekml.Color.red  # Make the text red
        kml_point.style.labelstyle.scale = 2  # Make the text twice as big
        kml_point.style.iconstyle.scale = 5
        kml_point.style.iconstyle.color = "red"
   #     kml_point.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png'
    
def usage(ProgName):
    print("usage: \n\t")
    print(ProgName, "<Full path of the lat-long file to read> <Full path(with name) of the output KML file to save>")
    print("\n")
    sys.exit(1)

if __name__ == "__main__":
    if (3 != len(sys.argv)) :
        usage(sys.argv[0])
        
    inputLatLongFile = sys.argv[1]
    outputKMLFile = sys.argv[2]
    
    LatLongKML = simplekml.Kml()    
    ListOfLatLongs = ReadLatLongFile(inputLatLongFile, 0)
    
    CreateKMLFromListOfLatLongStrings(LatLongKML, ListOfLatLongs)
    LatLongKML.save(outputKMLFile)

    