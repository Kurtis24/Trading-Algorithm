# import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


def main():
    # Define the ticker symbols
    # tickers = ['AAPL', 'MSFT', 'GOOGL', 'BTC-USD']  # Add or remove symbols as needed

    # # Download historical data for the specified tickers
    # data = yf.download(tickers, period='1mo', interval='1d', group_by='ticker')

    # # Initialize an empty dictionary to store individual DataFrames
    # ticker_data = {}

    # for ticker in tickers:
    #     try:
    #         ticker_df = data[ticker].dropna()  # Drop any rows with NaN values
    #         ticker_data[ticker] = ticker_df
    #     except KeyError:
    #         print(f'No data found for {ticker}')

    # # Save each ticker's data to a separate CSV file named "information_[TICKER].csv"
    # for ticker, df in ticker_data.items():
    #     # Clean ticker symbol for filename (replace '-' with '_')
    #     clean_ticker = ticker.replace('-', '_')
    #     filename = f'information_{clean_ticker}.csv'  # e.g., information_AAPL.csv
    #     df.to_csv(filename)
    #     print(f'Data for {ticker} saved to {filename}')


    df1 = pd.read_csv('information_MSFT.csv')
    df2 = pd.read_csv('information_AAPL.csv')
    df3 = pd.read_csv('information_GOOGL.csv')
    df4 = pd.read_csv('information_BTC_USD.csv')

    # Example: If your CSV has columns named 'Date' and 'Value', you can plot 'Value' over 'Date'
    plt.figure(figsize=(10, 5))
    
    plt.plot(df1['Date'], df1['Volume'], marker='o', linestyle='-')
    plt.plot(df2['Date'], df2['Volume'], marker='o', linestyle='-')
    plt.plot(df3['Date'], df3['Volume'], marker='o', linestyle='-')
    plt.plot(df4['Date'], df4['Volume'], marker='o', linestyle='-')
    
    plt.title('Value Over Time')
    plt.xlabel('Date')
    plt.ylabel('Value')

    # Rotate date labels if necessary
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Show the plot
    plt.show()



if __name__ == "__main__":
    main()