class Move:
    def __init__(self, name:str, form:str, typ:str, power:int, points:int, accuracy:int) -> None:
        self._name = name
        self._form = form
        self._typ = typ
        self._power = power
        self._points = points
        self._accuracy = accuracy

    def execute(self) -> bool:
        if not self.can_execute():
            return False

        self._points -= 1
        return True

    def can_execute(self) -> bool:
        return self._points > 0

    def __str__(self) -> str:
        return self._name

    @classmethod
    def fromJSON(cls, json_obj):
        return cls(json_obj["name"], json_obj["form"], json_obj["type"], json_obj["power"], json_obj["points"], json_obj["accuracy"])

