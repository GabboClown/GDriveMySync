# This file loads .env file in env variables and authenticates the user if they're not authenticated

from App.ServiceContainer import ServiceContainer
from App.Api.Authenticator import Authenticator
from App.Api.Configurator import Configurator
from App.Api.HelpAccessor import HelpAccessor
from App.Repositories.DriveRepository import DriveRepository
import os
import sys
import json
from dotenv import load_dotenv

# Dependencies used in main file
__all__ = ['load_dotenv', 'os', 'sys', 'json', 'ServiceContainer', 'Authenticator', 'Configurator', 'HelpAccessor', 'DriveRepository']

load_dotenv()

ServiceContainer.register('DriveRepository', DriveRepository)

# BEGIN AUTH PROCESS

# Authenticates by using authenticator class
service = Authenticator.getService()
# Setups DriveRepository service static attribute
driveRepository = ServiceContainer.get('DriveRepository', service) 

# END AUTH PROCESS