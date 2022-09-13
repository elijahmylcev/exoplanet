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

fig = px.scatter(df, x = 'RPLANET', y = 'A')

rplanet_selector = dcc.RangeSlider(
  id='range-slider',
  min=min(df['RPLANET']),
  max=max(df['RPLANET']),
  marks={5: '5', 10: '10', 20: '20'},
  step=1,
  value=[5, 10]
)

# fig.show()

app = dash.Dash(__name__)

# Frontend
app.layout = html.Div([
  html.H1('Planet Temperature ~ Distance from the Star'),
  html.Div(rplanet_selector, style = {'width': '50%'}),
  dcc.Graph(figure=fig)
],
style={
  'margin': '0 auto',
  'width': '70%',
  'font-family': 'JetBrains Mono'
}
)

if __name__ == '__main__':
  app.run_server(debug=True)