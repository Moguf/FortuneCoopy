import numpy as np
from sklearn.preprocessing import StandardScaler, scale
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
        self.code_list = []
        
    def run(self):
        print((self.db.getRowData(self.tablename, 'code', distinct=True)))

    def getClose(self, code):
        return self.numpyArray(self.db.select(self.tablename, 'close', where='code == "{}"'.format(code)))

    def getCode(self):
        return self.numpyArray(self.db.select(self.tablename, 'code', distinct=True))

    def createCorrelationTable(self):
        self.code_list = self.getCode()
        for icode in self.code_list:
            try:
                print(icode, end='')
            except:
                print()
                pass

    def createNormalizedTable(self, codelist):
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        
        for icode in codelist:
            data = self.getClose(icode)
            scaled = scale(data)
            ax1.plot(scaled)
        #ax.hist(scaled, bins=np.arange(min(scaled), max(scaled) + binwidth, binwidth))

        plt.show()
        
            
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

    def toList(self, inlist):
        pass
        
    def close(self):
        self.db.close()

if __name__ == '__main__':
    tmp = FcpyPrediction()
    #tmp.run()
    #print(pearsonr(tmp.getClose('1301T'), tmp.getClose('1305T')))
    #tmp.createCorrelationTable()
    code = ['1301T', '1305T', '1306T', '1311T', '1308T', '1310T', '1320T', '9790T', '9791T', '1435T']
    tmp.createNormalizedTable(code)
    tmp.close()

    
