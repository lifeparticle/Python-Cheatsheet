import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = pd.read_csv("netflix_titles.csv")

movie = df['type'] == 'Movie'
tv_show = df['type'] == 'TV Show'

# df = df.groupby(["type"]).count()
print(movie.count())
print(tv_show.count())


fig = px.pie(
    data_frame=df,
    names='type',
    # values='title',
    color='type',
    hole=0.5,
    height=800,
    width=800,
    title='TV Show vs. Movie')
# fig.show()



app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)