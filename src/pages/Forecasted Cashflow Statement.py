import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import dash
import dash_bootstrap_components as dbc
from dash.dash_table.Format import Format, Group
from dash import Dash, dcc, html, Input, Output, callback, dash_table


cashflow_statement_data = pd.read_csv('https://raw.githubusercontent.com/Susanto7an/Accounting1/main/datasets/Forecasted%20Cashflow%20Statement%20-%20Sheet1.csv')
cashflow_chart_data = pd.read_csv('https://raw.githubusercontent.com/Susanto7an/Accounting1/main/datasets/Cashflow%20Line%20Chart%20-%20Sheet1.csv')


########################################################################################################################
cashflow_line = go.Figure()
cashflow_line.add_trace(go.Scatter(x=cashflow_chart_data['Year'],
                                   y=cashflow_chart_data['Cashflow From Operating Activities'],
                                   mode='lines+markers',
                                   line={'color':'#32cd32'}))
cashflow_line.update_layout(title='Cashflow From Operating Activities',
                               height=500,
                               hoverlabel=dict(bgcolor="#f2f2f2", font_size=13, font_family="Lato, sans-serif"),
                               template='plotly_dark',
                               font_family='Arial', font_size=14, font_color='white',
                               showlegend=False)

########################################################################################################################


dash.register_page(__name__,path='/Cashflow', name='Cashflow Statement', order=3)
layout = dbc.Container([html.Br(),html.Br(),
    html.Div([html.P('Forecasted Cashflow Statement'), html.P('5 Years Forecast')],
             style={'textAlign': 'center','font-weight': 'bold', 'font-size':'26px'}),
    dbc.Row([
        dbc.Col([
            dash_table.DataTable(
                id='cashflow-datatable',
                columns=[
                    {"name": i, "id": i, "deletable": False, "selectable": True} for i in cashflow_statement_data.columns
                ],
                style_header={
                    'backgroundColor': 'rgb(30, 30, 30)',
                    'color': 'white'
                },
                style_data={
                    'backgroundColor': 'rgb(50, 50, 50)',
                    'color': 'white',
                },
                data=cashflow_statement_data.to_dict('records'),  # the contents of the table
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
                style_cell_conditional=[
                    {
                        'if': {'column_id': c},
                        'textAlign': 'left'
                    } for c in ['Item']
                ],
            ),
        ])
    ]), html.Br(), html.Br(),
    dbc.Row([
        dbc.Col([dcc.Graph(id='cashflow_chart', figure=cashflow_line)
        ]),
    ])
])