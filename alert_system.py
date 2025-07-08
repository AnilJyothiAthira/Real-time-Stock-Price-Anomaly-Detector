def send_alert(stock, anomalies):
    for ts, price, z in anomalies:
        print(f"🚨 Anomaly Detected in {stock} 🚨")
        print(f"Time: {ts}")
        print(f"Price: {price}")
        print(f"Z-Score: {z:.2f}\n")
