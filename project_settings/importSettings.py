import json
import os


# Function to import our settings
def getProjectSettings(importFilepath):
    # Test the filepath to make sure it's valid
    if os.path.exists(importFilepath):
        # Open the file
        f = open(importFilepath, "r")
        details = json.load(f)
        f.close()
        return details
    else:
        return "NoDetails"

