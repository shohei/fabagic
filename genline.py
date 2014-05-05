fin = open('out.txt').readlines()
prev = ('0','0');
cur = ('0','0');
fout = open('pathline.pde','w')
fout.write('void setup(){ \n size(1000,800);\n')
for line in fin:
    arr = line.split(' ') 
    cur = (arr[0],arr[1])
    command = "line("+prev[0]+","+prev[1]+","+cur[0]+","+cur[1]+");\n"
    fout.write(command)
    prev = cur
fout.write('}')
    
fout.close()
