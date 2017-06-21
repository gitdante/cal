import matplotlib.pyplot as plt
from osgeo import gdal
import numpy as np
import os
import re
import bisect


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
        self.sall=self.getall(self.path['s'],self.sname)
        self.wall=self.getall(self.path['w'],self.wname)
        self.r=self.getperson()
        self.months={str(i):self.getmonthtotal(self.sall,i) for i in range(6,10)}
        self.months={str(i):self.getmonthtotal(self.wall,i) for i in range(6,10)}
        self.seasons=np.sum(self.sall[:, :, :], axis=0)
        self.seasonw=np.sum(self.wall[:, :, :], axis=0)




    def readdata(self,path):
        fid = gdal.Open(path, gdal.GA_ReadOnly)
        data = fid.GetRasterBand(1).ReadAsArray()
        return data

    def findmissing(self,l):
        s=[re.findall('.*(\d{7})',x)[0] for x in l]
        s=set(s)
        jtos=set(['2012'+str(x) for x in range(153,275)])
        booll=['2012'+str(x) for x in range(153,275)]
        m=sorted(list(jtos - s))
        posi = [bisect.bisect(booll,x) for x in m]
        return posi

    def getmonthtotal(self,sorw,k):
        t= [31,29,31,30,31,30,31,31,30]
        return np.sum(sorw[(sum(t[:(k-1)])+1):sum(t[:k]), :, :], axis=0)


    def getall(self,p,n):
        a=[self.readdata(p+os.sep+i) for i in n]
        for i in self.findmissing(n):
            a.insert(i,self.missing)
        b=np.array(a)
        return b


    def getperson(self):
        start = 0
        end = 0
        monthdtd = []
        monthpt = []
        while end != 120:
            end += 8
            monthdtd.append(np.sum(self.sall[start:end, :, :], axis=0))
            monthpt.append(np.sum(self.wall[start:end, :, :], axis=0))
            start = end
        mmmdtd = np.array(monthdtd)
        mmmpt = np.array(monthpt)
        person = np.ones((600, 410))
        for i in range(567):
            for j in range(419):
                y = mmmdtd[:, i, j]
                x = mmmpt[:, i, j]
                c = np.corrcoef(x, y)[0][1]
                person[i][j] = c
        return c

    def pltwithlucc(self):


    def pltwithregion(self):


d = vali('^la.*LEc', '.tif')
print d.sname
print d.getmonth(6)
print d.getall(d.path['s'],d.sname)
