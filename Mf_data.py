import yfinance as yf
import pandas as pd

nse_mf_df = pd.read_excel('/kaggle/input/nse-mf-list/nsccl_cm_ann_mf.xlsx')

df = pd.DataFrame()  # Create an empty DataFrame

for isin in nse_mf_df.ISIN:
 try:
     mf_info = yf.Ticker(isin).info
     tckr_df = pd.DataFrame([mf_info])  # Create a DataFrame
     df = df.append(tckr_df, ignore_index=True, sort=False)  # Append the DataFrame
 except:
     pass

df.to_csv('All_mf_data.csv', index=False)
