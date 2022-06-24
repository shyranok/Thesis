"""
Categorizes a directory with images into sub directories based on filename.
"""

import os
import shutil
import sys

#Make sure the program is used properely
if len(sys.argv) < 3:
    exit()

#Create dictionaries for demographics
sexes = {
    '0': 'male',
    '1': 'female'
}

ethnicities = {
    '0': 'white',
    '1': 'black',
    '2': 'asian',
    '3': 'indian',
    '4': 'other'
}

#Function for dividing age groups in different classes
def ageCategory(age):
    if age < 27:
        return 0

    if age < 35:
        return 1

    if age < 51:
        return 2

    return 3

#Path to data
path = sys.argv[1] 
#Path to where the new folders should be stored
newBasePath = sys.argv[2]
#See all image filenames
files = os.listdir(path)
#Split according to filename in subdirectories 
#Code from https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory & https://realpython.com/python-assert-statement/ 
for filename in files:
    filePath = path + filename #What does this command do? path + 2_1_3_201710125.png? 
    if os.path.isfile(filePath):
        splitFilename = filename.split('_')

        #First argument is age, second is sex (0 = male, 1 = female)
        #Third is ethnicity (0 = white, 1 = black, 2 = asian, 3 = indian, 4 = other)
        try:
            if len(splitFilename) != 4:
                raise ValueError('Filename should consist of 4 parts')

            newFilePath = newBasePath + '/'
            newFilePath += sexes[splitFilename[1]] + '/'
            newFilePath += ethnicities[splitFilename[2]] + '/'
            newFilePath += str(ageCategory(int(splitFilename[0])))
        except:
            newFilePath = newBasePath + '/uncategorized/'

        os.makedirs(newFilePath, exist_ok = True) 
        shutil.copyfile(filePath, newFilePath + '/' + filename) #code from https://stackoverflow.com/questions/123198/how-to-copy-files
