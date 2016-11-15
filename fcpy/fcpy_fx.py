#!/usr/bin/env python3
# textencoding: utf-8

import csv
import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt
import matplotlib.finance as fin
import matplotlib.dates as mdates


class FcpyFX(object):
    def __init__(self):
        self.csv = '../data/fx/USDJPY.csv'
        self.dates = []
        self.opens = []
        self.highs = []
        self.lows = []
        self.closes = []
        self.fx = []

    def readCSV(self):
        with open(self.csv, encoding='shift-jis') as f:
            filename = self.csv.split('/')[-1]
            reader = csv.reader(f)
            next(reader)
            for i, row in enumerate(reader):
                date, opens, highs, lows, closes = row
                self.dates.append(date)
                self.opens.append(float(opens))
                self.highs.append(float(highs))
                self.lows.append(float(lows))
                self.closes.append(float(closes))
                self.fx.append([float(opens), float(highs), float(lows), float(closes)])

                
    def graphShow(self):
        fig = plt.figure()
        ax1 = fig.add_subplot('111')
        self.dates = self.dates[:40]
        fin.candlestick2_ochl(ax1, self.opens, self.closes, self.highs, self.lows, width=1, colorup='k', colordown='w')
        ax1.set_xticks([i for i in range(len(self.dates))][::2])
        ax1.set_xlim([0, len(self.dates)])
        ax1.set_xticklabels(["{}".format(i) for i in self.dates[::2]])
        ax1.set_ylim([117, 122])        
        fig.autofmt_xdate()
        plt.savefig("chart.png")
        #plt.show()

    def each_distribution(self):
        self.fx = np.array(self.fx)
        fig = plt.figure()
        ax = fig.add_subplot('111')
        data = []
        o = np.array(self.opens)
        h = np.array(self.highs)
        l = np.array(self.lows)
        c = np.array(self.closes)
        idx = []
        
        for i, x in enumerate(self.fx):
            if (x[3] / x[0] - 1 > 0.03):
                idx.append(True)
            else:
                idx.append(False)

                
        co = np.array(c) - np.array(o)
        ho = np.array(h) - np.array(o)
        lo = np.array(l) - np.array(o)
        hlo = np.append(ho, lo)
        ave = np.average(hlo)
        var = np.var(hlo)
        x = np.arange(-5,5,0.01)
        y = self.normal(ave, var, x)
        idx = np.array(idx)
        bigo = (np.where(idx, o, 0))
        bigh = (np.where(idx, h, 0))
        bigl = (np.where(idx, l, 0))
        bigc = (np.where(idx, c, 0))        
        
        #ax.plot(afridx)
        fin.candlestick2_ochl(ax, o, c, h, l, width=1, colorup='b', colordown='r')                
        fin.candlestick2_ochl(ax, bigo, bigc, bigh, bigl, width=1, colorup='y', colordown='r')        
        #self.hist(ax2, co)
        #self.set_xrange(ax)
        #self.set_xrange(ax2)        
        #ax.plot(x, y)
        plt.show()


    def set_xrange(self, ax):
        ax.set_xlim([-5.0, 5.0])
        
    def hist(self, ax, data):
        ax.hist(data, bins=100, normed=True)

    def plot(self, ax, data):
        ax.plot(data)

    def normal(self, ave, var, x):
        return 1/np.sqrt(2*np.pi*var)*np.exp(-(x-ave)**2/(2*var))

    
if __name__ == '__main__':
    tmp = FcpyFX()
    tmp.readCSV()
    tmp.graphShow()
    #tmp.each_distribution()
