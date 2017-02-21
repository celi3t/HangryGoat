import numpy as np
import pandas as pd

#from datetime import datetime
import matplotlib.pyplot as plt
import json
from dateutil.parser import parse
from datetime import date
import re

jtb_path = '/Users/celi/Desktop/FoodMath/hangry-goat.git/scrapy/hangrygoat/analysis/items.json'
keyword = 'cake'

def check_contains(x):
    return keyword in x

data = {}
data['titles'] = list()
data['dates'] = list()
for element in json.load(open(jtb_path)):
    if not len(element['title']) == 0 and not len(element['timestamp']) == 0:
        title = str(element['title'][0].encode('utf-8', 'replace').lower()).split()
        datestring =  parse(element['timestamp'][0])
        data['titles'].append(title)
        data['dates'].append(datestring)


ts = pd.Series(data['titles'], index = data['dates'])#, dtype = "str")
#ts = ts

tss = ts.groupby([ts.index.year, ts.index.month])

filtered = pd.Series()
for (year, month), values in tss:
    nts = pd.Series(values[values.apply(check_contains)].count() / float(values.count()), index = [date(year = year, month = month, day = 1)])
    filtered = pd.concat([filtered, nts])
    
trend = pd.rolling_mean(filtered, 5)


filtered.plot(kind = 'line', title = 'mentions of ' + keyword)
trend.plot(kind = 'line')
plt.show()

