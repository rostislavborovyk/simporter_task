class EventDao:
    __slots__ = ['date', 'value']

    def __init__(self, date: str, value: int):
        self.date = date
        self.value = value
