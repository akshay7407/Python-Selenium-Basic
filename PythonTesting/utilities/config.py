import configparser
import os


def getConfig():
    config = configparser.ConfigParser()
    # get root directory
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    FilePath = os.path.join(project_root, "utilities/properties.ini")
    config.read(FilePath)
    return config