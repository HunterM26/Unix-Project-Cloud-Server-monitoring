import dash
from dash import dcc, html
import requests
import time

app = dash.Dash(__name__)

def fetch_metrics():
    try:
        response = requests.get("http://your-server-ip:5000/metrics").json()
        return response
    except:
        return {}

app.layout = html.Div([
    html.H1("Server Performance Dashboard"),
    dcc.Interval(id='interval-component', interval=5000, n_intervals=0),
    dcc.Graph(id="cpu-graph"),
])

@app.callback(
    dash.dependencies.Output("cpu-graph", "figure"),
    [dash.dependencies.Input("interval-component", "n_intervals")]
)
def update_graph(n):
    metrics = fetch_metrics()
    cpu_usage = metrics.get("cpu_usage", 0)

    return {
        "data": [{"x": [time.time()], "y": [cpu_usage], "type": "line", "name": "CPU Usage"}],
        "layout": {"title": "Real-time CPU Usage"}
    }

if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0", port=8050)
