# import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    df1 = pd.read_csv('information_MSFT.csv')
    df2 = pd.read_csv('information_AAPL.csv')
    df3 = pd.read_csv('information_GOOGL.csv')
    
    # Convert "Date" columns to datetime
    df1['Date'] = pd.to_datetime(df1['Date'])
    df2['Date'] = pd.to_datetime(df2['Date'])
    df3['Date'] = pd.to_datetime(df3['Date'])

    plt.figure(figsize=(10,6))
    
    # Plot scatter of each
    plt.scatter(df1['Date'], df1['Volume'], c="red",   linewidth=2, label="MSFT Volume")
    plt.scatter(df2['Date'], df2['Volume'], c="green", linewidth=2, label="AAPL Volume")
    plt.scatter(df3['Date'], df3['Volume'], c="black", linewidth=2, label="GOOGL Volume")

    df_all = pd.concat([
        df1[['Date', 'Volume']],
        df2[['Date', 'Volume']],
        df3[['Date', 'Volume']]
    ], ignore_index=True)

    df_all.sort_values(by='Date', inplace=True)

    df_all['Date_ordinal'] = df_all['Date'].map(pd.Timestamp.toordinal)

    x = df_all['Date_ordinal'].values.reshape(-1, 1)
    y = df_all['Volume'].values.reshape(-1, 1)

    X = np.hstack([x, np.ones_like(x)])

    theta = np.linalg.inv(X.T @ X) @ (X.T @ y)

    y_pred = X @ theta

    plt.plot(df_all['Date'], y_pred, color='purple', linewidth=2,
             label='Combined Best Fit')

    # 10) Label, legend, show
    plt.title('Volume Over Time - Combined Regression')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()