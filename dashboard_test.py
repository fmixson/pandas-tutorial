from dash import Dash, dash_table, html, dcc, Input, Output
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px

df = pd.read_csv('C:/Users/flmix/OneDrive/Documents/Data Sheets/Division_Enrollment.csv', encoding='Latin')
pd.set_option('display.max_columns', None)
# departments = df['Dept'].unique()
scheduling_df = pd.DataFrame()

app = Dash(__name__,
            external_stylesheets=[dbc.themes.BOOTSTRAP]
           )
app.layout = html.Div(
    [
        html.Div(
        dcc.Dropdown(id='dept_dropdown',
                     options=[{'label': dept, 'value': dept}
                              for dept in df['Dept'].unique()]
                     )),
        dbc.Row([
            dbc.Col(html.Div(html.H2('Spring 2023 by Modalities')), width=4),
            dbc.Col(html.Div(html.H2('Spring 2023 by Sessions')), width=4),
            dbc.Col(html.Div(html.H2('Spring 2023 by Modalities')), width=4),
        ]),
        dbc.Row([
            dbc.Col(html.Div(id='modality_table'), width=4),
            dbc.Col(html.Div(id='session_table'), width=4),
            dbc.Col(html.Div(dcc.Graph(id='modality_piechart')), width=4)
        ]),
        dbc.Row([
            dbc.Col(html.Div(id='datasheet'))
        ])
    ]
)
@app.callback(
    Output(component_id='datasheet', component_property='children'),
    Input(component_id='dept_dropdown', component_property='value')
)
def display_datatable(dept):
    if dept is None:
        return dash_table.DataTable(df.to_dict('records'), [{'name': i, 'id': i} for i in df])
    else:
        dept_df = df[df['Dept'] == dept]
        return dash_table.DataTable(dept_df.to_dict('records'), [{'name': i, 'id': i} for i in dept_df])


@app.callback(
    Output(component_id='modality_table', component_property='children'),
    Input(component_id='dept_dropdown', component_property='value')
)
def display_modalities(dept):
    if dept is None:
        subset_df = df[['Dept', 'Room', 'Class', 'Size', 'Max']]
        modalities = subset_df.groupby('Room').agg({'Class': 'count', 'Size': 'sum', 'Max': 'sum'}).reset_index()
        return dash_table.DataTable(modalities.to_dict('records'), [{'name': i, 'id': i} for i in modalities])
    else:
        subset_df = df[['Dept', 'Room', 'Class', 'Size', 'Max']]
        subset_dff = subset_df[subset_df['Dept'] == dept]
        modalities = subset_dff.groupby('Room').agg({'Class': 'count', 'Size': 'sum', 'Max': 'sum'}).reset_index()
        return dash_table.DataTable(modalities.to_dict('records'), [{'name': i, 'id': i} for i in modalities])

@app.callback(
    Output(component_id='modality_piechart', component_property='children'),
    Input(component_id='dept_dropdown', component_property='value')
)
def modalities_piechart(dept):
    if dept is None:
        subset_df = df[['Dept', 'Room', 'Class', 'Size', 'Max']]
        modalities = subset_df.groupby('Room').agg({'Class': 'count', 'Size': 'sum', 'Max': 'sum'}).reset_index()
        total_count = modalities['Class'].sum()
        modalities['Perc'] = modalities['Class'] / total_count
        print(modalities)
        fig = px.pie(modalities, values='Perc', names='Room')
        fig.show()
        return fig
    else:
        subset_df = df[['Dept', 'Room', 'Class', 'Size', 'Max']]
        subset_dff = subset_df[subset_df['Dept'] == dept]
        modalities = subset_dff.groupby('Room').agg({'Class': 'count', 'Size': 'sum', 'Max': 'sum'}).reset_index()
        return dash_table.DataTable(modalities.to_dict('records'), [{'name': i, 'id': i} for i in modalities])

@app.callback(
    Output(component_id='session_table', component_property='children'),
    Input(component_id='dept_dropdown', component_property='value'))
def display_sessions(dept):
    if dept is None:
        subset_df = df[['Dept', 'Session', 'Class', 'Size', 'Max']]
        sessions = subset_df.groupby('Session').agg({'Class': 'count', 'Size': 'sum', 'Max': 'sum'}).reset_index()
        return dash_table.DataTable(sessions.to_dict('records'), [{'name': i, 'id': i} for i in sessions])
    else:
        subset_df = df[['Dept', 'Session', 'Class', 'Size', 'Max']]
        subset_dff = subset_df[subset_df['Dept'] == dept]
        modalities = subset_dff.groupby('Session').agg({'Class': 'count', 'Size': 'sum', 'Max': 'sum'}).reset_index()
        return dash_table.DataTable(modalities.to_dict('records'), [{'name': i, 'id': i} for i in modalities])



app.run(debug='True')