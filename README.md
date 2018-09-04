# MachineLearning
To add Code related to Machine Learning and Deep Learnings

dollar_file ='Input/USD_INR Historical Data - Copy.csv' 
dd = pd.read_csv(dollar_file, header=0,index_col=False,delimiter ='\t') 

dd=dd[['Date','Price']] 
data = define_input(filepath)
input_field = 'Close' 
df2 = build_split_data(data,input_field)

dd['Date'] =dd[dd.Date >=min(df2.Date)]
df3=df2.join(dd.set_index('Date'), on='Date')

