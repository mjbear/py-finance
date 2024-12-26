import pandas as pd
import quantstats_lumi as qs

qs.extend_pandas()

df = pd.read_csv('test.csv', names=['date', 'price'], 
                 index_col=['date'], parse_dates=['date'])[100:]
#df['returns'] = df['price'].pct_change()

qs.plots.snapshot(df['price'], title='Stock Performance', show=True)

report = qs.reports.html(df['price'], title='Stock Trading Performance Report', output='rep.html')

#print(report)