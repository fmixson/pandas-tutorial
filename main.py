import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/flmix/OneDrive/Documents/Data Sheets/Division_Enrollment.csv', encoding='Latin')
pd.set_option('display.max_columns', None)
# departments = df['Dept'].unique()
scheduling_df = pd.DataFrame()

class Dataframe():

    def __init__(self, df):
        self.df = df


    def get_times_days(self):
        amtimes = []
        times = self.df['Start'].unique()
        timesList = times.tolist()
        new_list  = [item for item in timesList if not(pd.isnull(item))]
        for item in new_list:
            if 'am' in item:
                amtimes.append(item)
            else:
                if len(item) > 6:
                    item2 = item[:5]
                else:
                    item2 = item[:4]
                print(item2)
        amtimes.sort()
        print('amtimes', amtimes)
        new_list.sort()
        print('new list', new_list)
        times = new_list

        days = self.df['Days'].unique()
        return times, days

    def set_columns_index(self):
        scheduling_df = pd.DataFrame(columns=times,index=days)
        return scheduling_df

class FillingDataframe:

    def __init__(self, df, scheduling_df, times, days):
        self.df = df
        self.schedule_df = scheduling_df
        self.times = times
        self.days = days

    def count_sections(self):
        print('count sections', type(self.df))
        for day in days:
            for time in times:
                section_count = 0
                for i in range(len(self.df) - 1):
                    if (self.df.loc[i, 'Days'] == day) & (self.df.loc[i, 'Start'] == time):
                        section_count += 1
                scheduling_df.loc[day, time] = section_count
                print(scheduling_df)

d = Dataframe(df)
times, days = d.get_times_days()
scheduling_df = d.set_columns_index()
f = FillingDataframe(df=df, scheduling_df=scheduling_df, times=times, days=days)
f.count_sections()




# for department in departments:
#     dept = df[df['Dept'] == department]
#     # print(dept)
#
# days = df['Days'].unique()
# # print(days)
# count = 0
# for day in days:
#      dy = df[df['Days']==day]
#      startTimes = dy['Start'].unique()
#      # print(startTimes)
#      for start in startTimes:
#         time_df = dy[dy['Start']==start]
#         print(f'{day} has {len(time_df.index)} sections at {start}')
#         count = count + 1