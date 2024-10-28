from abc import ABC, abstractmethod

# Abstract Base Class
class CricketTeam(ABC):
    def __init__(self, team_name, captain):
        self.team_name = team_name
        self.captain = captain
    
    # Abstract method
    @abstractmethod
    def get_squad(self):
        pass
