# Subclass inheriting from CricketTeam
class AsiaCupTeam(CricketTeam):
    def __init__(self, team_name, captain):
        super().__init__(team_name, captain)
        self.players = []
    
    # Method to add players to the squad
    def add_player(self, player_name, player_role):
        self.players.append({'name': player_name, 'role': player_role})
    
    # Implementing the abstract method get_squad
    def get_squad(self):
        return self.players
