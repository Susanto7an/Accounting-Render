import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import dash
import dash_bootstrap_components as dbc
from dash.dash_table.Format import Format, Group, Symbol
from dash.dash_table import FormatTemplate
from dash import Dash, dcc, html, Input, Output, callback, dash_table



sp22_data = pd.read_csv('https://raw.githubusercontent.com/Susanto7an/Accounting1/main/datasets/Sales%20Projection%202022%20-%20Sheet1.csv')
sp23_data = pd.read_csv('https://raw.githubusercontent.com/Susanto7an/Accounting1/main/datasets/Sales%20Projection%202023%20-%20Sheet1.csv')
sp24_data = pd.read_csv('https://raw.githubusercontent.com/Susanto7an/Accounting1/main/datasets/Sales%20Projection%202024%20-%20Sheet1.csv')
sp25_data = pd.read_csv('https://raw.githubusercontent.com/Susanto7an/Accounting1/main/datasets/Sales%20Projection%202025%20-%20Sheet1.csv')
sp26_data = pd.read_csv('https://raw.githubusercontent.com/Susanto7an/Accounting1/main/datasets/Sales%20Projection%202026%20-%20Sheet1.csv')
spbar_data = pd.read_csv('https://raw.githubusercontent.com/Susanto7an/Accounting1/main/datasets/SP_BarChart%20-%20Sheet1.csv')

dash.register_page(__name__,path='/', name='Sales Projection', order=1)

