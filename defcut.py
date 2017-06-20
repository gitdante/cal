import os
import subprocess
import re


def cut(path,a,b,c,d,tag,ref=None):
    command = 'gdal_translate -projwin '+str(a)+' '+str(b)+' '+str(c)+' '+str(d)+' '
    d=[]
    for root,dirn,files in os.walk(path):
        for file in files:
            if '.tif'in file:
                d.append(root+'/'+file)

    if ref!=None:
        d = filter(lambda x: re.match(ref,x), d)
# l = filter(lambda x: 'end' in x,l)
    print d

    for i in d:
        cmd = command + i + ' ' + str(tag) + i.split('/')[-1]
        proc = subprocess.Popen(cmd, cwd=path, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                                stderr=subprocess.STDOUT, universal_newlines=False)
        for line in iter(proc.stdout.readline, ''):
            print(line)
        proc.wait()

cut('H:\cutsong', 336980.930, 4762755.642,746980.930, 4162755.642,'la')