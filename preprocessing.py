def preprocess_data(df, ticker=None):
    if ticker:
        close = df['Close'][ticker]
    else:
        close = df['Close'].iloc[:, 0]
    return close.dropna()
