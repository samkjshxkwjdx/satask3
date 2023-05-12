import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import plotly.express as px

df = pd.read_csv('Fuel production vs consumption.csv', encoding = "ISO-8859-1")

fig = px.line(df, x="Year", y="Gas consumption(m³)", color='Entity', title='Worldwide gas consumption')

fig.update_layout(
    paper_bgcolor="#283618",
    plot_bgcolor="#283618",
    xaxis=dict(title=dict(text="Year", font=dict(color="#fefae0")), tickfont=dict(color="#fefae0"), showgrid=False),
    yaxis=dict(title=dict(text="Gas consumption (m³)", font=dict(color="#fefae0")), tickfont=dict(color="#fefae0"), showgrid=False),
    title=dict(text="Worldwide gas consumption", font=dict(color="#fefae0")),
    legend=dict(font=dict(color="#fefae0")),
    xaxis_tickangle=-45,
)





# Display the chart
fig.show()

import plotly.offline as pyo


pyo.plot(fig, filename='index.html', auto_open=True)