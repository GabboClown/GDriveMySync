from App.ServiceContainer import ServiceContainer
from App.Api.Authenticator import Authenticator
from App.Repositories.DriveRepository import DriveRepository
import os
from dotenv import load_dotenv

# Dependencies used in main file
__all__ = ['load_dotenv', 'os', 'ServiceContainer', 'Authenticator', 'DriveRepository']

load_dotenv()

ServiceContainer.register("DriveRepository", DriveRepository)