# -*- coding: utf-8 -*-
print("กำลังโหลดทรัพยากร.." ,end='..')

import plotly
from plotly.graph_objs import Scatter, Layout
print("สำเร็จ!")
print("กำลังสร้างแผนภูมิ..", end="..")
##print(plotly.__version__)  # version >1.9.4 required
plotly.offline.plot({
"data": [
    Scatter(x=[1, 2, 3, 4], y=[4, 1, 3, 500])
],
"layout": Layout(
    title="hello world"
)
})
print("สำเร็จ!")
