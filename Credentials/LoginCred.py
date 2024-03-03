

from Utilities.readConfig import ReadConfig
class CredentialsLogin(ReadConfig):
    base_URL = ReadConfig.getURL()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()


