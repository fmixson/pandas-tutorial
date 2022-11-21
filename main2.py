import pandas as pd

df = pd.read_csv('C:/Users/flmix/OneDrive/Documents/Data Sheets/Division_Enrollment.csv', encoding='Latin')
pd.set_option('display.max_columns', None)
div_df = df[df['Size'] < 10]
print(div_df)

modalities = df.groupby('Room').Size.sum()
# print(modalities)

enrollment_df2 = df.groupby('Start').Room.count()
enrollment_df = df.groupby('Days').Start.count()
# days = []
depts = df['Dept'].unique()
for dept in depts:
    dept_df = df[df['Dept'] == dept]
    dept_modalities = dept_df.groupby('Room').agg({'Course': 'count', 'Size': 'sum', 'Max': 'sum', 'WaitAv': 'sum'})

    # low_enrolled = dept_df[dept_df['Size'] < 10]
    # sections = day_time_df.groupby('Start').count()
    print(dept, dept_modalities)

