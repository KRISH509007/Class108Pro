import csv
import pandas as pd
import plotly.figure_factory as ff

df=pd.read_csv("class108Pro.csv")

fig=ff.create_distplot([df["Avg Rating"].tolist()],['Avg Rating'],show_hist=False)
fig.show()
