import pandas as pd

fandango = pd.read_csv('fandango_score_comparison.csv')
series_film = fandango['FILM']

#print(series_film[0:10])


from pandas import Series

film_names = series_film.values

#print(type(film_names))
#print(film_names)

series_rt = fandango['RottenTomatoes']

rt_scores = series_rt.values

#print(series_rt)

series_custom = Series(rt_scores, index=film_names)

print(series_custom[['Taken 3 (2015)','Leviathan (2014)']])
