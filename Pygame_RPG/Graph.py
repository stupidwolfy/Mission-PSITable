""" Graph generator """
print("Loading resource.." ,end='..')

import plotly
from plotly.graph_objs import Scatter, Layout
import plotly.graph_objs as go

#plotly.tools.set_credentials_file(username='it61070268', api_key='yt9KMI4UYOM6vNlH4Jvc')

x_axis = [1,2,3,4]
y_axis = [4,3,2,1]


data = [go.Scatter(x=x_axis, y=y_axis)]
layout = go.Layout(title="hello world")

print("Completed!")
print("Generating graph..", end="..")

plotly.offline.plot({"data": data,"layout": layout}, auto_open=True)

##plotly.offline.plot({"data": [Scatter(x=[1, 2, 3, 4], y=[4, 1, 3, 500])],
##                          "layout": Layout(title="Score")}
##                          )

print("Completed!")
