import tournament_utils as util

SUCCESS_SCORE = 5
FAILURE_SCORE = -5
RANKINGS_FILE_NAME = "World Cup Rankings.csv"
GAME_RESULTS_FILE_NAME = "World Cup Scores.csv"


if __name__ == "__main__":
    game_list = util.get_games(GAME_RESULTS_FILE_NAME)
    player_names, bracket_names, player_rankings = util.get_player_info(RANKINGS_FILE_NAME)
    final_scores = util.calculate_scores(player_rankings, game_list, SUCCESS_SCORE, FAILURE_SCORE)

    print("%20s  %s" %("name","score"))
    for i in range(len(player_rankings)):
        print("%20s: %d" %(player_names[i],final_scores[i]))
        