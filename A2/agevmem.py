import json
import os.path
import time
import datetime
from pprint import pprint
holdx=0
holdy=0
holdz=0
f = open('outputfile.txt', 'w+')
for item in list(range(1060)):
    JIsFile=os.path.isfile("json/data"+str(item)+".json")
    CIsFile=os.path.isfile("CarbonDateJSON/"+str(item)+".json")
    if(JIsFile and CIsFile):
        data1 = json.load(open('json/data'+str(item)+'.json'))
        data2 = json.load(open('CarbonDateJSON/'+str(item)+'.json'))
        if(data2["estimated-creation-date"] != ""):
            now = datetime.datetime.now()
            bdate = datetime.datetime.strptime(data2["estimated-creation-date"], '%Y-%m-%dT%H:%M:%S')
            print(str((now-bdate).days) + " Days with " + str(len(data1["mementos"]["list"]))+ " Mementos, ID: " + str(item))
            f.write(str((now-bdate).days) + " " +str(len(data1["mementos"]["list"])) + "\n")
    if(JIsFile):
        holdy = holdy + 1
        data = json.load(open('json/data'+str(item)+'.json'))
    if(CIsFile):
        holdx = holdx + 1
        data = json.load(open('CarbonDateJSON/'+str(item)+'.json'))
        if(data["estimated-creation-date"] != ""):
            holdz = holdz + 1
print("Number of sites: " + str(holdx))
print("With Estimted Dates of Creation: " + str(holdz))
print("With Mementos: "+ str(holdy))
