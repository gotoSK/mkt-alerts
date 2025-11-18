import yfinance as yf
import pytz
import time
import os

symbol = "DX-Y.NYB"
target_price = 98.300

ny_tz = pytz.timezone("America/New_York")

while True:
    data = yf.download(
        tickers=symbol,
        period="1d",
        interval="1m",
        auto_adjust=False
    )

    ltp = data["Close"].iloc[-1].item()
    timestamp = data.index[-1].tz_convert(ny_tz)

    print(f"LTP: {ltp}")
    print(f"Timestamp: {timestamp}")

    if ltp >= target_price:
        print("🚨 ALERT: Price touched target!")
        # cross-platform beep
        try:
            os.system("echo -n '\a';sleep 0.2;echo -n '\a'")
        except:
            pass
        break  # stop loop after alert

    time.sleep(60)  # check every 1 minute
