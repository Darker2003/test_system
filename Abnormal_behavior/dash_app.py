import dash
from dash import dcc
from dash import html
from django_plotly_dash import DjangoDash
import plotly.express as px
import pandas as pd

# Example DataFrame
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app = DjangoDash('SimpleExample')   # replaces dash.Dash

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
], style={'height': '100000px', 'width': '100px'})  # Adjust the height and width of the div here