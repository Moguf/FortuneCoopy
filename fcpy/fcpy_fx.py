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
        fin.candlestick2_ochl(ax1, self.opens, self.closes, self.highs, self.lows, width=1, colorup='b', colordown='r')
        ax1.set_xticks([i for i in range(len(self.dates))][::50])
        ax1.set_xlim([0, len(self.dates)])
        ax1.set_xticklabels(["{}".format(i) for i in self.dates[::50]])
        fig.autofmt_xdate()
        plt.show()

    def predictCandles(self):
        self.fx = np.array(self.fx)
        fig = plt.figure()
        ax = fig.add_subplot('111')
        for x in self.fx:
            ax.plot(x - x[0])
        plt.show()

        
if __name__ == '__main__':
    tmp = FcpyFX()
    tmp.readCSV()
    #tmp.graphShow()
    tmp.predictCandles()
