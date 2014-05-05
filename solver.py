from numpy import *
from pylab import *
import math

fin = open('in.path').readlines()
close_points = []
i=0
close_points.append([])
for line in fin:
    print close_points[i]
    lat = line.strip().split(' ')
    #print lat
    x = int(lat[0])
    y = int(lat[1])
    if (x==-1 or y==-1):
        i += 1
        close_points.append([])
    else:
        close_points[i].append([x,y])
print 'close_points',
print close_points
print 'total closure: ',len(close_points)


def calcScanPath(close_point):
    
    #point = [[1,1],[3,5],[5,2]]
    point = close_point 
    x = []
    y = []
    for i in range(len(point)):
        x.append(point[i][0])
        y.append(point[i][1])
    xmax= max(x)
    xmin = min(x)
    ymax = max(y)
    ymin = min(y)
    coef = {'a':[],'b':[]}
    
    p = point
    p.append(p[0])
    print p
    for i in range(len(p)-1):
        print p[i],p[i+1]
        a = (p[i+1][1] - p[i][1])*1.0/(p[i+1][0] - p[i][0])
        b = p[i][1] - a * p[i][0] 
        coef['a'].append(a)
        coef['b'].append(b)
    print coef
    
    dy=0.1
    y = ymin
    total_path = int(len(point))
    print 'totalpath',
    print total_path
    
    def hit_path(y,total_path):
        hit = []
        for i in range(total_path-1):
            current_ymin = min(p[i][1],p[i+1][1])
            current_ymax = max(p[i][1],p[i+1][1])
            print current_ymin,current_ymax
            if (y > current_ymin) and (y < current_ymax):
                #hit path
                hit.append(i)
        print "hit path: ",
        print hit
        return hit
    
    
    #hit_path(1.2,total_path)
    #hit_path(2.4,total_path)
    
    scanpath = []
    while(y < ymax):
        hits = hit_path(y,total_path) 
        for h in hits:
            a = coef['a'][h]
            b = coef['b'][h]
            xhit = round((y-b)*1.0/a,3)
            y = round(y,3)
            scanpath.append([xhit,y])
        y = y + dy
    
    return scanpath


total_scanpath = []
debugDict = {'point':[],'coef':[],'xmin':[],'xmax':[],'ymin':[],'ymax':[],'scanpath':[]}
for close_point in close_points:
    scanpath = calcScanPath(close_point)
    total_scanpath.append(scanpath)
    debugDict


def debugPlot(point,coef,xmin,xmax,ymin,ymax,scanpath):
    for p in point:
        plot(p[0],p[1],'o')
    for i in range(len(coef['a'])):
        x = arange(xmin,xmax,0.1)
        y =  coef['a'][i] * x + coef['b'][i]
        plot(x,y)
    for s in scanpath:
        x = s[0]
        y = s[1]
        plot(x,y,'o')
    xlim([xmin-1,xmax+1])
    ylim([ymin-1,ymax+1])
    plt.show()

for i in range():
    #debugPlot(debugDict['point'][i],debugDict['coef'][i],debugDict['xmin'][i],debugDict['point'][i],debugDict['point'][i],debugDict['point'][i],debugDict['point'][i],debugDict['point'][i],)

debugPlot

