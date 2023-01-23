import numpy as np
import pandas as pd
import openpyxl
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('C:/Users/flmix/OneDrive/Documents/Data Sheets/Liberal Arts Enrollment.csv', encoding='Latin')
pd.set_option('display.max_columns', None)
df.sort_values(by=['Employee ID', 'Course'], inplace=True)
# print(df.to_string())
df = df[df['Enrollment Drop Date'].isnull()].reset_index()
for i in range(len(df)-1):
    # print(i, len(df))
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
week_of = {}
for i in range(len(group_dates)):
    if day_count < 7:
        # if day_count == 1:
        #     if str(week_count) not in week_of:
        #         week_of[week_count] = group_dates[i, 'Enrollment Add Date']
        #         print(week_of)

        group_dates.loc[i, 'Week'] = week_count
        # print(group_dates)
        day_count += 1
    else:
        group_dates.loc[i, 'Week'] = week_count
        # group_dates.loc[i, 'Week of'] = week_of_date
        day_count = 1
        week_count += 1


group_weeks = group_dates.groupby('Week').agg({'Course': 'sum'}).reset_index()
# print( group_weeks)
# print(type(group_weeks))
# print(group_weeks.dtypes)
# group_weeks.columns=['Week', 'Course']
group_weeks.loc[0,'Total'] = group_weeks.loc[0, 'Course']
for i in range(1, len(group_weeks)):
    group_weeks.loc[i, 'Total'] = group_weeks.loc[i, 'Course'] + group_weeks.loc[i-1, 'Total']

sessions_df = group_weeks.rename(columns={'Total': 'Division'})
sessions_df = sessions_df.drop('Course', axis=1)
# sessions_df.loc[0: ,'Division'] = group_weeks.loc[0: ,'Total']
# sessions_df = group_weeks['Total']
# print(group_weeks)
print('sessions', sessions_df.head())

sessions = ['1', '15L', '15B', '9A', '9B', '6A', '6B', '6C']
for session in sessions:
    session_df = df[df['Session Code'] == session]
    subset_df = session_df[['Enrollment Add Date', 'Session Code', 'Course']]
    group_dates = subset_df.groupby('Enrollment Add Date').count().reset_index()


    day_count = 1
    week_count = 1
    for i in range(len(group_dates)):
        if day_count < 7:
            group_dates.loc[i, 'Week'] = week_count
            day_count += 1
        else:
            group_dates.loc[i, 'Week'] = week_count
            day_count = 1
            week_count += 1

    group_weeks = group_dates.groupby('Week').agg({'Course': 'sum'}).reset_index()
    # print(type(group_weeks))
    group_weeks.loc[0, 'Total'] = group_weeks.loc[0, 'Course']
    for i in range(1, len(group_weeks)):
        group_weeks.loc[i, 'Total'] = group_weeks.loc[i, 'Course'] + group_weeks.loc[i - 1, 'Total']
        sessions_df[session] = group_weeks['Total']
        # print('sessions', sessions_df)
    # if session == '1':
    #     print(group_weeks)
    #     sessions_df['Regular'] = group_weeks['Total']
    #
    # elif session == '15A':
    #     print(group_weeks)
    #     sessions_df['15A'] = group_weeks['Total']
    #
    # elif session == '15B':
    #     print(group_weeks)
    #     sessions_df['15B'] = group_weeks['Total']
    #
    # elif session == '9A':
    #     print(group_weeks)
    #     sessions_df['9A'] = group_weeks['Total']
    #
    # elif session == '9B':
    #     print(group_weeks)
    #     sessions_df['9B'] = group_weeks['Total']
    #
    # elif '6' in session:
    #     print(group_weeks)
    #     sessions_df['6'] = group_weeks['Total']

# """
# THIS SECTION IDENTIFIES TREND BY MODALITY
# """
#
# modalities = ['Online', 'In Person', 'Hybrid', 'Remote']
# for modality in modalities:
#     modalities_df = df[df['Modality'] == session]
#     subset_df = modalities_df[['Enrollment Add Date', 'Modality', 'Course']]
#     group_dates = subset_df.groupby('Enrollment Add Date').count().reset_index()
#
#
#     day_count = 1
#     week_count = 1
#     for i in range(len(group_dates)):
#         if day_count < 7:
#             group_dates.loc[i, 'Week'] = week_count
#             day_count += 1
#         else:
#             group_dates.loc[i, 'Week'] = week_count
#             day_count = 1
#             week_count += 1
#
#     group_weeks = group_dates.groupby('Week').agg({'Course': 'sum'}).reset_index()
#     # print(type(group_weeks))
#     group_weeks.loc[0, 'Total'] = group_weeks.loc[0, 'Course']
#     for i in range(1, len(group_weeks)):
#         group_weeks.loc[i, 'Total'] = group_weeks.loc[i, 'Course'] + group_weeks.loc[i - 1, 'Total']
#         modalities_df[modality] = group_weeks['Total']


""" 
THIS SECTION IDENTIFIES TREND BY Race and Ethnicity
"""

