# Function to check and install required packages
def check_and_install_packages():
    from package_installer import PackageInstaller
    installer = PackageInstaller()
    installer.check_and_install_packages()

# Main application class
class StockPredictionApp:
    def __init__(self, symbol):
        self.symbol = symbol

    def run(self):
        from data_loader import DataLoader
        from feature_engineer import FeatureEngineer
        from xgboost_model import XGBoostModel
        from trainer import Trainer
        from paper_trader import PaperTrader

        # Fetch intraday data
        loader = DataLoader(self.symbol, interval='1m', period='1d')
        raw_df = loader.fetch_data()

        # Feature engineering
        fe = FeatureEngineer(raw_df)
        df = fe.add_features()

        # Prepare features and target
        features = df[['SMA_3', 'SMA_10', 'RSI', 'Price_Change']]
        target = df['Target']

        # Train XGBoost model
        model = XGBoostModel()
        trainer = Trainer(model, features, target)
        trained_model = trainer.train_and_evaluate()

        # Get predictions
        predictions = trained_model.predict(features)

        # Run paper trading
        trader = PaperTrader(df, predictions, self.symbol)
        trader.run()

        return trained_model

# Main script execution
if __name__ == "__main__":
    # Step 1: Ensure required packages are installed
    check_and_install_packages()

    # Step 2: Initialize and run stock prediction application
    app = StockPredictionApp("AAPL")  # Example: Apple stock symbol
    trained_model = app.run()