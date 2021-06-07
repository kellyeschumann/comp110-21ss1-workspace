"""A class to model a basketball game."""

__author__ = "730314660"


# TODO 1: Define the BBallGame class, and its logic, here.
class BBallGame:
    """Represents a basketball game."""
    biscuts: bool
    points: int = 0
    winning_team: str
    losing_team: str


    def __init__(self, points: int, winning_team: str, losing_team: str):
        """Constructor."""
        self.points = points
        self.winning_team = winning_team
        self.losing_team = losing_team
        self.biscuits = False

    
    def check_points(self) -> None:
        """Check if there are at least 100 points."""
        if self.points >= 100:
            self.biscuits = True
        else:
            self.biscuits = False
        return None


    def winner(self) -> str:
        """Check who is the winner."""
        if self.winning_team == "UNC" and self.losing_team == "Dook":
            return "GTHD!!"
        if self.winning_team == "UNC":
            return "woohoo"
        return "daggum"

    
    def reset_points(self) -> int:
        """Returns current number of points and resets them to 0."""
        result: int = self.points
        self.points = 0 
        return result