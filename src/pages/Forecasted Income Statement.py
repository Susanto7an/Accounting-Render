import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import dash
import dash_bootstrap_components as dbc
from dash.dash_table.Format import Format, Group
from dash import Dash, dcc, html, Input, Output, callback, dash_table


income_statement_data = pd.read_csv('https://raw.githubusercontent.com/Susanto7an/Accounting1/main/datasets/Forecasted%20Income%20Statement%20-%20Sheet1.csv')
income_chart_data = pd.read_csv('https://raw.githubusercontent.com/Susanto7an/Accounting1/main/datasets/Income%20Chart%20Data%20-%20Sheet1.csv')



dash.register_page(__name__,path='/Income', name='Income Statement', order=2)
layout = dbc.Container([html.Br(),html.Br(),
    html.Div([html.P('Forecasted Income Statement'), html.P('5 Years Forecast')],
             style={'textAlign': 'center','font-weight': 'bold', 'font-size':'26px'}),
    dbc.Row([
        dbc.Col([
            dash_table.DataTable(
                id='datatable-sp22',
                columns=[
                    {"name": i, "id": i, "deletable": False, "selectable": True} for i in income_statement_data.columns
                ],
                style_header={
                    'backgroundColor': 'rgb(30, 30, 30)',
                    'color': 'white'
                },
                style_data={
                    'backgroundColor': 'rgb(50, 50, 50)',
                    'color': 'white',
                },
                data=income_statement_data.to_dict('records'),  # the contents of the table
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
        dbc.Col([
            dcc.Dropdown(id='income_dropdown', multi=False, value='Dec-2022',
                         options=[{'label': x, 'value': x} for x in sorted(income_chart_data['Year'].unique())],
                         ),
            dcc.Graph(id='income_chart')
        ])
    ])
], fluid=True)
@callback(
    Output('income_chart', 'figure'),
    Input('income_dropdown', 'value'))
def income_chart(Year):
    dff = income_chart_data.copy()
    dff = dff[dff['Year']==Year]
    annotations = [dict(yref='paper', y=0.2, showarrow=False, text = '      ')]
    fig1bar = go.Figure()
    fig1bar.add_trace(trace=go.Bar(y=dff['Value'], x=dff['Account'],marker=dict(color=['#ffff00', '#ffa500','#32cd32' ])))
    fig1bar.update_xaxes(showgrid=False)
    fig1bar.update_yaxes(showgrid=False)
    fig1bar.update_layout(title='Sales vs Expenses vs Net Profit',
                          height=500, annotations=annotations,
                          hoverlabel=dict(bgcolor="#f2f2f2", font_size=13, font_family="Lato, sans-serif"),
                          template='plotly_dark',
                          font_family='Arial', font_size=14, font_color='white')
    return fig1bar
