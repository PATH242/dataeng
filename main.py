from pathlib import Path
import csv
import os
from collections import namedtuple

first_names= [("tst","test")]
last_names= [("tst","test")]
birthts_list = [("tst","test")]
imagePaths = [("tst","test")]
folderPath = Path('02-src-data')
with open("processed_data.csv",'w') as outputFile:
    csvWriter = csv.writer(outputFile, delimiter=',')
    outputFileHeader = "user_id , first_name, last_name, birthts, img_path"
    csvWriter.writerow([outputFileHeader]) #the header
    for item in folderPath.glob('**/*'):
        userID = item.name
        if item.suffix == '.csv':
            with open(item, 'r') as csvFile:
                csvRearder = csv.reader(csvFile)
                next(csvRearder)  # to skip the first line
                line = next(csvRearder)
                first_name = line[0]
                last_name = line[1]
                birthts = line[2]
                first_names.append((userID, first_name))
                last_names.append((userID, last_name))
                birthts_list.append((userID, birthts))
        else:
            imagePath = Path.resolve(item)
            imagePaths.append((userID, imagePath))
    first_names.sort()
    last_names.sort()
    birthts_list.sort()
    imagePaths.sort()
    for i in range(100):
        j = i + 1
        ID = 1000 + i
        line = (str(ID) + "," + first_names[j][1] + "," + last_names[j][1] + "," + birthts_list[j][1] + "," + str(
            imagePaths[j][1]))
        csvWriter.writerow([line])