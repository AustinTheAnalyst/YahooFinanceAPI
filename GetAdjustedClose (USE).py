import yfinance as yf
import pandas as pd

# Ticker symbol of the stock you're interested in
ticker_symbol = ['^J403.JO','^J210.JO','^J213.JO','^J200.JO','MXWO.L','^J253.JO','^J203.JO','ZAR=X','ZARUSD=X','^J211.JO','^J400.JO','^J433.JO','^J430.JO','GC=F','^990100-USD-STRD','EEM','WDSC.L','SPYX.DE','SYGP.JO','GLAB.L','EBND']  

# Define the start and end dates for the historical data
start_date = '2023-07-30'
end_date = '2023-11-30'

# Fetch historical data
stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Resample the data to monthly frequency and select the last day of each month
monthly_returns = stock_data['Adj Close'].resample('M').last().pct_change()

# Sort the monthly returns by descending date
monthly_returns = monthly_returns.sort_index(ascending=False)

# Export to Excel
excel_filename = 'SeptToNov_YFreturns_data.xlsx'
monthly_returns.to_excel(excel_filename)

# Print or analyze the monthly returns
print(monthly_returns)
print(f"\nMonthly returns data has been exported to {excel_filename}")
