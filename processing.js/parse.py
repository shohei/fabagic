fin = open('load.pde')
fout = open('out.pde','w')

for line in fin:
    line = line.strip()
    fout.write(line)

fout.close()
