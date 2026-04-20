import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash(__name__)

# ================= LAYOUT =================
app.layout = html.Div(style={
    'backgroundColor': '#0b0f1a',
    'color': 'white',
    'fontFamily': 'Arial'
}, children=[

    html.H1("🛰️ Mission Control Dashboard",
            style={'textAlign': 'center', 'color': '#00d4ff'}),

    html.Div([
        html.Div(id='status-box', style={
            'textAlign': 'center',
            'fontSize': '28px',
            'padding': '10px',
            'border': '2px solid white',
            'margin': '10px'
        })
    ]),
