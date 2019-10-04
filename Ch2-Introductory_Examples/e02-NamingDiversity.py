# Basic BabyName analysis - Plots the diversity of baby names as a function of year
# Note - block must be copied into ipython --pylab

import pandas as pd

years = range (1880, 2011)
namePercent = 0.75
pieces = []
columns = ['name', 'sex', 'births']
for year in years:
    path = '/Users/Jason/PythonForDataAnalysis/datasets/babynames/yob{}.txt'.format(year)
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)
names = pd.concat(pieces, ignore_index = True)

def add_prop(group):
    births = group.births.astype(float)
    group['prop'] = births / births.sum()
    return group
names = names.groupby(['year', 'sex']).apply(add_prop)

def get_top1000(group):
    return group.sort_values(by='births', ascending=False)[:1000]
grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)
top1000.index = np.arange(len(top1000))

def get_quantile_count(group, q=namePercent):
    group = group.sort_values(by='prop', ascending=False)
    return group.prop.cumsum().values.searchsorted(q) + 1

diversity = top1000.groupby(['year', 'sex']).apply(get_quantile_count)
diversity = diversity.unstack('sex')
diversity.plot(title='Number of popular names in top 75 percentage of names')
