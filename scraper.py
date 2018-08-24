#/usr/bin

import re

# place KML style coordinates in JSON LngLat object
def formatCoordinates(coordinates): 
	coords = coordinates.split(",0")
	formattedCoords = ""
	i = 0
	while i  < len(coords):
		values = coords[i]
		values = values.replace("\n\t\t\t\t\t\t", "")
		values = values.split(",")
		i += 1
		if len(values) > 1:
	 		formattedCoords += "{\n\t\tlat: " + values[1] + ",\n\t\tlng: " + values[0] + "\n\t}, "
	return formattedCoords[:-2]

# third command line argument should be kml file name
file_object = open(sys.argv[2], "r")
data = file_object.read()
regexNames = r"<name>([\s\S]*?)</name>"
regexCoordinates = r"<coordinates>([\s\S]*?)</coordinates>"
matches =re.findall(regexNames, data, flags=0)
coordinateMatches = re.findall(regexCoordinates, data, flags=0)
i = 0
j = 0


while(i < len(coordinateMatches)):
	name = ""
	coord = ""
	coord1 = ""
	if j < len(matches):
		name = matches[j]
		coord = formatCoordinates(coordinateMatches[i])
		#place values in json objects
		if " " not in name:
			print(name + ": {\n\tcoords:[" + coord + "]},") 
		else:
			print("\"" + name + "\"" + ": {\n\tcoords:[" + coord + "]},") 

	i += 1
	j += 1







