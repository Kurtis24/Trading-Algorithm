from datetime import datetime
from lumibot.backtesting import YahooDataBacktesting
from lumibot.credentials import broker
from lumibot.credentials import IS_BACKTESTING
from lumibot.strategies import Strategy
from lumibot.traders import Trader
from alpaca.trading.client import TradingClient

import yfinance as yf
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import os

    
class BuyHold(Strategy):
  def initialize(self):
    self.sleeptime = "1S"

  def on_trading_iteration(self):
    if self.first_iteration:
      symbol = "NVDA"
      price = self.get_last_price(symbol)
      
      #if market is good or bad
      fake_quant = (self.cash // price) / 2
      
      
      data = yf.download(symbol, start="2024-5-01", end="2024-5-31")

      data.reset_index(inplace=True)

      data['Date'] = data['Date'].apply(lambda x: x.toordinal())
      dat = data['Date']
      vol = data['Volume']

      
      coefficients = np.polyfit(dat, vol, 1) 
      slope, intercept = coefficients

      y_pred = slope * dat + intercept
      
      if slope > 0:
        quantity = fake_quant * slope
        order = self.create_order(symbol, quantity, "buy")
        self.submit_order(order)
      else:
        print("Not good to buy")

if __name__ == "__main__":
  
  if IS_BACKTESTING:
    start = datetime(2024, 5, 1)
    end = datetime(2024, 5, 31)
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