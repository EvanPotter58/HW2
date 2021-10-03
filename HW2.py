import csv
import json
import xml.etree.ElementTree as xml
import re

response = input("What type of format do you want you file to covert it to? \n -c = CSV \n -j = JSON \n -x = XML\n")
if response == "-c":
    txt_file = r"NFL Offensive Player stats, 1999-2013.txt"
    csv_file = r"NFL Stats.csv"
    in_file = csv.reader(open(txt_file,"r"),delimiter = "\t")
    out_file = csv.writer(open(csv_file, "w"))
    out_file.writerows(in_file)
elif response == "-j":
    dict = {}
    with open('NFL Offensive Player stats, 1999-2013.txt') as File:
        command = File.readline().split("\t")
        length = len(command)
        dNum = 1
        for line in File:
            dict['Dict' + str(dNum)] = {}
            description = line.split("\t")
            for i in range(length):
                dict['Dict' + str(dNum)][command[i]] = description[i]
            dNum = dNum + 1
    outFile = open("NFL Offensive Player stats, 1999-2013.json", "w")
    json.dump(dict, outFile, indent=4, sort_keys=False)
    outFile.close()
elif response == "-x":
    file = open('NFL Offensive Player stats, 1999-2013.txt', "r")
    fileContent = file.read()
    fileArray = fileContent.split("\n")
    keys = []
    for i in range(len(fileArray)):
        if i == 0:
            keys = fileArray[i].split("\t")
    for i in range(len(keys)):
        keys[i] = re.sub("[^a-zA-Z]", "_", keys[i])
    xml = "<Results>"
    for i in range(len(fileArray)):
        if i > 0:
            xml += "<Result>"
            arr = fileArray[i].split("\t")
            for j in range(len(arr)):
                xml += "<" + keys[j] + ">" + arr[j] + "</" + keys[j] + ">"
            xml += "</Result>"
    xml += "</Results>"
    f = open("test.xml", "w")
    f.write(xml)
    f.close()