import dash
from dash import html, dcc
import dash_bootstrap_components as dbc


LOGO = "https://images.prismic.io/plotly-marketing-website-2/69e12d6a-fb65-4b6e-8423-9465a29c6028_plotly-logo-lg.png?auto=compress,format"

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.DARKLY],
                meta_tags = [{'name': 'viewport',
                    'content': 'width=device-width, initial-scale=1.0'}]
)
server = app.server


sidebar = dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div('Sales Projection', className="ms-2"),
                    ],
                    href="/",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.Div('Forecasted Income Statement', className="ms-2"),
                    ],
                    href="/Income",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.Div('Forecasted Cashflow Statement', className="ms-2"),
                    ],
                    href="/Cashflow",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.Div('Forecasted Balance Sheet', className="ms-2"),
                    ],
                    href="/Balance",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        dbc.DropdownMenu(
                            [
                                dbc.DropdownMenuItem('Cost Volume Profit Analysis', href='/CVP'),
                                dbc.DropdownMenuItem(divider=True),
                                dbc.DropdownMenuItem('Return on Investment', href='/ROI'),
                                dbc.DropdownMenuItem(divider=True),
                                dbc.DropdownMenuItem('Net Present Value', href='/NPV'),
                                dbc.DropdownMenuItem(divider=True),
                                dbc.DropdownMenuItem('Payback Period', href='/PP'),
                                dbc.DropdownMenuItem(divider=True),
                                dbc.DropdownMenuItem('Operating Profit Margin', href='/OPM'),
                                dbc.DropdownMenuItem(divider=True),
                            ], label='More',
                        )
                    ]
                )
            ],
            vertical=False,
            pills=True,
            className="bg-dark",
)

app.layout = dbc.Container([
    html.A(
        dbc.Row([
            dbc.Col(html.Img(src=LOGO, height="25px"))
    ], justify='center'),href="https://plotly.com",
                style={"textDecoration": "none"}),
        dbc.Row([
            dbc.Col(html.Div("Accounting Portfolio", className='font-weight-bold text-white',
                             style={'fontSize':50})),
        dbc.Row([
            sidebar, dash.page_container,
        ])
    ], justify='center'),

], fluid=True)

if __name__ == "__main__":
    app.run(debug=False, port=8300)

