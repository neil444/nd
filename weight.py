import plotly.figure_factory as ff
import pandas as pd
import csv

df = pd.read_csv("c:/Users/ADI/Downloads/Normal-Distribution-master (1)/Normal-Distribution-master/data.csv")
fig = ff.create_distplot([df["Weight(Pounds)"].tolist()], ["Weight"], show_hist=False)
fig.show()
