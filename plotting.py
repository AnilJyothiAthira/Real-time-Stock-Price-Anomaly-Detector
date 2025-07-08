import matplotlib.pyplot as plt

def plot_anomalies(prices, anomalies, stock):
    plt.figure(figsize=(12, 6))
    plt.plot(prices.index, prices.values, label='Close Price')

    if anomalies:
        times = [ts for ts, _, _ in anomalies]
        values = [price for _, price, _ in anomalies]
        plt.scatter(times, values, color='red', label='Anomalies', marker='o', s=100)

    plt.title(f'{stock} Closing Prices with Anomalies')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
