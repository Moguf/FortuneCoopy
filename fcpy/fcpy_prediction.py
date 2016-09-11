
import numpy as np
import sklearn
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import matplotlib.finance as fin
import matplotlib.dates as mdates

from sqliteater import SQLiteater

class FcpyPrediction(object):
    def __init__(self):
        self.db = SQLiteater()
        self.db.openDB('../data/mystocks.db')
        self.tablename = 'stocks'
        
    def run(self):
        print((self.db.getRowData(self.tablename, 'code', distinct=True)))

              
    def getClose(self, code):
        return self.numpyArray(self.db.select(self.tablename, 'close', where='code == "{}"'.format(code)))

    def createCorrelationTable(self):
        
    def chart(self, code):
        date = self.numpyArray(self.db.select(self.tablename, 'date', where='code == "{}"'.format(code)))
        high = self.numpyArray(self.db.select(self.tablename, 'high', where='code == "{}"'.format(code)))
        low = self.numpyArray(self.db.select(self.tablename, 'low', where='code == "{}"'.format(code)))
        openv = self.numpyArray(self.db.select(self.tablename, 'open', where='code == "{}"'.format(code)))
        close = self.numpyArray(self.db.select(self.tablename, 'close', where='code == "{}"'.format(code)))
        volume = self.numpyArray(self.db.select(self.tablename, 'volume', where='code == "{}"'.format(code)))

        fig = plt.figure()
        ax1 = fig.add_subplot('111')
        
        #ax2 = fig.add_subplot('212')

        fin.candlestick2_ochl(ax1, openv, close, high, low, width=1, colorup='b', colordown='r')
        #fin.volume_overlay(ax2, openv, close, volume, width=1)
        ax1.plot(close)
        ax1.set_xticks([i for i in range(len(date))][::10])
        ax1.set_xlim([0,len(date)])
        ax1.set_xticklabels(["{}".format(i) for i in date[::10]])
        fig.autofmt_xdate()
        plt.show()

    def numpyArray(self, inlist):
        return np.array(inlist).T[0]

    def toList():
    def close(self):
        self.db.close()

if __name__ == '__main__':
    tmp = FcpyPrediction()
    tmp.run()
    print(pearsonr(tmp.getClose('1301T'), tmp.getClose('1305T')))
    tmp.close()

    
