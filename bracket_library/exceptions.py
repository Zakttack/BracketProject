class InvalidRankError(ValueError):
    def __init__(self, message: str, cause: Exception | None = None):
        self.message = message
        super().__cause__ = cause
    
    def __str__(self):
        return f"{self.message}\nCaused by: {super().__cause__}" if super().__cause__ is not None else self.message