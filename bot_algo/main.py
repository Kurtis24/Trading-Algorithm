# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
    
  # def main(self):
  #   df1 = pd.read_csv('information_GOOGL.csv')
    
  #   # Convert "Date" columns to datetime
  #   df1['Date'] = pd.to_datetime(df1['Date'])
    
  #   plt.figure(figsize=(10,5))
    
  #   # Plot scatter of each
  #   plt.scatter(df1['Date'], df1['Volume'], c="red",   linewidth=2, label="GOOGL Volume")

  #   df1['Date_ordinal'] = df1['Date'].map(pd.Timestamp.toordinal)
    
  #   x = df1['Date_ordinal'].values.reshape(-1, 1)
  #   y = df1['Volume'].values.reshape(-1, 1)   

  #   X = np.hstack([x, np.ones_like(x)])          

  #   theta = np.linalg.inv(X.T @ X) @ (X.T @ y)   

  #   y_line = X @ theta                           

  #   plt.plot(df1['Date'], y_line, 'r', label='GOOGL Best Fit')

  #   plt.title('Volume Over Time')
  #   plt.xlabel('Date')
  #   plt.ylabel('Volume')
  #   plt.xticks(rotation=45)
  #   plt.legend()
  #   plt.tight_layout()
  #   plt.show()

# if __name__ == "__main__":
  # main()
  
from datetime import datetime
from lumibot.backtesting import YahooDataBacktesting
from lumibot.credentials import broker
from lumibot.credentials import IS_BACKTESTING
from lumibot.strategies import Strategy
from lumibot.traders import Trader


class BuyHold(Strategy):

  def initialize(self):
    self.sleeptime = "10S"

  def on_trading_iteration(self):
    if self.first_iteration:
      symbol = "NVDA"
      price = self.get_last_price(symbol)
      quantity = self.cash // price
      order = self.create_order(symbol, quantity, "buy")
      self.submit_order(order)

if __name__ == "__main__":
  if IS_BACKTESTING:
    start = datetime(2023, 11, 12)
    end = datetime(2024, 11, 11)
    BuyHold.backtest(
        YahooDataBacktesting,
        start,
        end
    )
  else:
    strategy = BuyHold(broker=broker)
    trader = Trader()
    trader.add_strategy(strategy)
    trader.run_all()                


