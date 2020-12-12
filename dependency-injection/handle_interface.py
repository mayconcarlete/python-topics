from abc import ABCMeta, abstractmethod

class IHandle(metaclass = ABCMeta):
    @abstractmethod
    def handle(self, http_request):
        raise NotImplementedError

class CreateUserController(IHandle):
    def handle(self, http_request):
        print(http_request)

user_controller = CreateUserController()
user_controller.handle({"name":"Maycon"})
        