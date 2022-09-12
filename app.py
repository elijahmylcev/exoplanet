from urllib import response
import dash
import dash_core_components as dcc
import dash_html_components as html

import requests
import pandas as pd
import plotly.express as px
import plotly.io as pol

pol.renderers.default = 'browser'

response = requests.get('http://asterank.com/api/kepler?query={}&limit=2000')
df = pd.json_normalize(response.json())

print(df.head())

fig = px.scatter(df, x = 'RPLANET', y = 'TPLANET')

# fig.show()

app = dash.Dash(__name__)

# Frontend
app.layout = html.Div([
  html.H1('ExoPlanets chart'),
  dcc.Graph(figure=fig)
])

if __name__ == '__main__':
  app.run_server(debug=True)