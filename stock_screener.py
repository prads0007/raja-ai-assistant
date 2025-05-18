import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
from googlesearch import search
from textblob import TextBlob

st.set_page_config(page_title="RAJA Stock Screener", layout="wide")
st.title("📈 RAJA - Small Cap Value Stock Screener")

st.markdown("This screener finds potential long-term multi-bagger small-cap stocks based on value investing criteria and sentiment analysis.")

# ----------------------------
# Sample NSE stock list (you can expand this with a full NSE list from APIs or CSV)
stocks = {
    "TATVA": "TATVA CHINTAN PHARMA CHEM LIMITED",
    "CLEAN": "CLEAN SCIENCE AND TECHNOLOGY LIMITED",
    "KIMS": "KIMS HOSPITALS",
    "GPIL.NS": "GODAWARI POWER & ISPAT LIMITED",
    "IRB.NS": "IRB INFRASTRUCTURE DEVELOPERS LTD",
    "BCLIND.NS": "BCL INDUSTRIES LIMITED",
    "CENTURYTEX.NS": "CENTURY TEXTILES & INDUSTRIES",
    "CAPLIPOINT.NS": "CAPLIN POINT LABORATORIES"
}

results = []

with st.spinner("Analyzing stocks. Please wait..."):
    for symbol, name in stocks.items():
        try:
            data = yf.Ticker(symbol)
            info = data.info

            # Basic filters
            pe = info.get("trailingPE", 0)
            roe = info.get("returnOnEquity", 0) * 100
            eps_growth = info.get("earningsQuarterlyGrowth", 0) * 100
            market_cap = info.get("marketCap", 0)
            debt_to_equity = info.get("debtToEquity", 1)

            # Criteria filters
            if 500e7 < market_cap < 5000e7 and pe < 20 and roe > 12 and eps_growth > 10 and debt_to_equity < 1:
                # Sentiment analysis
                headlines = []
                query = name + " stock news"
                for j in search(query, num_results=5):
                    headlines.append(j)

                polarity_scores = []
                for url in headlines:
                    try:
                        blob = TextBlob(url)
                        polarity_scores.append(blob.sentiment.polarity)
                    except:
                        polarity_scores.append(0)

                avg_sentiment = round(sum(polarity_scores) / len(polarity_scores), 2)

                results.append({
                    "Symbol": symbol,
                    "Company": name,
                    "P/E": round(pe, 2),
                    "ROE %": round(roe, 2),
                    "EPS Growth %": round(eps_growth, 2),
                    "Debt to Equity": round(debt_to_equity, 2),
                    "Sentiment Score": avg_sentiment
                })
        except:
            continue

if results:
    df = pd.DataFrame(results)
    df = df.sort_values(by=["Sentiment Score", "ROE %"], ascending=False)
    st.success(f"✅ Found {len(df)} potential small-cap value stocks!")
    st.dataframe(df, use_container_width=True)

    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Top Picks as CSV", csv, "RAJA_Top_Stocks.csv", "text/csv")
else:
    st.warning("No stocks matched your strict value criteria today. Try relaxing some conditions or check again tomorrow.")
