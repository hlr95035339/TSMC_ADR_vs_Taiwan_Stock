import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 下載資料
adr = yf.download("TSM", start="2020-01-01", end="2026-04-22")
tw = yf.download("2330.TW", start="2020-01-01", end="2026-04-22")
fx = yf.download("TWD=X", start="2020-01-01", end="2026-04-22")

# 取收盤價 Series
adr_close = adr['Close'].squeeze()
tw_close = tw['Close'].squeeze()
fx_close = fx['Close'].squeeze()

# 建立比較用 DataFrame
df = pd.DataFrame({
    'ADR_Close': adr_close,
    'TW_Close_USD': tw_close / fx_close
}).dropna()

# 計算相關係數
corr = df.corr().iloc[0,1]
print(f"ADR vs 台股 (美元計價) 的相關係數: {corr:.2f}")

# 畫折線圖
plt.figure(figsize=(12,6))
plt.plot(df.index, df['ADR_Close'], label='TSMC ADR (USD)')
plt.plot(df.index, df['TW_Close_USD'], label='TSMC Taiwan (USD)')
plt.title("TSMC ADR vs Taiwan Stock (2020–2026)")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.show()

df.to_csv("tsmc_comparison.csv")
