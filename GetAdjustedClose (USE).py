import yfinance as yf
import pandas as pd

# Ticker symbol of the stock you're interested in
ticker_symbol = ['^J403.JO','^J210.JO','^J213.JO','^J200.JO','MXWO.L','^J253.JO','^J203.JO','ZAR=X','ZARUSD=X','^J211.JO','^J400.JO','^J433.JO','^J430.JO','GC=F','^990100-USD-STRD','EEM','WDSC.L','SPYX.DE','SYGP.JO','GLAB.L','EBND','EURZAR=X','GBPZAR=X']
start_date = '2023-02-28'
end_date = '2023-12-31'

# Download adjusted closing prices for the specified date range
stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)['Adj Close']

# Resample to get monthly adjusted closing prices
monthly_prices = stock_data.resample('M').last()

# Export to Excel if needed
excel_filename = 'TotalReturns.xlsx'
monthly_prices.to_excel(excel_filename)

# Print or analyze the adjusted closing prices
print(monthly_prices)
print(f"\nAdjusted closing prices data for the date range {start_date} to {end_date} has been exported to {excel_filename}")
