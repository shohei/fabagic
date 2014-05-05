import os
basename = 'AgIC_Simulator'
filename = basename + '.pde'

#try:
#    os.system('rm -r '+basename)
#except Exception:
#    continue

fin = open('out.txt').readlines()
prev = ['0','0'];
cur = ['0','0'];
coord = [] 
fout = open(filename,'w')
for line in fin:
    arr = line.split(' ') 
    coord.append([arr[0],arr[1]])
fout.write('int[][] coord;\n')
fout.write('void setup(){ \n size(1000,800);\n')
for 
fout.write('coord = '+str(coord)+';\n')
fout.write('void draw(){\n')
#i=0
#for c in coord:
#    cur = (c[i][0],c[i][1])
#    command = "line("+prev[0]+","+prev[1]+","+cur[0]+","+cur[1]+");\n"
#    fout.write(command)
#    prev = cur
#    i=1
fout.write('}')
    
fout.close()
