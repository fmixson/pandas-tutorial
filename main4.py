import plotly.express as px
import pandas as pd


df = pd.read_csv('C:/Users/flmix/OneDrive/Documents/Data Sheets/Division_Enrollment.csv', encoding='Latin')
# dept_df = df[df['Dept'] == 'ASL']
# size_df = df.groupby('Dept').Size.sum().reindex()
# print(size_df)
# df2 = pd.DataFrame(data=size_df)
print(df.head())
subset_df = df[['Dept', 'Course', 'Modality', 'Size', 'Max', 'FTES']]
comm_df = subset_df[subset_df['Dept'] == 'COMM']
print(comm_df)
df2 = comm_df.groupby('Course').agg({'Modality': 'count', 'Size': 'sum','Max': 'sum', 'FTES': 'sum'})
df3 = comm_df.groupby('Modality').agg({'Course': 'count','Size': 'sum', 'Max': 'sum'})
df4 = comm_df.groupby('Modality').agg({'Course': 'count','Size': 'sum', 'Max': 'sum'})
total_modality = df3['Course'].sum()
df3['Perc'] = df3['Course'] / total_modality

print(total_modality)

df2['Fill']=df2['Size'] / df2['Max']
df4['Fill']=df4['Size'] / df4['Max']
df2['Rev'] = df2['FTES'] * 4000
print(df2)
print(df3)
print(df4)
# fig = px.line(x=[size_df['Dept'], y=size_df['Size'], title='sample figure')
# print(fig)
# fig.show()