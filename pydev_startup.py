"""
    Google Cloud Engine with Visual Studio Code
"""
import ConfigParser
import os
import sys
import ptvsd

CONFIG = ConfigParser.RawConfigParser()
CONFIG.sections()
CONFIG.read('app.cfg')
APP_IP = CONFIG.get('section', 'ipAddress')

# Assuming that pdvsd is located in the working folder
sys.path.append(os.getcwd())

# Feel free to change the secret and port number
ptvsd.enable_attach(secret='gae', address=(APP_IP, 3000))
