from dash import Dash, dash_table, html, dcc, Input, Output
import pandas as pd
import dash_bootstrap_components as dbc

df = pd.read_csv('C:/Users/flmix/OneDrive/Documents/Data Sheets/Division_Enrollment.csv', encoding='Latin')



app = Dash(__name__)
app.layout = html.Div(
    [
        dcc.Dropdown(id='dept',
                     options=[{'label': dept, 'value': dept}
                              for dept in df['Dept'].unique()]),
        dcc.Checklist(id='my_check',
                      options=[{'lable': sessions, 'value': sessions}
                               for sessions in df['Session'].unique()],
                      value=['Regular Session (8/15/2022 - 12/16/2022)']
                      ),
        html.Br(),
        dbc.Row([
            dbc.Col(html.Div(id='report'))
        ])
    ]
)

@app.callback(
    Output(component_id='report', component_property='children'),
    Input(component_id='dept', component_property='value'),
    Input(component_id='my_checklist', component_property='value')
)
def display_update_output(dept, session):

    if dept is None:
        filtered_df = df[df['Session'] == session]
        return html.Div(children=dash_table.DataTable(filtered_df.to_dict('records'), [{'name': i, 'id': i} for i in filtered_df.columns]))

    dept_table = df[(df['Dept'] == dept) & (df['Session'] == 'Regular Session (8/15/2022 - 12/16/2022)')]
    return html.Div(children=dash_table.DataTable(dept_table.to_dict('records'), [{'name': i, 'id': i} for i in dept_table.columns]))

app.run(debug=True)