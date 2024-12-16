import yfinance as yf
import pandas as pd


def main():
    # Define the ticker symbols
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'BTC-USD']  # Add or remove symbols as needed

    # Download historical data for the specified tickers
    data = yf.download(tickers, period='1mo', interval='1d', group_by='ticker')

    # Initialize an empty dictionary to store individual DataFrames
    ticker_data = {}

    for ticker in tickers:
        try:
            ticker_df = data[ticker].dropna()  # Drop any rows with NaN values
            ticker_data[ticker] = ticker_df
        except KeyError:
            print(f'No data found for {ticker}')

    # Save each ticker's data to a separate CSV file named "information_[TICKER].csv"
    for ticker, df in ticker_data.items():
        # Clean ticker symbol for filename (replace '-' with '_')
        clean_ticker = ticker.replace('-', '_')
        filename = f'information_{clean_ticker}.csv'  # e.g., information_AAPL.csv
        df.to_csv(filename)
        print(f'Data for {ticker} saved to {filename}')



if __name__ == "__main__":
    main()