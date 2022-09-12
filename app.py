from urllib import response
import requests
import pandas as pd
import plotly.express as px
import plotly.io as pol

pol.renderers.default = 'browser'

response = requests.get('http://asterank.com/api/kepler?query={}&limit=2000')
df = pd.json_normalize(response.json())

print(df.head())

fig = px.scatter(df, x = 'RPLANET', y = 'TPLANET')
fig.show()