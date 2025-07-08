import time
from api_client import fetch_stock_data
from preprocessing import preprocess_data
from anomaly_detector import detect_zscore_anomalies
from alert_system import send_alert
from plotting import plot_anomalies

def main():
    stock_list = ['AAPL', 'GOOGL', 'AMZN', 'TSLA']

    while True:
        for stock in stock_list:
            print(f"\n📈 Monitoring {stock}...")
            df = fetch_stock_data(stock, period='5d', interval='60m')
            if df.empty:
                print(f"No data for {stock}")
                continue

            prices = preprocess_data(df, ticker=stock)
            anomalies = detect_zscore_anomalies(prices)

            if anomalies:
                send_alert(stock, anomalies)
                plot_anomalies(prices, anomalies, stock)
            else:
                print(f"No anomalies detected for {stock}")

        print("\n⏳ Waiting for 1 hour before next check...\n")
        time.sleep(3600)

if __name__ == "__main__":
    main()
