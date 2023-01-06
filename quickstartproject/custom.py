from azure.appconfiguration.provider import AzureAppConfigurationProvider

CONFIG_CONNECTION_STRING = "your-connection-string"
config = AzureAppConfigurationProvider.load(CONFIG_CONNECTION_STRING)

# Overrides default language setting in 'settings.py' file
try:
    LANGUAGE_CODE = config["language"]
    print("Custom language mode configured.")

except KeyError:
    print("Default language will be used")


USER_NAME = config["name"]
