import pandas as pd

class FeatureEngineer:
    def __init__(self, df):
        self.df = df

    def compute_rsi(self, data, window=14):
        delta = data.diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        
        avg_gain = gain.rolling(window=window).mean()
        avg_loss = loss.rolling(window=window).mean()
        
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def add_features(self):
        df = self.df.copy()
        df['Price_Change'] = df['Close'].pct_change()
        df['SMA_3'] = df['Close'].rolling(window=3).mean()  # Short-term SMA for intraday
        df['SMA_10'] = df['Close'].rolling(window=10).mean()  # Longer-term SMA
        df['RSI'] = self.compute_rsi(df['Close'], 14)  # 14-period RSI
        df['Target'] = df['Close'].shift(-1) > df['Close']
        df['Target'] = df['Target'].astype(int)
        df.dropna(inplace=True)
        return df
