import pandas as pd
import dash
from dash import Dash, dcc, html, Input, Output, dash_table
import plotly.express as px

df = pd.read_csv('C:/Users/flmix/OneDrive/Documents/Data Sheets/Division_Enrollment.csv', encoding='Latin')
unique_df = df['Session'].unique()
unique_dff = unique_df.tolist()
split_unique_df = [x.split()[0] for x in unique_dff]
checklist = []
for x in split_unique_df:
    if x not in checklist:
        checklist.append(x)
print(split_unique_df)
print(type(unique_df))
app = Dash(__name__)

app.layout = html.Div([
    html.Div([
    dcc.Checklist(
        id='my_checklist',
        options=[
            {'label': x, 'value': x, 'disabled': False}
            for x in checklist
        ],
        value=['Regular Session (8/15/2022 - 12/16/2022)'],

        className='my_box_container',
        style={'display': 'flex'},

        inputClassName='my_box_input',
        inputStyle={'cursor': 'pointer'},

        labelClassName='my_box_label',
        labelStyle={'background': '#A5D6A7',
                    'padding': '0.5rem 1rem',
                    'border-radius': '0.5rem'},
    ),
    html.Div(id='enrollment_sheet')
]),])


@app.callback(
    Output(component_id='enrollment_sheet', component_property='children'),
    Input(component_id='my_checklist', component_property='value')
)

def update_enrollment_sheet(options_chosen):
    dff = df[df['Session'].isin(options_chosen)]
    return html.Div(children=dash_table.DataTable(dff.to_dict('records'), [{'name': i, 'id': i} for i in dff.columns]))

if __name__ == '__main__':
    app.run(debug=True)