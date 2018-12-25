import math
import random
import numpy as np
import matplotlib.pyplot as plt

height = 10
width = 20

def ifOnCircle1(x, y, h, w):
    midPoindx = w/4
    midPoindy = h/2
    r = h/2
    line = math.sqrt((x-midPoindx)*(x-midPoindx)+(y-midPoindy)*(y-midPoindy))
    if(line<r):
        #print(1)
        return(True)
    else:
        #print(0)
        return(False)
        
def ifOnCircle2(x, y, h, w):
    midPoindx = w*0.75
    midPoindy = h/2
    r = h/2
    
    line = math.sqrt((x-midPoindx)*(x-midPoindx)+(y-midPoindy)*(y-midPoindy))
    if(line<r):
        #print(1)
        return(True)
    else:
        #print(0)
        return(False)

def ifOnUpperTri(x, y, h, w):
    k = h/w
    y2 = k*x
    if(y2<y):
        #print(1)
        return(True)
    else:
        #print(0)
        return(False)

def ifOnLeft(x, y, h, w):
    t = w/4
    if(x<t):
        #print(1)
        return(True)
    else:
        #print(0)
        return(False)
        
def ifOnUpper(x, y, h, w):
    t = h/2
    if(y>t):
        #print(1)
        return(True)
    else:
        #print(0)
        return(False)
times = 100000
yes = 0
show = 0
showP = times/100
rrx = []
rry = []
rrxt = []
rryt = []

for i in range(times):
    ry = random.randint(0, height*1000000000)/1000000000
    rx = random.randint(0, width*1000000000)/1000000000
    #print("["+str(rx)+","+str(ry)+"]")
    state = 0
    if(ifOnCircle1(rx, ry, height, width)):
        state = 1
    elif(ifOnCircle2(rx, ry, height, width)):
        state = 1
    elif(ifOnUpperTri(rx, ry, height, width)):
        state = 1
    elif(ifOnLeft(rx, ry, height, width)):
        state = 1
    #if(ifOnUpper(rx, ry, height, width)):
    #    state = 1
    if(state == 0):
        yes = yes+1
        rrxt = rrxt+[rx]
        rryt = rryt+[ry]
    else:
        rrx = rrx+[rx]
        rry = rry+[ry]
    show = show+1
    if(show == showP):
        show = 0
        percentage = i/times
        percentage = percentage*100
        print(str(percentage)+"%")
        #area = width*height*(yes/(i+1))
        #print(area)
        print("----------")

rrx = rrx+[width]+[0]
rry = rry+[height]+[0]
area = width*height*(yes/times)
print(area)
plt.figure()
plt.scatter(rrx,rry,c='red',s=25,alpha=1,marker='o')
plt.scatter(rrxt,rryt,c='green',s=25,alpha=1,marker='o')
plt.show()
#19.503
#ifOnUpperTri(3, 1, height, width)
