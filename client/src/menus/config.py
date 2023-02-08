import configparser

# Config class to read and write config files
class Config:

    # Constructor
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config_file = "..\conf.cfg"
        self.read_config()
            
    # Read the config file
    def read_config(self):
        self.config.read(self.config_file)
        
    # Get a value from the config file
    def get_value(self, section, key):
        return self.config.get(section, key)
    
    # Set a value in the config file
    def set_value(self, section, key, value):
        self.config.set(section, key, value)
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)