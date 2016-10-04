#!/usr/bin/python3
# coding:utf-8

import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.finance as fin
import matplotlib.dates as mdates

class ForexSimulator(object):
    """ Simulator for forex market. """
    def __init__(self):
        self.csv_path = ''
        self.dates = []
        self.opens = []
        self.highs = []
        self.lows = []
        self.closes = []
        self.fx = []
        self.revalage = 10

    def readData(self):
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

    
    def run(self):
        pass

    

if __name__ == '__main__':
    sim = ForexSimulator()
    sim.run()
