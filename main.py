# Initial Main File Setup
import project_settings.importSettings as startup
import project_settings.startupMT5 as startMT5


# Project Variables
settingsPath = r"C:\Users\james\PycharmProjects\automatedMetaTraderBotPublic\settings.json"


def print_welcome():
    # Welcome to your Automated Backtester for Meta Trader 5! You're well on your way!
    print(f'Welcome to Automated Trading Backtester for Meta Trader 5!')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_welcome()
    projectDetails = settings_info = startup.getProjectSettings(settingsPath)
    startMT5.startMT5(projectDetails)
