# InteractiveBrokers-LiveMarketDataFetcher

This repository contains a Python script for fetching and displaying live market data for selected stock tickers using the Interactive Brokers API. The script utilizes the `ib_insync` library to establish a connection with the Interactive Brokers Trader Workstation (TWS) or IB Gateway, request market data, and handle the received data in real-time.

## Features:
- **Live Market Data**: Fetch and display bid, ask, and last traded prices in real-time for specified stock tickers.
- **Average Price Estimation**: In cases where the last traded price is not available, the script calculates an average price based on the bid and ask prices.
- **Time-Stamped Data**: Each data point is time-stamped with millisecond precision, ensuring accurate tracking of market movements.
- **Handle None Values**: The script includes checks to handle None values in bid, ask, and last traded prices, preventing potential errors during runtime.
- **Customizable Ticker List**: Users can easily modify the list of stock tickers to fetch data for, making the script versatile for different use cases.
- **Continuous Data Fetching**: The script runs in an infinite loop, continuously fetching and displaying market data until manually stopped.
- **Safe API Interaction**: Includes a sleep function to prevent overloading the Interactive Brokers API with requests, ensuring compliance with rate limits.

## Getting Started:
1. **Install Required Libraries**: Ensure that the `ib_insync` and `datetime` libraries are installed in your Python environment.
2. **Set Up Interactive Brokers Connection**: Ensure that the Interactive Brokers Trader Workstation (TWS) or IB Gateway is running and properly configured to accept API connections.
3. **Configure API Connection**: Modify the connection parameters in the `main` function if necessary to match your TWS or IB Gateway setup.
4. **Customize Stock Tickers**: Update the `tickers` list in the `main` function with the stock tickers you wish to fetch data for.
5. **Run the Script**: Execute the script. It will start fetching and displaying live market data for the specified stock tickers.

## Requirements:
- Python 3.x
- Interactive Brokers account
- Trader Workstation (TWS) or IB Gateway installed and configured
- `ib_insync` library
- `datetime` library

## Note:
The script is set to request delayed market data by default. You can change the market data type in the `reqMarketDataType` function call according to your Interactive Brokers account and data subscription.

---

Feel free to clone, fork, and contribute to this repository to make it even better! If you encounter any issues or have suggestions for improvements, please open an issue in the repository.

**Disclaimer**: I am not responsible for any investments, trades or losses. Any first time connection should use a paper account. Use this code at your own risk!
