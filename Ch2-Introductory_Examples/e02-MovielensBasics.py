# Plots the number of data entries per time-zone, based on bitly_usagov.txt data

# Note - block must be copied into ipython --pylab

import pandas as pd

path = '/Users/Jason/PythonForDataAnalysis/datasets/movielens/users.dat'

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table(path, sep='::', header=None, names = unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table(path, sep='::', header=None, names = rnames)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table(path, sep='::', header=None, names = mnames)

print(users[:5])
print(ratings[:5])
print(movies[:5])