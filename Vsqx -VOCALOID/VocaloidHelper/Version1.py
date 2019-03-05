#!/usr/bin/env python 
#-*- coding: utf8 -*- 
import re 

errorNum = 0
try:
    try:
        inp = 0.75
    except Exception as e:
        print("Error in Part0: "+str(e))
        errorNum = errorNum+1

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

    try:
        vsqx = input("Vsqx File: ").replace('"', "").replace("\\", "/")
        inp = float(input("Stretch Parameter (Recommand to input 0.75 here):"))
        vsqxFile = vsqx
        extend = 1/inp
        #vsqx = "test.vsqx"
        whole = 0
        i = 0
        newVsqx = ""
    except Exception as e:
        print("Error in Part1: "+str(e))
        errorNum = errorNum+1

    try:
        for line in vsqx:  
            whole = whole+1
    except Exception as e:
        print("Error in Part2: "+str(e))
        errorNum = errorNum+1

    try:
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
    except Exception as e:
        print("Error in Part3: "+str(e))
        errorNum = errorNum+1

    try:
        file_put_contents(vsqxFile+".new.vsqx", newVsqx)
    except Exception as e:
        print("Error in Part4: "+str(e))
        errorNum = errorNum+1
except Exception as e:
    print("Unexpected Error: "+str(e))
    errorNum = errorNum+1
print("\n-------------------")
resS = "Success."
if(errorNum>0):
    resS = str(errorNum)+" error(s) happenned."
print(resS)
try:
    print("File save in "+vsqxFile+".new.vsqx")
except Exception as e:
    pass
print("Coding By @Lazy_Lazy_Man, open source code (Python3): https://github.com/xiawenke/MyCodes/tree/master/Vsqx%20-VOCALOID/VocaloidHelper")
input(" Press Enter go on...")
