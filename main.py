# Initial Main File Setup
import json
import os.path

import project_settings.importSettings as startup
import project_settings.startupMT5 as startMT5
import querySymbolData


# Project Variables
settingsPath = r"C:\Users\james\PycharmProjects\automatedMetaTraderBotPublic\settings.json"


def print_welcome():
    # Welcome to your Automated Backtester for Meta Trader 5! You're well on your way!
    print(f'Welcome to Automated Trading Backtester for Meta Trader 5!')


# Get the query parameters for the function
def getQueryParameters(queryLocation):
    # Test the filepath to make sure it's valid
    if os.path.exists(queryLocation):
        # Open the file
        f = open(queryLocation, "r")
        details = json.load(f)
        f.close()
        return details
    else:
        return False



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Welcome message -> You can make this really cool with ASCII art if you want!
    print_welcome()
    # Get the sensitive details of the project
    projectDetails = settings_info = startup.getProjectSettings(settingsPath)
    # Start MT5
    startMT5.startMT5(projectDetails)
    # Get the query details
    queryDetails = getQueryParameters(projectDetails["parameterQuery"])
    print(queryDetails)
    # Pass the query details to the querySymbolData
    queryOutcomes = querySymbolData.querySymbolData(queryDetails)
