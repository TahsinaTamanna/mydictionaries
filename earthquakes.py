"""
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries

1) print out the number of earthquakes

2) iterate through the dictionary and extract the location, magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a 
   magnitude > 6. Print out the new dictionary.

3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

"""


import json

infile = open("eq_data.json", "r")

eqs = json.load(infile)
print(type(eqs))

# number of earthquakes

print(len(eqs["features"]))

# creating and printing eq_dict
eq_dict = {}
for i in eqs["features"]:
    if i["properties"]["mag"] > 6:
        eq_dict["Location"] = i["properties"]["place"]
        eq_dict["Magnitude"] = i["properties"]["mag"]
        eq_dict["Longitude"] = i["geometry"]["coordinates"][0]
        eq_dict["Latitude"] = i["geometry"]["coordinates"][1]
        print(eq_dict)

# formatted print
for i in eqs["features"]:
    for k, v in eq_dict.items():
        print(k, " : ", v)
    print()
