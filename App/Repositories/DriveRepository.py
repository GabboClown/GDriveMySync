from App.Exceptions.ServiceNotRegisteredException import ServiceNotRegisteredException

class DriveRepository:
    _service = None

    def __init__(self, service=None):
        if DriveRepository._service is None:
            if service is not None:
                DriveRepository._service = service
            else:
                raise ServiceNotRegisteredException("You need to pass Google Resource service on initialization")
