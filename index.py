from app import app
from apps import Info, Monthly
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H4("COVID-19 WebApp"),
        html.Hr(),
        html.P(
            children='Web application for monitoring the expansion of the epidemic COVID-19 ', className="lead"
        ),
        html.Hr(),
        dbc.Nav(
            [
                html.Hr(),
                dcc.Link("COVID-19 Monthly cases", href="/apps/Monthly", className="btn btn-secondary",
                         style={"marginBottom": 20}),
                html.Hr(),
                dcc.Link("COVID-19 Country info", href="/apps/Info", className="btn btn-secondary"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    sidebar,
    content,
],
)


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return sidebar
    elif pathname == '/apps/Info':
        return Info.layout
    elif pathname == '/apps/Monthly':
        return Monthly.layout
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)
