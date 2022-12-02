import pandas as pd

df = pd.read_csv('C:/Users/flmix/OneDrive/Documents/Data Sheets/Enrollment Counts - table (1).csv', encoding='Latin')
pd.set_option('display.max_columns', None)

df.fillna(0, inplace=True)
df = df.replace(',', '', regex=True)
df[['Spring 2017', 'Spring 2018', 'Spring 2019', 'Spring 2020', 'Spring 2021', 'Spring 2022']] = df[['Spring 2017','Spring 2018', 'Spring 2019', 'Spring 2020', 'Spring 2021', 'Spring 2022']].astype(str).astype(int)
print(df)
# convert_dict = {'Spring 2017': int, 'Spring 2018': int, 'Spring 2019': int,
#                                             'Spring 2020': int, 'Spring 2021': int, 'Spring 2022': int}

division_totals = df.groupby('Division').agg({'Spring 2017': 'sum','Spring 2018': 'sum', 'Spring 2019': 'sum',
                                            'Spring 2020': 'sum', 'Spring 2021': 'sum', 'Spring 2022': 'sum'}).reset_index()
division_totals_series = division_totals.iloc[0]
division_totals_list = division_totals_series.values.tolist()
division_index_list = division_totals_series.index.values.tolist()
years = division_index_list[1:]
enrollments = division_totals_list[1:]

print(division_totals)

print(enrollments
      )
print(years)


dept_df = df[df['Department'] == 'COMM']
courses = dept_df['Course'].unique()
dept_totals_df = df.groupby('Division')



# print(df.dtypes)