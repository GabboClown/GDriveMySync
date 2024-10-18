from App.Exceptions.ServiceNotRegisteredException import ServiceNotRegisteredException

class ServiceContainer:
    _services = {}
    _singletons = {}

    @staticmethod
    def register(name, cls):
        ServiceContainer._services[name] = cls

    @staticmethod
    def get(name, *classargs):
        if name not in ServiceContainer._services:
            raise ServiceNotRegisteredException(f"Service '{name}' not registered.")

        # If the singleton instance doesn't exists, it's created
        if name not in ServiceContainer._singletons:
            # Creates instance and saves it
            ServiceContainer._singletons[name] = ServiceContainer._services[name](*classargs)

        return ServiceContainer._singletons[name]