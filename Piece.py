class Piece:
    def __init__(self, team):
        self.team = team
    
    def getTeam(self):
        """Returns the team of the piece"""
        return self.team
    
    def isSameTeam(self, other):
        """Checks if one piece is on the same team as another"""
        return self.team == other.team

    def move(self):
        pass