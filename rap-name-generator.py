# Guided Exploration No. 3
# Chris Grasser

# importing the random library
import random

# empty list to store future rap names
possible_names = []

# open the file for the rap names
outputFile = open('rap-names-output.txt', 'w')

# open file for reading assign it handle of dataFile
with open('rap-names.txt', 'r') as dataFile:
    # iterate through each line in the file
    for name in dataFile:
        # remove line feed at end with .rstip()
        possible_names.append(name.rstrip())

# get number of rap names to generate
count = int(input('How many rap names would you like to create? '))
# get number of parts the name should contain
parts = int(input('How many parts should the name contain? '))

# loop to make specified number of rap names
for i in range(count):
    # list to hold rap name parts
    name_parts = []
    # loop to generate the name parts
    for j in range(parts):
        # generate parts ranodmly and append them to list
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])
    # write the name to the dataFile handle
    outputFile.write(f"{' '.join(name_parts)}\n")
    # print the rap names
    print(f"{' '.join(name_parts)}")

# close the file
outputFile.close()
