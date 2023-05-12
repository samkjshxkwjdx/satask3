import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import plotly.express as px
# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

df = pd.read_csv("co2_emissions_kt_by_country.csv")
df.head()

asia = df[df['country_name'].str.contains('Asia')]['country_name'].unique()
europe = df[df['country_name'].str.contains('Euro')]['country_name'].unique()
caribbean = df[df['country_name'].str.contains('Caribbean')]['country_name'].unique()
africa = df[df['country_name'].str.contains('Africa')]['country_name'].unique() # remove South Africa
africa = africa[africa != 'South Africa']

demographic = df[df['country_name'].str.contains('demo')]['country_name'].unique()
ida = df[df['country_name'].str.contains('IDA')]['country_name'].unique()
ibrd = df[df['country_name'].str.contains('IBRD')]['country_name'].unique()

income = df[df['country_name'].str.contains('income')]['country_name'].unique()


other_regions = ['World', 'Europe', 'North America', 'South Asia', 'OECD members', 'Euro area', 'Arab World', 'Heavily indebted poor countries (HIPC)',
          'Small states','Other small states' , 'Fragile and conflict affected situations', 'Least developed countries: UN classification', 
          'Pacific island small states']

country_groups = np.concatenate((asia, europe, caribbean, africa, demographic, ida, ibrd,income, other_regions))

df_country = df.query("country_name not in @country_groups").copy() # Data with only countries for rows (no aggregates)

fig = px.choropleth(df_country, locations="country_code",
                    animation_frame="year", animation_group="country_name",
                    color="value", 
                    hover_name="country_name",
                    hover_data=['year', 'country_name', 'value'],
                    color_continuous_scale=px.colors.sequential.dense)

fig.update_layout(
    paper_bgcolor="#283618",
    plot_bgcolor="#283618",
    title=dict(text="Worldwide C02 emissions", font=dict(color="#fefae0")),
    hoverlabel=dict(font=dict(color="#fefae0")),
    font=dict(color="#fefae0"),
    geo=dict(bgcolor="#283618")
)

fig.show()

import plotly.offline as pyo


pyo.plot(fig, filename='index.html', auto_open=True)

import chart_studio.tools as tls
tls.get_embed('https://samkjshxkwjdx.github.io/samkjshxkwjdx1.github.io/') #change to your url