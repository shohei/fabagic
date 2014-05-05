from numpy import *
from pylab import *

point = [[1,1],[3,5],[5,2]]
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

dy=0.01
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
hit_path(2.4,total_path)

#while(y < ymax):
#    hit_path = []
#    descriminate(y,total_path)
#
#    hit_path.append()
#    y = y + dy






########################################

def debugPlot():
    for p in point:
        plot(p[0],p[1],'o')
    for i in range(len(coef['a'])):
        x = arange(xmin,xmax,0.1)
        y =  coef['a'][i] * x + coef['b'][i]
        plot(x,y)
    xlim([xmin-1,xmax+1])
    ylim([ymin-1,ymax+1])
    plt.show()

debugPlot()



