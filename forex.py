import yfinance as yf
import pandas as pd
import mplfinance as mpf
# data = yf.download('NVDA', start='2020-01-01', end='2024-07-01')
# mpf.plot(data.tail(100),type='candle',style='yahoo',volume=True)

forex_data_gbp_usd = yf.download('GBPUSD=X', start='2019-01-02', end='2023-12-31')
forex_data_usd_gbp = yf.download('GBP=X', start='2019-01-02', end='2023-12-31')

# # Set the index to a datetime object
forex_data_gbp_usd.index = pd.to_datetime(forex_data_gbp_usd.index)
forex_data_usd_gbp.index = pd.to_datetime(forex_data_usd_gbp.index)

# # Display the last five rows
print(forex_data_gbp_usd.tail())
print(forex_data_usd_gbp.tail())
