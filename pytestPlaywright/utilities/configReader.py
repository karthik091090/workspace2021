from configparser import ConfigParser
import os

# config=ConfigParser()
# config.read("./config.ini")
# print(config.get("locator","firstnameInput"))

def readConfig(section, key):
    config=ConfigParser()
    
    base_dir=os.path.dirname(os.path.abspath(__file__))
    print(base_dir)
    config_path=os.path.join(base_dir,"..","ConfigurationData","conf.ini")
    print(config_path)

    ######config.read("./config.ini")
    config.read(config_path)
    print(config.get(section,key))
    return config.get(section,key)

def readLocators(locatorPage, key):
    config=ConfigParser()
    
    base_dir=os.path.dirname(os.path.abspath(__file__))
    print(base_dir)
    config_path=os.path.join(base_dir,"..","ConfigurationData",locatorPage)
    print(config_path)

    ######config.read("./config.ini")
    config.read(config_path)
    print(config.get("locators",key))
    return config.get("locators",key)
    
    
# readConfig("locator","firstnameInput")