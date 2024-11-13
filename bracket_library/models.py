from .exceptions import *
class Participant:
    def __init__(self, rank: int, name: str ="Bye"):
        if rank < 1:
            raise InvalidRankError("The rank must be at least 1.")
        self.rank = rank
        self.name = name
    
    def __str__(self):
        return f"#{self.rank}: {self.name}"

class Matchup:
    def __init__(self, top: Participant, bottom: Participant):
        self.top = top
        self.bottom = bottom
    
    def __str__(self):
        return f"{self.top}\n{self.bottom}"