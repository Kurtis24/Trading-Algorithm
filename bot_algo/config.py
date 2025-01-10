import os

ALPACA_CONFIG = {
    # Put your own Alpaca key here:
    "API_KEY": os.getenv("ALPACA_API_KEY"),
    # Put your own Alpaca secret here:
    "API_SECRET": os.getenv("ALPACA_API_SECRET"),
    # Set this to False to use a live account
    "PAPER": True
}