""" Graph generator """
print("..:::Pygame RPG Graph generator:::..")
print("Loading resource.." ,end='..')

import plotly
from plotly import tools
import plotly.plotly as py
import plotly.graph_objs as go
from firebase import firebase

url = 'https://pygame-rpg01-223910.firebaseio.com/'
messenger = firebase.FirebaseApplication(url)

fire_score = messenger.get('/Score', None) ## Get score in dict type
fire_wave = messenger.get('/Wave', None) ## Get wave in dict type
fire_time = messenger.get('/Time', None) ## Get time in dict type

print("Done!")
print("Generating graph....")

fire_x, fire_y = list(), list()
for s in fire_score:
    fire_x.append('^'+str(s)+'^')
    fire_y.append(fire_score[s])
#Scatter
Score = go.Bar(
    x=fire_x,
    y=fire_y,
    name = 'Score',
#    text=['Text A', 'Text B', 'Text C'],
)

fire_x, fire_y = list(), list()
for w in fire_wave:
    fire_x.append('^'+str(w)+'^')
    fire_y.append(fire_wave[w])

Wave = go.Bar(
    x=fire_x,
    y=fire_y,
    name = 'Wave',
#    text=['Text D', 'Text E', 'Text F'],
#    textposition='inside'
)

fire_x, fire_y = list(), list()
for t in fire_time:
    fire_x.append('^'+str(t)+'^')
    fire_y.append(fire_time[t])

Timess = go.Bar(
    x=fire_x,
    y=fire_y,
    name = 'Time',
#    text=['Text D', 'Text E', 'Text F'],
#    textposition='inside'
)

title = ('Score', 'Wave', 'Time', 'Total')
fig = tools.make_subplots(rows=4, cols=1, subplot_titles=title )

fig.append_trace(Score, 1, 1)
fig.append_trace(Wave, 2, 1)
fig.append_trace(Timess, 3, 1)
fig.append_trace(Score, 4, 1)
fig.append_trace(Wave, 4, 1)

fig['layout'].update(height=1600, width=800, showlegend=False, title='Player Result')
plotly.offline.plot(fig, filename='Graphv3.html')

print("Completed!")
