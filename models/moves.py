class Move:
    def __init__(self, name: str, form: str, typ: str, power: int, points: int, accuracy: int) -> None:
        self._name = name
        self._form = form
        self._typ = typ
        self._power = power
        self._points = points
        self._points_max = points
        self._accuracy = accuracy

    def execute(self) -> bool:
        if not self.can_execute():
            return False

        self._points -= 1
        return True

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, value: int):
        self._points = value

    def can_execute(self) -> bool:
        return self.points > 0

    def details(self) -> str:
        """Returns the details of the move for display"""
        return f"{self._name} : [{self._typ}] {self.disp_form()} {self.points}/{self._points_max} <{self._power}>"

    def disp_form(self) -> str:
        """Returns a one-character string for the display of physical/special form"""
        if self._form == "physical":
            return "*"
        return "o"

    def __str__(self) -> str:
        """Returns the name of the move for display"""
        return self._name

    @classmethod
    def fromJSON(cls, json_obj):
        """Generates a Move object from a json hash"""
        print(f"json_obj : {json_obj}")
        return cls(json_obj["name"], json_obj["form"], json_obj["type"], json_obj["power"], json_obj["points"], json_obj["accuracy"])
