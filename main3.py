from drop import Dash, dash_table
import plotly.express as px
import pandas as pd

df = pd.read_csv('C:/Users/flmix/OneDrive/Documents/Data Sheets/Division_Enrollment.csv', encoding='Latin')
dept_df = df[df['Dept'] == 'ASL']
Size = dept_df.groupby('Course').sum()

app = Dash(__name__)
app.layout = dash_table.DataTable(dept_df.to_dict('records'), [{'name': i, 'id': i} for i in df.columns])
fig = px.bar(dept_df, x='Size')
print(fig)

if __name__ == '__main__':
    app.run(debug=True)