from dependency_injection.handle_interface import IHandle

class CreateUserExample(IHandle):
    def handle(self, http_request):
        print(http_request)
