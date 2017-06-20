from osgeo import gdal
import numpy as np
import os
import subprocess


path = r"H:\warped\ratio"
l = os.listdir(path)
# l = filter(lambda x: 'end' in x,l)
command = 'gdal_translate -projwin 336980.930 4762755.642 746980.9300000002 4162755.642 '
print l

for i in l:
    cmd = command + i + ' ' + 'cut' + i
    proc = subprocess.Popen(cmd, cwd=path, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                            stderr=subprocess.STDOUT, universal_newlines=False)
    for line in iter(proc.stdout.readline, ''):
        print(line)
    proc.wait()
