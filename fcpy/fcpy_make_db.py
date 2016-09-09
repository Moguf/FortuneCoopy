#!/usr/bin/env python3
# fileencoding:utf-8

import csv
import codecs
from subprocess import check_output
from sqliteater import SQLiteater


class FcpyMakeDB:
    def __init__(self):
        self.db = SQLiteater()
        self.db.openDB('../data/mystocks.db')
        self.tablename = 'stocks'
        self.namelist = ['date_code', 'date', 'weekday', 'code', 'name', 'market',
                         'open', 'high', 'low', 'close', 'volume', 'turnover']
        self.stocks_types = [str, int, str, str, str, str, float, float, float, float, int, int]
        self.constraints = ['PRIMARY KEY', '', '',  '',  '',  '',  '',  '',  '',  '',  '',  '']
                
    def createTable(self):
        self.db.createTable(self.tablename, self.namelist, self.stocks_types, self.constraints)

    def insertData(self, filepath):
        with open(filepath, encoding='shift-jis') as f:
            filename = filepath.split('/')[-1]
            reader = csv.reader(f)
            next(reader)
            ilist = filename.split(".")
            weekday = ilist[0].split('-')[-1]
            sdate = "".join(ilist[0].split('-')[1:-1])
            date = int(sdate)

            for i, row in enumerate(reader):
                data = []
                code, name, market, openv, high, low, close, volume, turnover = row
                indata = [sdate+code, date, weekday, code, name, market, openv, high, low, close, volume, turnover]
                self.db.insert(self.tablename, self.namelist, typelist=self.stocks_types, datalist=indata)

    def showDB(self):
        self.db.selectAll(self.tablename)
        
    def close(self):
        self.db.close()
    
        
if __name__ == '__main__':
    tmp = FcpyMakeDB()
    tmp.createTable()
    cmd = 'ls ../data/csv/*.csv'
    for ifile in check_output(cmd, shell=True).split():
        tmp.insertData(ifile.decode('utf-8'))
    #tmp.showDB()
    tmp.close()
    #createDB()
    #createDate("t-2015-06-29-Mon.csv")
