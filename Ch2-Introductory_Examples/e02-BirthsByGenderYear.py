# Basic BabyName analysis - Plot Births by Year and Gender

# Note - block must be copied into ipython --pylab

import pandas as pd

path = '/Users/Jason/PythonForDataAnalysis/datasets/babynames/yob1880.txt'


years = range (1880, 2011)
pieces = []
columns = ['name', 'sex', 'births']
for year in years:
    path = '/Users/Jason/PythonForDataAnalysis/datasets/babynames/yob{}.txt'.format(year)
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)
names = pd.concat(pieces, ignore_index = True)
total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)
total_births.plot(title = 'Total births by sex and year')