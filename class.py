import matplotlib.pyplot as plt
from osgeo import gdal
import numpy as np
import os
import re


class vali:
    path = dict(s=r'H:\cutsong',
            w=r'H:\aboutgcp\modi',
            lucc=r'H:\aboutgcp\lucc.tif',
            region=r'H:\aboutgcp\region2.tif'
                )
    missing=np.zeros((600,410))

    #use re to filter
    def __init__(self,skey,wkey):
        self.sname=[x for x in os.listdir(self.path['s']) if re.match(skey,x)]
        self.wname=[x for x in os.listdir(self.path['w']) if re.match(skey,x)]
        self.lucc=self.readdata(self.path['lucc'])
        self.type=np.unique(self.lucc)
        self.region=self.readdata(self.path['lucc'])

    def readdata(self,path):
        fid = gdal.Open(path, gdal.GA_ReadOnly)
        data = fid.GetRasterBand(1).ReadAsArray()
        return data

    def findmissing(self):


    def getmonth(self):


    def getall(self):


    def getperson(self):


    def pltwithlucc(self):


    def pltwithregion(self):


d = vali('^la', '.tif')
print d.sname
print d.wname