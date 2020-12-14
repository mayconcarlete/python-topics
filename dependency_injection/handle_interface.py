from abc import ABCMeta, abstractmethod

class IHandle(metaclass = ABCMeta):
    @abstractmethod
    def handle(self, http_request):
        raise NotImplementedError
        