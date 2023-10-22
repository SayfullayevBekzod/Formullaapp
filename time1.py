class TugashVaqti:
    def __init__(self, hour, minut, second, ms) -> None:
        self._hour = hour
        self._minut = minut
        self._second = second
        self._ms = ms

class Time:
    def __init__(self, gp, driver, tugash_vaqti) -> None:
        self._gp = gp
        self._driver = driver
        self._tugash_vaqti = tugash_vaqti

    def __str__(self) -> str:
        vaqt = self._tugash_vaqti
        return f"{vaqt._hour}:{vaqt._minut}:{vaqt._second}.{vaqt._ms}"
        