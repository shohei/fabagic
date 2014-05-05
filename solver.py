from numpy import *
from pylab import *
import math

fin = open('in.path').readlines()
close_points = []
coefs = []
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

dy = 1
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
        try:
            a = (p[i+1][1] - p[i][1])*1.0/(p[i+1][0] - p[i][0])
            b = p[i][1] - a * p[i][0] 
        except:
            a = p[i+1][0] # Hey, this is foolish, but I'm inserting X value into A.
            b = "NA"
        coef['a'].append(a)
        coef['b'].append(b)
    print coef
    coefs.append(coef)    

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
            if b == "NA":
                xhit = a
            else:
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


#TODO: this is not functioning well...
def debugPlot(close_points,coefs,total_scanpath):
    #for loop for one closure
    i = 0
    g_x = []
    g_y = []
    for point in close_points:
        xvec = []
        yvec = []
        for p in point:
            plot(p[0],p[1],'o')
            xvec.append(p[0])            
            yvec.append(p[1])            
        xmax = max(xvec)
        xmin = min(xvec) 
        ymax = max(yvec) 
        ymin = min(yvec) 
        g_x.append(xmax)
        g_x.append(xmin)
        g_y.append(ymax)
        g_y.append(ymin)
    
        for j in range(len(coefs[i]['a'])):
            if coefs[i]['b'][j]=="NA":
                #y =  float(coefs[i]['a'][j]) * x + float(coefs[i]['b'][j])
                yNum = int(floor((ymax-ymin)/dy))
                yk = ymin
                ylist = []
                xlist = []
                for k in range(yNum):
                    ylist.append(y)
                    xlist.append(xmin)
                    yk = yk + dy
                y = array(ylist)
                x = array(xlist)
            else:
                x = arange(xmin,xmax,0.1)
                y =  float(coefs[i]['a'][j]) * x + float(coefs[i]['b'][j])
            plot(x,y)

    for scanpath in total_scanpath:
        for s in scanpath:
            x = s[0]
            y = s[1]
            plot(x,y,'o')

    g_xmin = min(g_x)
    g_xmax = max(g_x)
    g_ymin = min(g_y)
    g_ymax = max(g_y)

    xlim([g_xmin-1,g_xmax+1])
    ylim([g_ymin-1,g_ymax+1])
    plt.show()

#debugPlot(close_points,coefs,total_scanpath)

