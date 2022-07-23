import data_gathering.getSymbolList as getSymbols
import MetaTrader5 as mt5


# Director function to manage data query
def querySymbolData(queryParameters):
    # Define the data
    symbols = queryParameters['symbols']
    candleTimeframesRaw = queryParameters['candleTimeframes']
    rowQtys = queryParameters['rowQtys']

    # Convert the candleTimeframes into MT5 compatible format
    candleTimeframes = convertTimeframeIntoMT5Format(candleTimeframesRaw)

    # For each symbol:
    for symbol in symbols:
        # Check if Symbol exists
        symbolCheck = checkSymbol(symbol)
        # If Symbol exists, enable
        if symbolCheck:
            symbolEnable = enableSymbol(symbol)
            if symbolEnable:
                # Query symbol for each candleTimeframeType
                for candleTime in candleTimeframes:
                    # Query symbol for each row type
                    for numRows in rowQtys:
                        rates = queryHistoricData(symbol, candleTime, numRows)
                        print(rates)

            else:
                # Todo: handle the error
                return False
        else:
            # Todo: handle the error
            return False


# Check if symbol is in symbol list
def checkSymbol(symbol):
    # Get the full list of symbols
    symbolList = getSymbols.getSymbolList()
    # Test to see if the symbol we're using is in the list
    if symbol in symbolList:
        # If it exists, return True
        return True
    else:
        # If it does not exist, return False
        return False


# Enable the Symbol
def enableSymbol(symbol):
    # Attempt to enable symbol
    enabled = mt5.symbol_select(symbol, True)
    if enabled:
        print(f"Symbol {symbol}: Enabled")
        return True
    else:
        print(f"Error. {symbol} not enabled")
        return False


# Query the historic symbol details
def queryHistoricData(symbol, candlestickTimeframe, numRows):
    # Make sure the number of rows is an integer
    numRows = int(numRows)
    # Query MT5
    rates = mt5.copy_rates_from_pos(symbol, candlestickTimeframe, 0, numRows)
    return rates


# Convert the string in candleTimeframeType
def convertTimeframeIntoMT5Format(timeframeTypeRaw):
    # Create an array to store the timeframes
    candleTimeframes = []
    for timeframe in timeframeTypeRaw:
        if timeframe == "M1":
            candleTimeframes.append(mt5.TIMEFRAME_M1)
        elif timeframe == "M2":
            candleTimeframes.append(mt5.TIMEFRAME_M2)
        elif timeframe == "M3":
            candleTimeframes.append(mt5.TIMEFRAME_M3)
        elif timeframe == "M4":
            candleTimeframes.append(mt5.TIMEFRAME_M4)
        elif timeframe == "M5":
            candleTimeframes.append(mt5.TIMEFRAME_M5)
        elif timeframe == "M6":
            candleTimeframes.append(mt5.TIMEFRAME_M6)
        elif timeframe == "M10":
            candleTimeframes.append(mt5.TIMEFRAME_M10)
        elif timeframe == "M12":
            candleTimeframes.append(mt5.TIMEFRAME_M12)
        elif timeframe == "M15":
            candleTimeframes.append(mt5.TIMEFRAME_M15)
        elif timeframe == "M20":
            candleTimeframes.append(mt5.TIMEFRAME_M20)
        elif timeframe == "M30":
            candleTimeframes.append(mt5.TIMEFRAME_M30)
        elif timeframe == "H1":
            candleTimeframes.append(mt5.TIMEFRAME_H1)
        elif timeframe == "H2":
            candleTimeframes.append(mt5.TIMEFRAME_H2)
        elif timeframe == "H3":
            candleTimeframes.append(mt5.TIMEFRAME_H3)
        elif timeframe == "H4":
            candleTimeframes.append(mt5.TIMEFRAME_H4)
        elif timeframe == "H6":
            candleTimeframes.append(mt5.TIMEFRAME_H6)
        elif timeframe == "H8":
            candleTimeframes.append(mt5.TIMEFRAME_H8)
        elif timeframe == "H12":
            candleTimeframes.append(mt5.TIMEFRAME_H12)
        elif timeframe == "D1":
            candleTimeframes.append(mt5.TIMEFRAME_D1)
        elif timeframe == "all":
            candleTimeframes = [
                mt5.TIMEFRAME_M1,
                mt5.TIMEFRAME_M2,
                mt5.TIMEFRAME_M3,
                mt5.TIMEFRAME_M4,
                mt5.TIMEFRAME_M5,
                mt5.TIMEFRAME_M6,
                mt5.TIMEFRAME_M10,
                mt5.TIMEFRAME_M12,
                mt5.TIMEFRAME_M15,
                mt5.TIMEFRAME_M20,
                mt5.TIMEFRAME_M30,
                mt5.TIMEFRAME_H1,
                mt5.TIMEFRAME_H2,
                mt5.TIMEFRAME_H3,
                mt5.TIMEFRAME_H4,
                mt5.TIMEFRAME_H6,
                mt5.TIMEFRAME_H8,
                mt5.TIMEFRAME_H12,
                mt5.TIMEFRAME_D1
            ]
        else:
            candleTimeframes.append(mt5.TIMEFRAME_H1)
    return candleTimeframes


def queryAllForexData():
    print("Query All FOREX Data Activated")