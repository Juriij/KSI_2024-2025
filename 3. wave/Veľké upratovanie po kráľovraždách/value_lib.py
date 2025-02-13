class Value:
    def __init__(self, value: str):
        self._value = value
        self._is_disposed = False
    
    def free(self) -> None:
        assert not self._is_disposed
        self._is_disposed = True
        
    def get_value(self) -> str:
        assert not self._is_disposed
        return self._value


class ValueFactory:
    def __init__(self):
        self._values = []

    def make_value(self, value: str) -> Value:
        self._values.append(Value(value))
        return self._values[-1]