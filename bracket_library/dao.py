from .exceptions import *
from .models import *

class Bracket:
    def __init__(self, participants: list[Participant]):
        if len(participants) == 0:
            self.participants = [Participant(1), Participant(2)]
        elif len(participants) == 1 and participants[0].rank != 1:
            raise InvalidRankError("This participant must be ranked number 1.")
        elif len(participants) >= 2:
            participants_check = sorted(participants, key=lambda x: x.rank)
            current_valid_rank = 1
            for participant in participants_check:
                if participant.rank != current_valid_rank:
                    raise InvalidRankError(f"{participant.name} must be ranked {current_valid_rank} rather than {participant.rank}.")
                current_valid_rank += 1
            self.participants = participants_check
            