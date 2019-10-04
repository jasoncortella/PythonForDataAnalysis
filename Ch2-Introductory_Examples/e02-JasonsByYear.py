# Basic BabyName analysis - Plots the number of births per year of a specified name

# Note - block must be copied into ipython --pylab

import pandas as pd

enterNames = ['Jason', 'Johanna']
years = range (1880, 2011)
pieces = []
columns = ['name', 'sex', 'births']
for year in years:
    path = '/Users/Jason/PythonForDataAnalysis/datasets/babynames/yob{}.txt'.format(year)
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)
names = pd.concat(pieces, ignore_index = True)

def add_prop(group):
    # Integer division floors
    births = group.births.astype(float)
    group['prop'] = births / births.sum()
    return group
names = names.groupby(['year', 'sex']).apply(add_prop)

def get_top1000(group):
    return group.sort_values(by='births', ascending=False)[:1000]
grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)
top1000.index = np.arange(len(top1000))

boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']
total_births = top1000.pivot_table('births', index='year', columns='name', aggfunc=sum)
subset = total_births[enterNames]
subset.plot(subplots=True, figsize=(12,10), grid=False, title="Number of births per year")
