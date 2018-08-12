import requests
from base64 import b64encode
import json
from datetime import date, timedelta


season_dates = {"2016-2017" : {"regular_season" : {"from" : 20161025,"to" : 20170412},
                               "playoffs" : {"from" : 20170415,"to" : 20170525},
                               "final" : {"from" : 20170601,"to" : 20170612}},
                "2017-2018" : {"regular_season" : {"from" : 20171017,"to" : 20180411},
                               "playoffs" : {"from" : 201780414,"to" : 20180528},
                               "final" : {"from" : 20170531,"to" : 20170608}}}

def request_data(address, login):
    '''
    Wrapper function to send a request to server
    
    :param: address: address for request
    :login login: login for the request 
    '''
    userAndPass = b64encode(login).decode("ascii")
    print('Requesting ... {}'.format(address))
    r = requests.get(address,
                     headers = { 'Authorization' : 'Basic %s' %  userAndPass })
    
    str_content = r.content.decode("utf-8") 
    
    obj = json.loads(str_content)
    return obj



def get_seasonal_games(login, year_from=2017, year_to = 2018, 
              season='regular',to_file=False):
    '''
    Wrapper function to get season games
    
    :param login: login for the request
    :param year_from: beginning of season
    :param yeat_to: end of season
    :param season: regular or playoff
    :to_file: to save json to disk
    :return: python dictionary containing requested data    
    '''
    
    address = 'https://api.mysportsfeeds.com/v2.0/pull/nba/{}-{}/games.json'.format(year_from, year_to, season)
    data = request_data(address, login)
    
    if to_file and len(data)>0:
        file_name = 'data/seasonal/games_{}-{}-{}.json'.format(year_from, year_to, season)
        print("Saving data to ... {}".format(file_name))
        with open(file_name, 'w') as outfile:
            json.dump(data, outfile)
    return data


def get_daily_games(login, date, 
              season='regular',to_file=False):
    '''
    Wrapper function to get games for a given day
    
    :param login: login for the request
    :param date: data in YYYYMMDD format
    :param season: regular or playoff
    :to_file: to save json to disk
    :return: python dictionary containing requested data    
    '''
    
    year_to = int(date[0:4])
    year_from = year_to-1
    address = 'https://api.mysportsfeeds.com/v2.0/pull/nba/{}-{}-{}/date/{}/games.json'.format(year_from,
                                                                                               year_to,
                                                                                               season,
                                                                                               date)
    data = request_data(address, login)
    
    if to_file and len(data)>0:
        file_name = 'data/daily/games_{}-{}.json'.format(date, season)
        print("Saving data to ... {}".format(file_name))
        with open(file_name, 'w') as outfile:
            json.dump(data, outfile)
            
    return data


def get_seasonal_player_logs(login, 
                             year_from=2017, 
                             year_to=2018, 
                             season='regular',
                             to_file=False):
    '''
    Wrapper function to get games for a given day
    
    :param login: login for the request
    :param date: data in YYYYMMDD format
    :param season: regular or playoff
    :to_file: to save json to disk
    :return: python dictionary containing requested data    
    '''
    
    address = 'https://api.mysportsfeeds.com/v2.0/pull/nba/{}-{}-{}/player_gamelogs.json'.format(year_from,
                                                                                               year_to,
                                                                                               season)
    data = request_data(address, login)
    
    if to_file and len(data)>0:
        file_name = 'data/seasonal/player_logs_{}-{}-{}.json'.format(year_from, year_to, season)
        print("Saving data to ... {}".format(file_name))
        with open(file_name, 'w') as outfile:
            json.dump(data, outfile)
            
    return data



def get_daily_player_logs(login,
                          date, 
                          year_from,
                          year_to,
                          season='regular',
                          to_file=False):
    
    ### STILL IN DEVELOPMENT
    '''
    Wrapper function to get games for a given day
    
    :param login: login for the request
    :param date: data in YYYYMMDD format
    :param season: regular or playoff
    :to_file: to save json to disk
    :return: python dictionary containing requested data    
    '''

    datetime_object = datetime.strptime(date, '%Y%m%d')
    week_no = datetime_object.isocalendar()[1]
    week_no=1
    address='https://api.mysportsfeeds.com/v2.0/pull/nba/{}-{}-{}/date/{}/week/{}/player_gamelogs.json'.format(year_from,
                                                                                                               year_to,
                                                                                                               season,
                                                                                                               date,
                                                                                                               week_no)
    data = request_data(address, login)
    
    if to_file and len(data)>0:
        file_name = 'data/daily/player_logs_{}-{}.json'.format(season, date)
        print("Saving data to ... {}".format(file_name))
        with open(file_name, 'w') as outfile:
            json.dump(data, outfile)
            
    return data



def get_daily_player_stats(login, 
                           date,
                           year_from=2017, 
                           year_to=2018,
                           season='regular',
                           to_file=False):
    '''
    Wrapper function to get player stats for a given day
    
    :param login: login for the request
    :param date: data in YYYYMMDD format
    :param season: regular or playoff
    :to_file: to save json to disk
    :return: python dictionary containing requested data    
    '''

    address = 'https://api.mysportsfeeds.com/v2.0/pull/nba/{}-{}-{}/player_stats_totals.json?date={}'.format(year_from,
                                                                                                             year_to,
                                                                                                             season,                                                                                                             date)
    data = request_data(address, login)
    
    if to_file and len(data)>0:
        file_name = 'data/daily/player_stats_{}-{}.json'.format(season, date)
        print("Saving data to ... {}".format(file_name))
        with open(file_name, 'w') as outfile:
            json.dump(data, outfile)
            
    return data


def get_game_play_by_play(login, 
                          game_id,
                          year_from, 
                          year_to,
                          season='regular',
                          to_file=False):
    '''
    Wrapper function to get play by play of a game
    
    :param login: login for the request
    :param game_id: data in YYYYMMDD format
    :param season: regular or playoff
    :to_file: to save json to disk
    :return: python dictionary containing requested data    
    '''

    address = 'https://api.mysportsfeeds.com/v2.0/pull/nba/{}-{}-{}/games/{}/playbyplay.json'.format(year_from,
                                                                                                      year_to,
                                                                                                      season,
                                                                                                      game_id)
    data = request_data(address, login)
    
    away_team = data["game"]["awayTeam"]["abbreviation"]
    home_team = data["game"]["homeTeam"]["abbreviation"]
    game_date = datetime.strptime(data["game"]["startTime"][0:10], '%Y-%m-%d').strftime('%Y%m%d')
    
    if to_file and len(data)>0:
        file_name = 'data/game/game_play_by_play_{}-{}-{}-{}.json'.format(game_date, away_team, home_team, game_id)
        print("Saving data to ... {}".format(file_name))
        with open(file_name, 'w') as outfile:
            json.dump(data, outfile)
            
    return data