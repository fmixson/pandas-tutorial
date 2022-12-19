import numpy as np
import pandas as pd
import openpyxl
import plotly.express as px

df = pd.read_csv('C:/Users/flmix/OneDrive/Documents/Data Sheets/Liberal Arts Enrollment.csv', encoding='Latin')
pd.set_option('display.max_columns', None)
df.sort_values(by=['Employee ID', 'Course'], inplace=True)
print(df)
df = df[df['Enrollment Drop Date'].isnull()].reset_index()
for i in range(len(df)-1):
    print(i, len(df))
    if df.loc[i, 'Employee ID'] == df.loc[i+1, 'Employee ID']:
        if df.loc[i, 'Course'] == df.loc[i+1, 'Course']:
            df.loc[i,'Instruction Mode Description'] = 'Laboratory'
df = df[df['Instruction Mode Description'] != 'Laboratory']
df['Enrollment Add Date'] = pd.to_datetime(df['Enrollment Add Date'], infer_datetime_format=True)
df.to_excel('test_sheet.xlsx')
# print(df)
subset_df = df[['Enrollment Add Date', 'Course']]
group_dates = subset_df.groupby('Enrollment Add Date').count().reset_index()


day_count = 1
week_count = 1
for i in range(len(group_dates)):
    if day_count < 7:
        group_dates.loc[i, 'Week'] = 'Week ' + str(week_count)
        day_count += 1
    else:
        group_dates.loc[i, 'Week'] = 'Week ' + str(week_count)
        day_count = 1
        week_count += 1


group_weeks = group_dates.groupby('Week').agg({'Course': 'sum'}).reset_index()
print(type(group_weeks))
group_weeks.loc[0,'Total'] = group_weeks.loc[0, 'Course']
for i in range(1, len(group_weeks)):
    group_weeks.loc[i, 'Total'] = group_weeks.loc[i, 'Course'] + group_weeks.loc[i-1, 'Total']
print(group_weeks)

fig = px.line(group_weeks, x=group_weeks['Week'], y=group_weeks['Total'])
fig2 = px.scatter(group_dates, x=group_dates['Enrollment Add Date'], y=group_dates['Course'])
fig.show()
fig2.show()