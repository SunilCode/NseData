# Download NSE Market data
import yfinance as yf
import pandas as pd

nse_tickers_df = pd.read_csv('/kaggle/input/nsetickerlist/NSE_EQUITY_List.csv')
nse_tickers_df['SYMBOL'] = nse_tickers_df['SYMBOL'].astype(str) + '.NS'

df = pd.DataFrame()  # Create an empty DataFrame

for ticker in nse_tickers_df.SYMBOL:
    tckr_info = yf.Ticker(ticker).info
    tckr_df = pd.DataFrame([tckr_info])  # Create a DataFrame
    df = pd.concat([df, tckr_df], axis=0, ignore_index=True, sort=False)  # Concatenate the DataFrames

df.to_csv('All_ticker_data.csv', index=False)
