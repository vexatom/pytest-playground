from itertools import count


class Task:

    __id = count(start=0)

    @property
    def id(self) -> int:
        return self.__id

    def __init__(self, name: str, description: str, priority: int = 0, status: bool = True) -> None:
        if not isinstance(name, str):
            raise TypeError("Task name must be a string")
        if not name.strip():
            raise ValueError("Task name cannot be empty")
        if len(name) > 50:
            raise ValueError("Task name cannot be longer than 50 characters")
        if not isinstance(description, str):
            raise TypeError("Task description must be a string")
        if len(description) > 400:
            raise ValueError("Task description cannot be longer than 400 characters")
        if type(priority) is not int:
            raise TypeError("Priority must be an integer")
        if priority < 0 or priority > 3:
            raise ValueError("Priority must be between 0 and 3")

        self.name: str = name
        self.description: str = description
        self.priority: int = priority
        self.status: bool = status
        self.__id: int = next(self.__id)

    def change_name(self, name: str) -> bool:
        if not isinstance(name, str):
            raise TypeError("Task name must be a string")
        if not name.strip():
            raise ValueError("Task name cannot be empty")
        if len(name) > 50:
            raise ValueError("Task name cannot be longer than 50 characters")
        self.name = name
        return True

    def change_description(self, description: str) -> bool:
        self.description = description
        return True

    def change_priority(self, priority: int) -> bool:
        self.priority = priority
        return True

    def change_status(self, status: bool) -> bool:
        self.status = status
        return True

