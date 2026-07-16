from itertools import count


class Task:

    __id = count(start=0)

    @property
    def id(self) -> int:
        return self.__id

    @staticmethod
    def _validate_name(name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Task name must be a string")
        if not name.strip():
            raise ValueError("Task name cannot be empty")
        if len(name) > 50:
            raise ValueError("Task name cannot be longer than 50 characters")

    @staticmethod
    def _validate_description(description: str) -> None:
        if not isinstance(description, str):
            raise TypeError("Task description must be a string")
        if len(description) > 400:
            raise ValueError("Task description cannot be longer than 400 characters")

    @staticmethod
    def _validate_priority(priority: int) -> None:
        if type(priority) is not int:
            raise TypeError("Priority must be an integer")
        if priority < 0 or priority > 3:
            raise ValueError("Priority must be between 0 and 3")

    @staticmethod
    def _validate_status(status: bool) -> None:
        if type(status) is not bool:
            raise TypeError("Status must be a boolean")

    def __init__(self, name: str, description: str, priority: int = 0, status: bool = True) -> None:
        self._validate_name(name)
        self._validate_description(description)
        self._validate_priority(priority)
        self._validate_status(status)

        self.name: str = name
        self.description: str = description
        self.priority: int = priority
        self.status: bool = status
        self.__id: int = next(self.__id)

    def set_name(self, name: str) -> bool:
        self._validate_name(name)
        self.name = name
        return True

    def set_description(self, description: str) -> bool:
        self._validate_description(description)
        self.description = description
        return True

    def set_priority(self, priority: int) -> bool:
        self._validate_priority(priority)
        self.priority = priority
        return True

    def change_status(self) -> bool:
        self.status = not self.status
        return self.status

