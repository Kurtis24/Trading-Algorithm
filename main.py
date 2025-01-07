# import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
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

    plt.figure(figsize=(10,5))
    
    # Plot scatter of each
    plt.scatter(df1['Date'], df1['Volume'], c="red",   linewidth=2, label="MSFT Volume")
    plt.scatter(df2['Date'], df2['Volume'], c="green", linewidth=2, label="AAPL Volume")
    plt.scatter(df3['Date'], df3['Volume'], c="black", linewidth=2, label="GOOGL Volume")

    # Example best fit line for df1 only:
    # 1) Convert date to an ordinal so it's numeric
    df1['Date_ordinal'] = df1['Date'].map(pd.Timestamp.toordinal)
    
    # 2) Prepare X and y
    x = df1['Date_ordinal'].values.reshape(-1, 1)  # shape (N,1)
    y = df1['Volume'].values.reshape(-1, 1)        # shape (N,1)

    # 3) Build matrix X (with intercept)
    X = np.hstack([x, np.ones_like(x)])            # shape (N,2)

    # 4) Solve for theta = (X^T X)^{-1} X^T y
    theta = np.linalg.inv(X.T @ X) @ (X.T @ y)     # shape (2,1)

    # 5) Predict
    y_line = X @ theta                             # shape (N,1)

    # Plot the best fit line against the original Date
    plt.plot(df1['Date'], y_line, 'r', label='MSFT Best Fit')

    plt.title('Volume Over Time')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()