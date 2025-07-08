import yfinance as yf

def fetch_stock_data(ticker, period="1mo", interval="1d"):
    df = yf.download(ticker, period=period, interval=interval, progress=False, auto_adjust=True)
    df.dropna(inplace=True)
    return df
