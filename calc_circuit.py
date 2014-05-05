fin = open('out.txt')
array = []
vec = {'x':[],'y':[]}

for line in fin:
    x = int(line.split(' ')[0])
    y = int(line.split(' ')[1])
    vec['x'].append(x)
    vec['y'].append(y)

#print vec
v_x = vec['x']
v_y = vec['y']

hit = {'x':[],'y':[]}
for x in v_x:
    if x in v_x:
        #print v_x.index(x)
        hit['x'].append(v_x.index(x))
for y in v_y:
    if y in v_y:
        #print v_y.index(y) 
        hit['y'].append(v_y.index(y))

#print hit
indices = []
for x in hit['x']:
    if x in hit['y']:
        index = hit['x'].index(x)
        indices.append(index)
indices.sort()
indices = list(set(indices))
print indices

#anchors = []
#for a in array:
#    temp = array.pop(array.index(a))
#    if a in temp:
#        print "detected: "+a
#        anchors.append(a)
#
#
#print anchors

