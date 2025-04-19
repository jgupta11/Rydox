import pandas as pd
from datetime import datetime

class PaperTrader:
    def __init__(self, df, predictions, symbol):
        self.df = df.reset_index()
        self.predictions = predictions
        self.symbol = symbol
        self.trades = []

    def run(self):
        for i in range(len(self.df) - 1):
            if self.predictions[i] == 1:  # Buy signal
                buy_time = self.df.loc[i, 'Datetime']  # Include the exact timestamp for intraday
                buy_price = self.df.loc[i, 'Close']
                sell_price = self.df.loc[i + 1, 'Close']  # Sell on next time step (for simplicity)
                sell_time = self.df.loc[i + 1, 'Datetime']
                profit = round(sell_price - buy_price, 2)  # Profit calculation

                trade = {
                    "Datetime": sell_time,
                    "Symbol": self.symbol,
                    "Buy Price": buy_price,
                    "Sell Price": sell_price,
                    "Profit": profit
                }
                self.trades.append(trade)

        self.save_trades()

    def save_trades(self):
        df_trades = pd.DataFrame(self.trades)
        df_trades.to_csv("paper_trades.csv", index=False)
        print(f"{len(self.trades)} trades written to paper_trades.csv")
