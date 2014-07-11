import string

class Game:
    def __init__(self, team_1="", team_2="", winner=""):
        team_1,team_2 = team_1.lower(),team_2.lower()     
        self.team_1 = team_1
        self.team_2 = team_2 
        
        if winner == "": 
            self.winner = ""
            self.loser = ""
        elif winner in ["1","2"]: 
            winner = int(winner)-1
            self.winner = [team_1,team_2][winner]
            self.loser = [team_2,team_1][winner]
        elif winner.lower() == "tbd":
            self.winner = "tbd"

def calculate_scores(player_rankings, game_list, success_score = 5, fail_score = -5):
    '''player_rankings is a list of lists such as ['argentina','brazil'] in order of greatest
         to worst teams
       game_list is a list of game objects; the attributes should be set'''
    player_scores = [0 for game in game_list]
    for game in game_list:
        for i in range(len(player_rankings)):
            ranking = player_rankings[i]
            if game.winner != "" and game.winner != "tbd":
                try:
                    winner_index = ranking.index(game.winner)
                    loser_index = ranking.index(game.loser)
                except ValueError as e:
                    # this is the case where a player did not list one
                    #  of the game's teams in his/her ranking
                    # we can either leave score untouched (A) or
                    #  make an assumption that they only chose the best teams
                    #  and if they left out the loser, give them some points (B)
                    
                    # A - no points
                    #continue
                    
                    # B - make assumption
                    if game.winner in ranking and game.loser not in ranking:
                        player_scores[i] += success_score
                    elif game.loser in ranking and game.winner not in ranking:
                        player_scores[i] += fail_score
                    continue
                    
                if winner_index < loser_index:
                    player_scores[i] += success_score
                else: 
                    player_scores[i] += fail_score
                    
            else: # tie or tbd, no points
                pass
    return player_scores
            
def get_player_info(file_name):
    """Returns a tuple containing: ([player_names], [bracket_names], [rankings])"""
    with open(file_name,"rb") as f:
        f.readline() # throw away the first line
        lines = f.readlines()
        
    player_names = []
    bracket_names = []
    rankings = []
    for line in lines:
        line = line.decode("utf-8",'ignore')
        cols = line.strip().split(",")
        

        player_name, bracket_name, ranking = cols[0], cols[1], cols[2:]
        player_names.append(player_name)
        bracket_names.append(bracket_name)
        
        # strip white-space characters and standardize cote d'ivoir 'o'
        ranking = [name.lower().strip().replace('\xf4','o') for name in ranking]
        rankings.append(ranking)
        
    return (player_names,bracket_names,rankings)
    
def get_games(file_name):
    """returns a list of games"""
    with open(file_name,"rb") as f:
        lines = f.readlines()
        
    games = []
    for line in lines:
        line = line.decode("utf-8",'ignore')
    
        cols = line.strip().split(",")
        

        team_1, team_2, winner = cols[0], cols[1], cols[2]
        game = Game(team_1, team_2, winner)
        games.append(game)
    
    return games
        
        
        
        