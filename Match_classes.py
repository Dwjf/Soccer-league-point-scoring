class Team:
    """This class defines the teams to score
    with variables: 
        Name : str 
        Points: int
    """
    def __init__(self,name=None,points=0):
        self.name = name
        self.points = points


class Match:
    """
    This class defines the match to score with variables
        Name Team A:object
        Name Team B: object
        Result: Tuple
        Penalty: Boolean
    """
    def __init__ (self,teamA=None, teamB=None,result=(), penalty=None):
        self.teamA = teamA
        self.teamB = teamB
        self.result = result
        self.penalty = penalty

    def pointCalc(self,teamA, teamB,result, penalty):
        """
        Funtion to return tuple of points assigned to Team A and 
        Team B, based on result of match. Results should be a tuple

        """
       
        scoreA,scoreB = result
        if scoreA>scoreB:
            if penalty == False:
                teamA.points =teamA.points+3
            else:
                teamA.points=teamA.points +2
        elif scoreB>scoreA:
            if penalty == False:
                teamB.points =teamB.points+3
            else:
                teamB.points=teamB.points +2
        elif scoreA == scoreB:
            teamA.points =teamA.points+1
            teamB.points = teamB.points + 1




