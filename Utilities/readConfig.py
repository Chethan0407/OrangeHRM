import configparser



config= configparser.RawConfigParser()
config.read("/Users/chethangopal/Desktop/OrangeHRM/Configurations/config.ini")





class ReadConfig():
    @staticmethod
    def getURL():
        url = config.get('Basic info', "base_URL")
        return url


    @staticmethod
    def get_username():
        username = config.get('Basic info', "username")
        return username

    @staticmethod
    def get_password():
        password = config.get('Basic info', "password")
        return password