layout = dbc.Container([html.Br(),html.Br(),
    html.Div([html.P('Year: 2022')]),dbc.Row([
        dbc.Col([
            dash_table.DataTable(
                id='datatable-sp22',
                columns=[
                    {"name": 'Item', "id": 'Item'},
                    {"name": 'Variable Cost', "id": 'Variable Cost', 'type':'numeric','format': FormatTemplate.money(2)},
                    {"name": 'Fixed Cost', "id": 'Fixed Cost', 'type':'numeric','format': FormatTemplate.money(2)},
                    {"name": 'Price', "id": 'Price', 'type':'numeric','format': FormatTemplate.money(2)},
                    {"name": 'Quantity Stocked', "id": 'Quantity Stocked', 'type':'numeric'},
                    {"name": 'Quantity Sold', "id": 'Quantity Sold', 'type': 'numeric'},
                    {"name": 'Total Cost', "id": 'Total Cost', 'type': 'numeric'},
                    {"name": 'Total Revenue', "id": 'Total Revenue', 'type': 'numeric'},
                    {"name": 'Gross Profit', "id": 'Gross Profit', 'type': 'numeric'},
                    {"name": 'Inventory', "id": 'Inventory', 'type': 'numeric'},
                    {"name": 'Inventory Value', "id": 'Inventory Value', 'type': 'numeric'},
                    {"name": 'Cost of Goods sold', "id": 'Cost of Goods sold', 'type': 'numeric'},

                ],
                style_header={
                    'backgroundColor': 'rgb(30, 30, 30)',
                    'color': 'white'
                },
                style_data={
                    'backgroundColor': 'rgb(50, 50, 50)',
                    'color': 'white',
                },
                data=sp22_data.to_dict('records'),  # the contents of the table
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
    ]), html.Br(),html.Br(),
    html.Div([html.P('Year: 2023')]),dbc.Row([
        dbc.Col([
            dash_table.DataTable(
                id='datatable-sp23',
                columns=[
                    {"name": 'Item', "id": 'Item'},
                    {"name": 'Variable Cost', "id": 'Variable Cost', 'type': 'numeric',
                     'format': FormatTemplate.money(2)},
                    {"name": 'Fixed Cost', "id": 'Fixed Cost', 'type': 'numeric', 'format': FormatTemplate.money(2)},
                    {"name": 'Price', "id": 'Price', 'type': 'numeric', 'format': FormatTemplate.money(2)},
                    {"name": 'Quantity Stocked', "id": 'Quantity Stocked', 'type': 'numeric'},
                    {"name": 'Quantity Sold', "id": 'Quantity Sold', 'type': 'numeric'},
                    {"name": 'Total Cost', "id": 'Total Cost', 'type': 'numeric'},
                    {"name": 'Total Revenue', "id": 'Total Revenue', 'type': 'numeric'},
                    {"name": 'Gross Profit', "id": 'Gross Profit', 'type': 'numeric'},
                    {"name": 'Inventory', "id": 'Inventory', 'type': 'numeric'},
                    {"name": 'Inventory Value', "id": 'Inventory Value', 'type': 'numeric'},
                    {"name": 'Cost of Goods sold', "id": 'Cost of Goods sold', 'type': 'numeric'},

                ],
                style_header={
                    'backgroundColor': 'rgb(30, 30, 30)',
                    'color': 'white'
                },
                style_data={
                    'backgroundColor': 'rgb(50, 50, 50)',
                    'color': 'white',
                },
                data=sp23_data.to_dict('records'),  # the contents of the table
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
    html.Div([html.P('Year: 2024')]),dbc.Row([
        dbc.Col([
            dash_table.DataTable(
                id='datatable-sp24',
                columns=[
                    {"name": 'Item', "id": 'Item'},
                    {"name": 'Variable Cost', "id": 'Variable Cost', 'type': 'numeric',
                     'format': FormatTemplate.money(2)},
                    {"name": 'Fixed Cost', "id": 'Fixed Cost', 'type': 'numeric', 'format': FormatTemplate.money(2)},
                    {"name": 'Price', "id": 'Price', 'type': 'numeric', 'format': FormatTemplate.money(2)},
                    {"name": 'Quantity Stocked', "id": 'Quantity Stocked', 'type': 'numeric'},
                    {"name": 'Quantity Sold', "id": 'Quantity Sold', 'type': 'numeric'},
                    {"name": 'Total Cost', "id": 'Total Cost', 'type': 'numeric'},
                    {"name": 'Total Revenue', "id": 'Total Revenue', 'type': 'numeric'},
                    {"name": 'Gross Profit', "id": 'Gross Profit', 'type': 'numeric'},
                    {"name": 'Inventory', "id": 'Inventory', 'type': 'numeric'},
                    {"name": 'Inventory Value', "id": 'Inventory Value', 'type': 'numeric'},
                    {"name": 'Cost of Goods sold', "id": 'Cost of Goods sold', 'type': 'numeric'},

                ],
                style_header={
                    'backgroundColor': 'rgb(30, 30, 30)',
                    'color': 'white'
                },
                style_data={
                    'backgroundColor': 'rgb(50, 50, 50)',
                    'color': 'white',
                },
                data=sp24_data.to_dict('records'),  # the contents of the table
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
    html.Div([html.P('Year: 2025')]),dbc.Row([
        dbc.Col([
            dash_table.DataTable(
                id='datatable-sp25',
                columns=[
                    {"name": 'Item', "id": 'Item'},
                    {"name": 'Variable Cost', "id": 'Variable Cost', 'type': 'numeric',
                     'format': FormatTemplate.money(2)},
                    {"name": 'Fixed Cost', "id": 'Fixed Cost', 'type': 'numeric', 'format': FormatTemplate.money(2)},
                    {"name": 'Price', "id": 'Price', 'type': 'numeric', 'format': FormatTemplate.money(2)},
                    {"name": 'Quantity Stocked', "id": 'Quantity Stocked', 'type': 'numeric'},
                    {"name": 'Quantity Sold', "id": 'Quantity Sold', 'type': 'numeric'},
                    {"name": 'Total Cost', "id": 'Total Cost', 'type': 'numeric'},
                    {"name": 'Total Revenue', "id": 'Total Revenue', 'type': 'numeric'},
                    {"name": 'Gross Profit', "id": 'Gross Profit', 'type': 'numeric'},
                    {"name": 'Inventory', "id": 'Inventory', 'type': 'numeric'},
                    {"name": 'Inventory Value', "id": 'Inventory Value', 'type': 'numeric'},
                    {"name": 'Cost of Goods sold', "id": 'Cost of Goods sold', 'type': 'numeric'},

                ],
                style_header={
                    'backgroundColor': 'rgb(30, 30, 30)',
                    'color': 'white'
                },
                style_data={
                    'backgroundColor': 'rgb(50, 50, 50)',
                    'color': 'white',
                },
                data=sp25_data.to_dict('records'),  # the contents of the table
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
    html.Div([html.P('Year: 2026')]),dbc.Row([
        dbc.Col([
            dash_table.DataTable(
                id='datatable-sp26',
                columns=[
                    {"name": 'Item', "id": 'Item'},
                    {"name": 'Variable Cost', "id": 'Variable Cost', 'type': 'numeric',
                     'format': FormatTemplate.money(2)},
                    {"name": 'Fixed Cost', "id": 'Fixed Cost', 'type': 'numeric', 'format': FormatTemplate.money(2)},
                    {"name": 'Price', "id": 'Price', 'type': 'numeric', 'format': FormatTemplate.money(2)},
                    {"name": 'Quantity Stocked', "id": 'Quantity Stocked', 'type': 'numeric'},
                    {"name": 'Quantity Sold', "id": 'Quantity Sold', 'type': 'numeric'},
                    {"name": 'Total Cost', "id": 'Total Cost', 'type': 'numeric'},
                    {"name": 'Total Revenue', "id": 'Total Revenue', 'type': 'numeric'},
                    {"name": 'Gross Profit', "id": 'Gross Profit', 'type': 'numeric'},
                    {"name": 'Inventory', "id": 'Inventory', 'type': 'numeric'},
                    {"name": 'Inventory Value', "id": 'Inventory Value', 'type': 'numeric'},
                    {"name": 'Cost of Goods sold', "id": 'Cost of Goods sold', 'type': 'numeric'},

                ],
                style_header={
                    'backgroundColor': 'rgb(30, 30, 30)',
                    'color': 'white'
                },
                style_data={
                    'backgroundColor': 'rgb(50, 50, 50)',
                    'color': 'white',
                },
                data=sp26_data.to_dict('records'),  # the contents of the table
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
            dcc.Dropdown(id='sp_bar_dropdown', multi=False, value=2022,
                         options=[{'label':x, 'value':x}for x in sorted(spbar_data['Year'].unique())],
                         ),
            dcc.Graph(id='sp_bar_chart')
        ])
    ])
], fluid=True)

@callback(
    Output('sp_bar_chart', 'figure'),
    Input('sp_bar_dropdown', 'value'))
def sp_bar_chart(Year):
    dff = spbar_data.copy()
    dff = dff.sort_values(['Year', 'Sales Prediction'], ascending=[True,True])
    dff = dff[dff['Year']==Year]
    annotations = [dict(yref='paper', y=0.2, showarrow=False, text = '      ')]
    fig1bar = go.Figure()
    fig1bar.add_trace(trace=go.Bar(y=dff['Product'], x=dff['Sales Prediction'],orientation='h',marker=dict(color='#32cd32')))
    fig1bar.update_xaxes(showgrid=False)
    fig1bar.update_yaxes(showgrid=False)
    fig1bar.update_layout(title='Average State Sales',
                          height=500, annotations=annotations,
                          hoverlabel=dict(bgcolor="#f2f2f2", font_size=13, font_family="Lato, sans-serif"),
                          template='plotly_dark',
                          font_family='Arial', font_size=14, font_color='white')
    return fig1bar
