import pandas as pd
import plotly.graph_objects as go

# path to MT5 csv source file
infile = '24-28.csv'

# rename columns
colnames = ['Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Tickvol', 'Vol', 'Spread']
stocks = pd.read_csv(infile, sep='\t', parse_dates=[['Date', 'Time']], header=0, names=colnames)

# make a new column with plotly friendly date
stocks['Date'] = stocks.Date_Time.dt.strftime('%Y.%m.%d %H:%M:%S')
stocks = stocks.to_records(index=False)

fig = go.Figure(data=[go.Candlestick(name='Price', x=stocks['Date'], open=stocks['Open'], high=stocks['High'], low=stocks['Low'], close=stocks['Close'])])


fig.update_layout(
            xaxis_rangeslider_visible=True,
            title='MT5 data viewer',
            yaxis_title='Price')
fig.show()

