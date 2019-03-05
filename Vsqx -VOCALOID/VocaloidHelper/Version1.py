#!/usr/bin/env python 
#-*- coding: utf8 -*- 
import re 
   
inp = 0.75
extend = 1/inp

def xmlTag(string):
    ret = re.search("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>", string)
    try:
        res = ret.group('tag_name')
    except Exception as err:
        res = False
    return(res)

def xmlVal(string):
    p = re.compile('<[^>]+>') 
    return(p.sub("", string))

def file_put_contents(filename, text):
    fileHandle = open (filename, 'w')
    fileHandle.write (text) 
    fileHandle.close() 

def clearLast(string):
    string = str(round(string))
    if("." in string):
        return(clearLast(string[:-1]))
    else:
        return(string)

#vsqx = input("Vsqx File: ").replace('"', "").replace("\\", "/")
vsqx = "test.vsqx"
whole = 0
i = 0
newVsqx = ""

for line in vsqx:  
    whole = whole+1

oldPlayt = 0
newPlayt = 0
vsqx = open("test.vsqx")
for line in vsqx:   
    i = i+1
    if(xmlTag(line) == "dur"):
        if(oldPlayt < 0 or newPlayt < 0):
            print("error: invalid PlayTime!")
            #break
        newVal = "<"+xmlTag(line)+">"+clearLast(int(xmlVal(line))*extend)+"</"+xmlTag(line)+">\n"

    elif(xmlTag(line) == "t" and ("tempo" in line) == False):
        newVal = "<"+xmlTag(line)+">"+clearLast(int(xmlVal(line))*extend)+"</"+xmlTag(line)+">\n"

    elif(xmlTag(line) == "playTime"):
        newVal = "<"+xmlTag(line)+">"+clearLast(int(xmlVal(line))*extend)+"</"+xmlTag(line)+">\n"
    else:
        pass
        newVal = line
    
    newVsqx = newVsqx+newVal

file_put_contents("C:/Users/FrankXia/Documents/Python Scripts/VocaloidHelper/result.vsqx", newVsqx)
