import configparser

from CONSTANTS import ROOT_DIR

abs_path = f'{ROOT_DIR}/config/configuration.ini'
config = configparser.RawConfigParser()
config.read(abs_path)


class ReadConfig:
    @staticmethod
    def get_bas_url():
        return config.get('app_info', 'base_url')

    @staticmethod
    def get_user_name():
        return config.get('user_data', 'user_name')

    @staticmethod
    def get_user_password():
        return config.get('user_data', 'password')

    @staticmethod
    def get_browser_data():
        return config.get('browser_data', 'browser_id')
