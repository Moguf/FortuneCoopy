#!/usr/bin/env python
# coding:utf-8

import urllib2
import calendar

#print response.read()

c = calendar.Calendar()

for j in range(3,7):
    g = c.itermonthdates(2016,j)
    for i in range(35):
        s = str(g.next())
        ymd = str(s).split("-")
        y,m,d = ymd
        dweek = calendar.weekday(int(y),int(m),int(d))
        if dweek < 5:
            ymd = "-".join(ymd)
            fname = "t-"+ymd+'-'+calendar.day_abbr[dweek]+".csv"
            url = 'http://k-db.com/stocks/%s?download=csv' % ymd
            response = urllib2.urlopen(url)
            result = response.read()
            wfile = open(fname,'w')
            wfile.write(result)
            print(fname)
