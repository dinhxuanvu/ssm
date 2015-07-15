import os

# Support both COnfigParser (Python2) & configparser (Python3)
try:
    import ConfigParser
except ImportError:
    import configparser as ConfigParser

# Dict to hold parsed configuration data
config_data = {}

try:
    SSM_CONFIG_PATH = os.environ['SSM_CONFIG_PATH']
except KeyError:
    SSM_CONFIG_PATH = "/etc/ssm.conf"


def get_variable(section, option, environ_variable, default):
    '''
    Retrieve the variable based on section and option from either
    environment variable or configuration file or default value.
    '''

    try:
        return os.environ[environ_variable]
    except KeyError:
        try:
            return get_config()[section][option]
        except KeyError:
            return default


def get_config():
    '''
    Read the configuration file (ssm.conf) to set SSM options
    Save all configuration in global dictionary and reuse
    '''

    global config_data

    if config_data:
        return config_data
    else:
        # Configuration parser
        parser = ConfigParser.SafeConfigParser()
        # Read configuration file
        try:
            config = parser.read(SSM_CONFIG_PATH)
        except ConfigParser.ParsingError:
            return config_data

        if config:
            # Get all available sections in config file
            sections = parser.sections()
            # Parse configuration file section by section
            for section in sections:
                config_data[section] = {}
                options = parser.options(section)
                for option in options:
                    config_data[section][option] = parser.get(section, option)
            return config_data
        else:
            # Can't read/find config file, return empty dict
            return config_data
