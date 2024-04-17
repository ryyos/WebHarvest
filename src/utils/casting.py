class Casting:

    @staticmethod
    def to_float(text: str) -> float | str:
        try:
            return float(text)
        except Exception:
            return text
        

    @staticmethod
    def to_int(text: str) -> float | str:
        try:
            return int(text)
        except Exception:
            return text