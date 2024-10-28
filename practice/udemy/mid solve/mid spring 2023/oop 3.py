# Player class to represent individual players
class Player:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    
    def __repr__(self):
        return f'{self.name} ({self.role})'

# AsiaCupTeam class inheriting from CricketTeam
class AsiaCupTeam(CricketTeam):
    def __init__(self, team_name, captain):
        super().__init__(team_name, captain)
        self.players = []
    
    # Method to add players to the squad
    def add_player(self, player_name, player_role):
        player = Player(player_name, player_role)  # Create a Player object
        self.players.append(player)  # Add the Player object to the squad list
    
    # Implementing the abstract method get_squad
    def get_squad(self):
        return self.players

# Main program
if __name__ == "__main__":
    # Creating an instance of AsiaCupTeam for Team Bangladesh
    team_bd = AsiaCupTeam("Bangladesh", "Shakib Al Hasan")
    
    # Adding players to the Bangladesh team
    team_bd.add_player("Litton Kumar Das", "Opening Batsman")
    team_bd.add_player("Mushfiqur Rahim", "Middle Order Batsman")
    team_bd.add_player("Taskin Ahmed", "Right-arm Fast Bowler")
    
    # Printing the squad details
    print(f"Asia Cup 2023 Teams and Players:")
    print(f"Team: {team_bd.team_name}, Captain: {team_bd.captain}")
    print("Squad:")
    for player in team_bd.get_squad():
        print(player)
