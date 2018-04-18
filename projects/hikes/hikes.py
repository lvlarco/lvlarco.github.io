import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab
from plotly import __version__
import plotly.plotly as py
from plotly.offline.offline import _plot_html

df = pd.read_csv("files/hike_compilation.csv")

# print(df.columns)
listEG = df['Elevation Gain [ft]']
listTime = df['Time [hh:mm]']

plot1 = plt.plot(listTime, listEG, 'o')
plt.ylabel('Elevation Gain [ft]')
plt.xlabel('Time [hh:mm]')
plt.show()

# py.image.save_as(plot1, 'my_plot.png')
# 
# # plotly.offline.plot(, include_plotlyjs=False, output_type='div')
# 
# # data_or_figure = [{"x": [1, 2, 3], "y": [3, 1, 6]}]
# plot_html = _plot_html(plot1, False, "", '100%', '100%', 525)
# # 
# print(plot_html)
# # plot_url = py.plot_mpl(plot1)
# # print(df['ID'])
