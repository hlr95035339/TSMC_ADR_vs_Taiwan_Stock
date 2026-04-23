# TSMC ADR vs Taiwan Stock Market Analysis 

## Project Overview
Why does TSMC ADR trade at a premium over Taiwan-listed shares?

---

## Key Insights
- ADR premium averages 15–25%
- Spread is persistent
- Influenced by FX and US market sentiment








## Overview
This project compares TSMC ADR (NYSE: TSM) and TSMC Taiwan-listed shares (2330.TW) from 2020 to 2026, analyzing cross-market dynamics and exchange rate effects.

---
## Data
- Source: Yahoo Finance (TSM, 2330.TW)
- Period: 2020-01-01 to 2026-04-22
- Variables: Closing price, trading volume, USD/TWD exchange rate

## Methods
- Data cleaning and alignment with Python (main.py)
- Currency conversion for Taiwan stock prices
- Correlation analysis between ADR and Taiwan shares
- Visualization with matplotlib / Tableau

-----

## Visualizations
![TSMC_ADR_vs_Taiwan_Stock Dashboard](Dashboard_1.png)


👉 [View Interactive Dashboard on Tableau Public](https://public.tableau.com/views/TSMCADRvsTaiwanStockMarketAnalysis20202026/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

----
## Insights
- ADR and Taiwan shares show strong correlation (>0.9).
- Exchange rate fluctuations create short-term gaps.
- US investors focus on earnings calls, while Taiwan investors emphasize 法說會.
- Long-term trend (2020–2026) highlights resilience during global crises and AI boom.
----
## Skills Demonstrated
- Python data analysis (main.py)
- Tableau dashboard design
- Financial market comparison and business insight generation

---

## Data (2020-2026)
- Taiwan Stock Exchange (2330)
- NYSE ADR (TSM)
- USD/TWD exchange rate

---

## Methodology
Spread = (ADR × 5 × FX) - TW price

---

## Analysis
- Time series comparison
- Spread distribution
- Rolling statistics

---

## Modeling
- Regression on spread drivers
- Optional: Z-score signal

---

## Trading Implications
- Potential mean reversion
- Arbitrage limitations exist

---

## Tools
- Python (Pandas, Matplotlib)



