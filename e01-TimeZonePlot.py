# Note - block must be copied into ipython --pylab

import json
from pandas import DataFrame, Series
import pandas as pd

numCitiesDisplay = 5
graphType = 'barh'
labelRotation = 0

path = '/Users/Jason/PythonForDataAnalysis/datasets/bitly_usagov.txt'
records = [json.loads(line) for line in open(path, 'rb')]
frame = DataFrame(records)
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
tz_counts[:numCitiesDisplay].plot(kind=graphType, rot=labelRotation)
