# Import necessary libraries
from ib_insync import IB, Stock  # IB API helper libraries
import datetime  # To work with date and time

# Function to fetch market data for a given stock ticker
def fetch_data_for_ticker(ib, ticker):
    # Define the contract for the stock with the given ticker
    contract = Stock(ticker, 'SMART', 'USD')  # Stock contract: ticker, exchange, currency
    print(f"Fetching data for {ticker}...")

    # Infinite loop to keep fetching data
    while True:
        # Request market data
        mkt_data = ib.reqMktData(contract, '', False, False)  # Request market data
        ib.sleep(0.5)  # Sleep for 0.5 seconds to avoid overloading the API with requests

        # Extract and round bid and ask prices, handle None values
        bid = round(mkt_data.bid, 7) if mkt_data.bid is not None else None  # Bid price rounded to 7 decimal places
        ask = round(mkt_data.ask, 7) if mkt_data.ask is not None else None  # Ask price rounded to 7 decimal places
        last_price = round(mkt_data.last, 7) if mkt_data.last is not None else None  # Last traded price rounded to 7 decimal places

        # Calculate the average price as an estimate if last traded price is not available
        # The number 2 in the division is used to calculate the average of bid and ask.
        price = round((bid + ask) / 2, 7) if last_price is None else last_price  

        # Get the current time with millisecond precision
        # The -3 in the slicing is used to trim the last 3 characters (microseconds) off the datetime string, 
        # leaving the precision at milliseconds.
        current_time = datetime.datetime.now().strftime('%Y%m%d %H:%M:%S.%f')[:-3]

        # Compile the data into a list
        data = [current_time, price, bid, ask]

        # Print the data to the console
        print(data)

# Main function to set up the connection and start fetching data
def main():
    # Define the list of stock tickers to fetch data for
    tickers = ["F"]  # Example ticker: Ford Motor Company

    # Create an instance of the IB class for interacting with the IB API
    ib = IB()

    # Connect to the Interactive Brokers Trader Workstation (TWS) or IB Gateway
    ib.connect('127.0.0.1', 7684, clientId=1)  # IP address, Port number, Unique client identifier for the API connection

    # Request delayed market data (3)
    # The number 3 here is used to request delayed market data.
    ib.reqMarketDataType(3)  # 1 = Live, 2 = Frozen, 3 = Delayed, 4 = Delayed frozen

    # Fetch market data for each ticker
    for ticker in tickers:
        fetch_data_for_ticker(ib, ticker)

    # Disconnect from the IB API when done
    ib.disconnect()

# Check if the script is run directly and not imported as a module
if __name__ == "__main__":
    main()  # Run the main function
