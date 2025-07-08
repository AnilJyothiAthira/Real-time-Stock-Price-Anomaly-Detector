def detect_zscore_anomalies(prices, threshold=2.0):
    import pandas as pd

    if not hasattr(prices, '__iter__'):
        raise TypeError(f"Expected iterable for prices but got {type(prices)}")

    prices = pd.to_numeric(prices, errors='coerce').dropna()
    # rest unchanged

    mean = prices.mean()
    std = prices.std()
    z_scores = (prices - mean) / std

    anomalies = [
        (ts, price, z)
        for ts, price, z in zip(prices.index, prices, z_scores)
        if abs(z) > threshold
    ]
    return anomalies
