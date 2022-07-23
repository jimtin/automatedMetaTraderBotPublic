import MetaTrader5 as mt5


# Get a list of symbols available. Function assumes that Meta Trader 5 is working from the startup functions
def getSymbolList():
    print("Getting Symbol List")
    # Get a list of symbols
    symbols = mt5.symbols_get()
    # Create an array to store all the names
    symbolNames = []
    # Add all symbol names to the list
    for symbol in symbols:
        # Use the append function to add to array
        symbolNames.append(symbol.name)
    return symbolNames
