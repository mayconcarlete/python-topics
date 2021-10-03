from typing import Type
from typing import Union


class CheckFieldInstance:
    def __init__(self, type: Type) -> None:
        self.type = type

    def validate(self, field) -> bool:
        if isinstance(field, self.type):
            return True
        return False
