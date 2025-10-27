import yfinance as yf
import pytz

symbol = "DX-Y.NYB"

data = yf.download(
    tickers=symbol,
    period="1d",
    interval="1m",
    auto_adjust=False
)

# Get last row cleanly
ltp = data["Close"].iloc[-1].item()   # convert to plain float
timestamp = data.index[-1]

# Convert timestamp to New York time
ny_tz = pytz.timezone("America/New_York")
timestamp_ny = timestamp.tz_convert(ny_tz)

print(f"\n\nLTP: {ltp}")
print(f"Timestamp: {timestamp_ny}")
