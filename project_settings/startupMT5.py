import MetaTrader5 as mt5


# Function to start Meta Trader 5, then test it's working
def startMT5(settings_info):
    # Extract the information we need from the settings info
    # MT5 requires the username to be an int, not a string. Ensure this is the case.
    username = int(settings_info['username'])
    password = settings_info['password']
    server = settings_info['server']
    path = settings_info['mt5Pathway']

    # Test Initialisation
    if not mt5.initialize(login=username, password=password, server=server, path=path):
        # If it doesn't work, print to the screen
        print(f"MT5 failed to initialise. Error: {mt5.last_error()}")
        # Quit the application
        quit()
        return False
    else:
        # If it does work, login
        print("Successfully Initialised")
        login = mt5.login(login=username, password=password, server=server)
        if login:
            print("Logged In Successfully")
            return True
        else:
            print(f"Login Fail {mt5.last_error()}")
            return False
