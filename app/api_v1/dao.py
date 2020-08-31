class EventDao:
    __slots__ = ['date', 'value']  # for faster creation of objects

    def __init__(self, date: str, value: int):
        self.date = date
        self.value = value
