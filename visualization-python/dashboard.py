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

    
    html.Div([
        dcc.Graph(id='temp-graph', style={'width': '48%', 'display': 'inline-block'}),
        dcc.Graph(id='volt-graph', style={'width': '48%', 'display': 'inline-block'})
    ]),

    html.H3("📊 Latest Telemetry", style={'textAlign': 'center'}),

    html.Div(id='table', style={'padding': '20px'}),

    dcc.Interval(id='interval', interval=1000, n_intervals=0)
])

# ================= UPDATE =================
@app.callback(
    [Output('temp-graph', 'figure'),
     Output('volt-graph', 'figure'),
     Output('status-box', 'children'),
     Output('status-box', 'style'),
     Output('table', 'children')],
    [Input('interval', 'n_intervals')]
)
def update(n):

    try:
        df = pd.read_csv("telemetry.csv",
                         names=["seq", "time", "temp", "volt"])

        # ===== TEMPERATURE GRAPH =====
        temp_fig = go.Figure()
        temp_fig.add_trace(go.Scatter(
            x=df["seq"], y=df["temp"],
            mode='lines+markers',
            name='Temperature'
        ))

        temp_fig.update_layout(
            template="plotly_dark",
            title="Temperature",
            xaxis_title="Packet",
            yaxis_title="°C"
        )

        # ===== VOLTAGE GRAPH =====
        volt_fig = go.Figure()
        volt_fig.add_trace(go.Scatter(
            x=df["seq"], y=df["volt"],
            mode='lines+markers',
            name='Voltage'
        ))

        volt_fig.update_layout(
            template="plotly_dark",
            title="Voltage",
            xaxis_title="Packet",
            yaxis_title="V"
        )

        # ===== STATUS =====
        if len(df) > 0:
            last_temp = df["temp"].iloc[-1]

            if last_temp > 25:
                status = "🔴 ALERT: High Temperature"
                style = {
                    'textAlign': 'center',
                    'fontSize': '28px',
                    'padding': '10px',
                    'border': '2px solid red',
                    'color': 'red'
                }
            else:
                status = "🟢 SYSTEM NORMAL"
                style = {
                    'textAlign': 'center',
                    'fontSize': '28px',
                    'padding': '10px',
                    'border': '2px solid green',
                    'color': 'lightgreen'
                }
        else:
            status = "No Data"
            style = {}

 # ===== TABLE =====
        table = html.Table([
            html.Tr([html.Th(col) for col in df.columns])
        ] + [
            html.Tr([html.Td(df.iloc[i][col]) for col in df.columns])
            for i in range(max(0, len(df)-5), len(df))
        ])

        return temp_fig, volt_fig, status, style, table

    except:
        return go.Figure(), go.Figure(), "Waiting...", {}, ""

# ================= RUN =================
if __name__ == '__main__':
    app.run(debug=True)
