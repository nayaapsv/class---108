import pandas as pd
import csv
import plotly.figure_factory as ff
import statistics

df = pd.read_csv('data2.csv')
rating = df['Avg Rating'].to_list()

fig = ff.create_distplot([rating],['Rating'],show_hist=False)
fig.show()

