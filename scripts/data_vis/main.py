import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)
server = app.server

df = pd.read_csv("netflix_titles.csv")
df.drop_duplicates(inplace=True)

pie_fig = px.pie(
    data_frame=df,
    names='type',
    hole=0.8,
    title='TV Show vs. Movie')

bar_fig = px.bar(
    data_frame=df.groupby(["type"], as_index=False).agg(count=pd.NamedAgg(column="type", aggfunc="count")),
    x='type',
    y='count',
    color='type',
    title='TV Show vs. Movie')

app.layout = html.Div(children=[
    html.H1(children='Visualizing Netflix Data With Python'),
    html.Div(children='''
        Using Pandas, Plotly Express, and Dash.
    '''),
    html.Div([
        dcc.Graph(
            id='graph1',
            figure=pie_fig
        ),
    ]),
    html.Div([
        dcc.Graph(
            id='graph2',
            figure=bar_fig
        ),
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)