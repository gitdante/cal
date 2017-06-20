from osgeo import gdal
import numpy as np
import os
import subprocess


path = r"H:\rnwarp"
l = os.listdir(path)
#l = filter(lambda x: '.tif' in x,l)
command1 ='gdal_translate -gcp 410.500000 71.750000 670208.094229 4687792.96545 -gcp 404.250000 114.250000 670458.094229' \
          ' 4635542.96545 -gcp 354.750000 174.750000 630458.094229 4570292.96545 -gcp 315.750000 208.250000 597958.094229 ' \
          '4531292.96545 -gcp 276.750000 254.500000 568208.094229 4481292.96545 -gcp 159.250000 272.750000 468958.094229 ' \
          '4454292.96545 -gcp 218.750000 275.500000 515458.094229 4456042.96545 -gcp 191.500000 305.250000 491458.094229 ' \
          '4421042.96545 -gcp 237.250000 363.500000 531208.094229 4357542.96545 -gcp 224.500000 362.250000 522208.094229 ' \
          '4358292.96545 -gcp 372.750000 413.750000 648458.094229 4304542.96545 -gcp 317.750000 367.250000 601708.094229 ' \
          '4355042.96545 '

command2 ='gdalwarp -r bilinear -t_srs EPSG:32647 '
command3 ='gdalwarp -tr 1000 1000 -t_srs EPSG:32647 '
print l

for i in l:
    cmd = command1 + i + ' ' + 'mid' + i
    proc = subprocess.Popen(cmd, cwd=path, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                            stderr=subprocess.STDOUT, universal_newlines=False)
    for line in iter(proc.stdout.readline, ''):
        print(line)
    proc.wait()

    cmd = command2 + 'mid' + i + ' ' + 'mid2' + i
    proc = subprocess.Popen(cmd, cwd=path, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                            stderr=subprocess.STDOUT, universal_newlines=False)
    for line in iter(proc.stdout.readline, ''):
        print(line)
    proc.wait()

    cmd = command3 + 'mid2' + i + ' ' + 'end' + i
    proc = subprocess.Popen(cmd, cwd=path, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                            stderr=subprocess.STDOUT, universal_newlines=False)
    for line in iter(proc.stdout.readline, ''):
        print(line)
    proc.wait()