ethnicities = ['Native Hawaiian or Other Pacific Islander', 'Asian', 'Black or African American', 'Hispanic or Latino', 'Two or More Races', 'Race/ethnicity Unknown',
'American Indian or Alaskan Native', 'Decline to State', 'White']
for ethnicity in ethnicities:
    ethnicity_df = df[df['Race/Ethnicity'] == ethnicity]
    subset_df = ethnicity_df.groupby('Enrollment Add Date').count().reset_index()
    # print(ethnicity, ethnicity_df)

    day_count = 1
    week_count = 1
    for i in range(len(group_dates)):
        if day_count < 7:
            group_dates.loc[i, 'Week'] = week_count
            day_count += 1
        else:
            group_dates.loc[i, 'Week'] = week_count
            day_count = 1
            week_count += 1
    # print(group_dates)
    group_weeks = group_dates.groupby('Week').agg({'Course': 'sum'}).reset_index()
    # print(type(group_weeks))
    group_weeks.loc[0, 'Total'] = group_weeks.loc[0, 'Course']
    for i in range(1, len(group_weeks)):
        group_weeks.loc[i, 'Total'] = group_weeks.loc[i, 'Course'] + group_weeks.loc[i - 1, 'Total']
        ethnicity_df[ethnicity] = group_weeks['Total']
    print('ethnicity', ethnicity_df.head())
ethnicity_fig = go.Figure()

# ethnicity_fig.add_trace(go.Scatter(x=ethnicity_df['Week'], y=ethnicity_df['Division'],
#                          mode='lines',
#                          name='Division'))

# ethnicity_fig.add_trace(go.Scatter(x=ethnicity_df['Week'], y=ethnicity_df['American Indian or Alaskan Native'],
#                          mode='lines',
#                          name='Online'))

ethnicity_fig.add_trace(go.Scatter(x=ethnicity_df['Week'], y=ethnicity_df['Asian'],
                         mode='lines',
                         name='In Person'))

ethnicity_fig.add_trace(go.Scatter(x=ethnicity_df['Week'], y=ethnicity_df['Black or African American'],
                         mode='lines',
                         name='Hybrid'))

ethnicity_fig.add_trace(go.Scatter(x=ethnicity_df['Week'], y=ethnicity_df['Decline to State'],
                         mode='lines',
                         name='Remote'))

ethnicity_fig.add_trace(go.Scatter(x=ethnicity_df['Week'], y=ethnicity_df['Two or more Races'],
                         mode='lines',
                         name='Remote'))

ethnicity_fig.add_trace(go.Scatter(x=ethnicity_df['Week'], y=ethnicity_df['Native Hawaiian or Other Pacific Islander'],
                         mode='lines',
                         name='Remote'))

ethnicity_fig.add_trace(go.Scatter(x=ethnicity_df['Week'], y=ethnicity_df['Hispanic or Latino'],
                         mode='lines',
                         name='Remote'))

ethnicity_fig.add_trace(go.Scatter(x=ethnicity_df['Week'], y=ethnicity_df['Hispanic or Latino'],
                         mode='lines',
                         name='Remote'))

#     
#  
# modality_fig = go.Figure()
#
# modality_fig.add_trace(go.Scatter(x=modalities_df['Week'], y=modalities_df['Division'],
#                          mode='lines',
#                          name='Division'))
#
# modality_fig.add_trace(go.Scatter(x=modalities_df['Week'], y=modalities_df['Online'],
#                          mode='lines',
#                          name='Online'))
#
# modality_fig.add_trace(go.Scatter(x=modalities_df['Week'], y=modalities_df['In Person'],
#                          mode='lines',
#                          name='In Person'))
#
# modality_fig.add_trace(go.Scatter(x=modalities_df['Week'], y=modalities_df['Hybrid'],
#                          mode='lines',
#                          name='Hybrid'))
#
# modality_fig.add_trace(go.Scatter(x=modalities_df['Week'], y=modalities_df['Remote'],
#                          mode='lines',
#                          name='Remote'))




fig = go.Figure()

fig.add_trace(go.Scatter(x=sessions_df['Week'], y=sessions_df['Division'],
                         mode='lines',
                         name='Division'))

fig.add_trace(go.Scatter(x=sessions_df['Week'], y=sessions_df['1'],
                         mode='lines',
                         name='Regular'))

# fig.add_trace(go.Scatter(x=sessions_df['Week'], y=sessions_df['15L'],
#                          mode='lines',
#                          name='15A'))

fig.add_trace(go.Scatter(x=sessions_df['Week'], y=sessions_df['15B'],
                         mode='lines',
                         name='15B'))

fig.add_trace(go.Scatter(x=sessions_df['Week'], y=sessions_df['9A'],
                         mode='lines',
                         name='9A'))

fig.add_trace(go.Scatter(x=sessions_df['Week'], y=sessions_df['9B'],
                         mode='lines',
                         name='9B'))

# fig.add_trace(go.Scatter(x=sessions_df['Week'], y=sessions_df['6'],
#                          mode='lines',
#                          name='6'))
# fig = px.line(sessions_df, x='Week', y='Division')
# fig.add_scatter(x=sessions_df['Week'], y=sessions_df['Regular'])
# fig.add_scatter(x=sessions_df['Week'], y=sessions_df['15A'])
# fig.add_scatter(x=sessions_df['Week'], y=sessions_df['15B'])
# fig.add_scatter(x=sessions_df['Week'], y=sessions_df['9A'])
# fig.add_scatter(x=sessions_df['Week'], y=sessions_df['9B'])
# fig.add_scatter(x=sessions_df['Week'], y=sessions_df['6'])
# fig.add_trace(go.Scatter(x=random_x, y=random_y0,
#                     mode='lines',
#
#                     name='lines'))


fig.show()
# generate scatter plot


print(group_weeks)
print(sessions_df)



    # regular_fig = px.line(group_weeks, x=group_weeks['Week'], y=group_weeks['Total'])
    # regular_fig.show()


# fig = px.line(group_weeks, x=group_weeks['Week'], y=group_weeks['Total'])
# fig2 = px.scatter(group_dates, x=group_dates['Enrollment Add Date'], y=group_dates['Course'])
# fig.show()
# # fig2.show()