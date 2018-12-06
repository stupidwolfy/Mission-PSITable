# -*- coding: utf-8 -*-
""" Graph generator """
print("..:::โปรแกรมสร้างแผนภูมิเกม Python RPG:::..")
print("กำลังโหลดข้อมูล" ,end='..')

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

print("สำเร็จ!")
print("กำลังสร้างแผนภูมิ....")

fire_x, fire_y = list(), list()
for s in fire_score:
    fire_x.append('^'+str(s)+'^')
    fire_y.append(fire_score[s])
#Scatter
Score = go.Bar(
    x=fire_x,
    y=fire_y,
    name = 'คะแนน',
#    text=['Text A', 'Text B', 'Text C'],
)

fire_x, fire_y = list(), list()
for w in fire_wave:
    fire_x.append('^'+str(w)+'^')
    fire_y.append(fire_wave[w])

Wave = go.Bar(
    x=fire_x,
    y=fire_y,
    name = 'ด่าน',
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
    name = 'วินาที',
#    text=['Text D', 'Text E', 'Text F'],
#    textposition='inside'
)

title = ('คะแนน', 'ด่าน', 'เวลา', 'โดยรวม')
fig = tools.make_subplots(rows=4, cols=1, subplot_titles=title )

fig.append_trace(Score, 1, 1)
fig.append_trace(Wave, 2, 1)
fig.append_trace(Timess, 3, 1)
fig.append_trace(Score, 4, 1)
fig.append_trace(Wave, 4, 1)

temp = 1
for i in fig['layout']['annotations']:
    if temp == 1:
        i['font'] = dict(family='Courier New, monospace', size=35,color='#0000aa')
    elif temp == 2:
        i['font'] = dict(family='Courier New, monospace', size=35,color='#aa0000')
    elif temp == 3:
        i['font'] = dict(family='Courier New, monospace', size=35,color='#00aa00')
    elif temp == 4:
        i['font'] = dict(family='Courier New, monospace', size=35,color='#000000')
    temp += 1

fig['layout'].update(height=3600, showlegend=False, title='กระดานคะแนน Python RPG', font=dict(family='Courier New, monospace', size=25, color='#000000'))
plotly.offline.plot(fig, filename='Graphv3.html')

print("เรียบร้อย!")
