import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import dash
import dash_bootstrap_components as dbc
from dash.dash_table.Format import Format, Group
from dash import Dash, dcc, html, Input, Output, callback, dash_table

roi_data = pd.read_csv('https://raw.githubusercontent.com/Susanto7an/Accounting1/main/datasets/Return%20on%20Investment%20-%20Sheet1.csv')

dash.register_page(__name__,path='/ROI', name='Return on Investment', order=6)
layout = dbc.Container([html.Br(),html.Br(),
    html.Div([html.P('Return on Investment Analysis'), html.P('5 Years Forecast')],
             style={'textAlign': 'center','font-weight': 'bold', 'font-size':'26px'}),
    dbc.Row([
        dbc.Col([
            dash_table.DataTable(
                id='roi-datatable',
                columns=[
                    {"name": i, "id": i, "deletable": False, "selectable": True} for i in roi_data.columns
                ],
                style_header={
                    'backgroundColor': 'rgb(30, 30, 30)',
                    'color': 'white'
                },
                style_data={
                    'backgroundColor': 'rgb(50, 50, 50)',
                    'color': 'white',
                },
                data=roi_data.to_dict('records'),  # the contents of the table
                editable=True,  # allow editing of data inside all cells
                row_deletable=False,  # choose if user can delete a row (True) or not (False)
                selected_columns=[],  # ids of columns that user selects
                selected_rows=[],  # indices of rows that user selects
                page_action="none",  # all data is passed to the table up-front or not ('none')
                style_cell={
                    'height': 'auto',
                    # all three widths are needed
                    'minWidth': '100px', 'width': '100px', 'maxWidth': '100px',
                    'whiteSpace': 'normal'
                },
            ),
        ])
    ])
])