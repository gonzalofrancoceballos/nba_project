import pandas as pd
from datetime import datetime

def get_season_games_table_from_json(season_games):
    '''
    Converts season game results from original json format into 
    tabular format

    :param season_games: (dict) python dictionary containing game results for a season
    :return: (pd.DataFrame) table containing game results. One game per row
	'''


    games_pd = pd.DataFrame()

    for i in range(len(season_games["games"])):
        field_game_id = season_games["games"][i]["schedule"]["id"]
        field_away_team = season_games["games"][i]["schedule"]["awayTeam"]["abbreviation"]
        field_away_team_id = season_games["games"][i]["schedule"]["awayTeam"]["id"]
        field_home_team = season_games["games"][i]["schedule"]["homeTeam"]["abbreviation"]
        field_home_team_id = season_games["games"][i]["schedule"]["homeTeam"]["id"]
        field_date = datetime.strptime(season_games["games"][i]["schedule"]["startTime"][0:10], '%Y-%m-%d').strftime('%Y%m%d')
        field_venue = season_games["games"][i]["schedule"]["venue"]["id"]
        field_score_total_away = season_games["games"][i]["score"]["awayScoreTotal"]
        field_score_total_home = season_games["games"][i]["score"]["homeScoreTotal"]
        field_score_q1_away = season_games["games"][i]["score"]["quarters"][0]["awayScore"]
        field_score_q1_home = season_games["games"][i]["score"]["quarters"][0]["homeScore"]
        field_score_q2_away = season_games["games"][i]["score"]["quarters"][1]["awayScore"]
        field_score_q2_home = season_games["games"][i]["score"]["quarters"][1]["homeScore"]
        field_score_q3_away = season_games["games"][i]["score"]["quarters"][2]["awayScore"]
        field_score_q3_home = season_games["games"][i]["score"]["quarters"][2]["homeScore"]
        field_score_q4_away = season_games["games"][i]["score"]["quarters"][3]["awayScore"]
        field_score_q4_home = season_games["games"][i]["score"]["quarters"][3]["homeScore"]

        game_dict = {
            'game_id' : [field_game_id],
            'away_team' : [field_away_team],
            'away_team_id' : [field_away_team_id],
            'home_team' : [field_home_team],
            'home_team_id' : [field_home_team_id],
            'date' : [field_date],
            'venue' : [field_venue],
            'score_total_away' : [field_score_total_away],
            'score_total_home' : [field_score_total_home],
            'score_q1_away' : [field_score_q1_away],
            'score_q1_home' : [field_score_q1_home],
            'score_q2_away' : [field_score_q2_away],
            'score_q2_home' : [field_score_q2_home],
            'score_q3_away' : [field_score_q3_away],
            'score_q3_home' : [field_score_q3_home],
            'score_q4_away' : [field_score_q4_away],
            'score_q4_home' : [field_score_q4_home]}

        new_row = pd.DataFrame(game_dict)

        games_pd = games_pd.append(new_row,ignore_index=True)

    return games_pd