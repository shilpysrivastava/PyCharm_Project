''''This is the config reader file which will read my config file'''''


import configparser
import os

config = configparser.ConfigParser()
config_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "config",
    "config.ini"
)
config.read(config_path)

def get_config(section, key):
    return config.get(section, key)


