# Plots the number of Windows users vs. non-Windows users per time-zone, based on bitly_usagov.txt data

# Note - block must be copied into ipython --pylab

import json
from pandas import DataFrame, Series
import pandas as pd


numCitiesDisplay = 5
graphType = 'barh'
stacked = True
labelRotation = 0
plotType = 'normalized' # set as 'normalized' or 'default'

path = '/Users/Jason/PythonForDataAnalysis/datasets/bitly_usagov.txt'
records = [json.loads(line) for line in open(path, 'rb')]
frame = DataFrame(records)
cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
by_tz_os = cframe.groupby(['tz', operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)
indexer = agg_counts.sum(1).argsort()
count_subset = agg_counts.take(indexer)[-10:]

if plotType is 'default':
    count_subset.plot(kind = graphType, stacked = stacked)
elif plotType is 'normalized':
    normed_subset = count_subset.div(count_subset.sum(1), axis = 0)
    normed_subset.plot(kind = graphType, stacked = stacked)
else:
    print('Invalid plot type')