from dash import Dash, dash_table, html, dcc
import pandas as pd
import dash_bootstrap_components as dbc


df = pd.read_csv('C:/Users/flmix/OneDrive/Documents/Data Sheets/Division_Enrollment.csv', encoding='Latin')
pd.set_option('display.max_columns', None)


subset_df = df[['Dept', 'Course', 'Class', 'Size', 'Max', 'FTES']]

df2 = subset_df.groupby('Course').agg({'Class': 'count','Size': 'sum','Max': 'sum', 'FTES': 'sum'}).reset_index()
df3 = subset_df.groupby('Dept').agg({'Class': 'count','Size': 'sum','Max': 'sum', 'FTES': 'sum'}).reset_index()

app = Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)
app.layout = html.Div(
    [
        dbc.Row(dbc.Col(html.Div('A Single Column'))),
        dbc.Row([
            dbc.Col(html.Div(dash_table.DataTable(df3.to_dict('records'), [{'name': i, 'id': i} for i in df3.columns]),), width=4
                    ),
            dbc.Col(html.Div(dash_table.DataTable(df2.to_dict('records'), [{'name': i, 'id': i} for i in df2.columns])), width=6),
            dbc.Col(html.Div('One of three columns'))
        ]),
        dbc.Row([
            dbc.Col(html.Div(dash_table.DataTable(df3.to_dict('records'), [{'name': i, 'id': i} for i in df3.columns]),
                             )),
            dbc.Col(html.Div('One of three columns'))
        ])
    ]
)



# app.layout = dbc.Container(html.Div(
#     [
#         dbc.Row(dbc.Col(html.Div(dash_table.DataTable(df3.to_dict('records'), [{'name': i, 'id': i} for i in df3.columns]),
#                  className='six columns',
#                  ))),
#         dbc.Alert(
#             'Course Enrollment Table', style={'textAlign': 'center'}, color='success'
#         ),
#     html.Div(dash_table.DataTable(df2.to_dict('records'), [{'name': i, 'id': i} for i in df2.columns]))
# ]))

app.run(debug=True)


