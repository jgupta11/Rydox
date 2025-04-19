import yfinance as yf

class DataLoader:
    def __init__(self, symbol, interval='1m', period='1d'):
        self.symbol = symbol
        self.interval = interval
        self.period = period

    def fetch_data(self):
        print(f"Fetching data for {self.symbol} with {self.interval} intervals.")
        df = yf.download(tickers=self.symbol, interval=self.interval, period=self.period, progress=False)
        df.dropna(inplace=True)
        return df
