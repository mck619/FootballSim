import numpy

class GameClock(object):

    '''game clock for football sim'''

    def __init__(self, quarters=4, q_len = 15):

        self.q = 1
        self.quarters = quarters
        self.q_len = q_len*60
        self.q_time = self.q_len
        self.game_over = False
        self.quarter_over = False

    def run_clock(self, secs):

        self.q_time -= secs

        if self.q_time <= 0 :
            self.q_time = 0
            self.quarter_over = True

    def start_quarter(self):

        self.q += 1
        self.q_time = self.q_len
        if self.q == 5:
            self.game_over = True

    def quarter_end(self):

        return self.quarter_over

    def game_end(self):

        return self.game_over

    def time_str(self):
        mins = int(self.q_time/60)
        secs = self.q_time%60
        return "Q"+str(self.q)+" "+str(mins).zfill(2)+":"+str(secs).zfill(2)

    def time_secs(self):
        return (self.q, self.q_time)

class Game(object):

    def __init__(self, away_team, home_team):
        self.away_team = away_team
        self.home_team = home_team
        self.clock = GameClock()
        self.score = (0,0)
        self.winner = None
        self.drives = []
        self.log = Logger()

    def play_game(self, name):

        self.log.start_log(name)

        p = Play()
        k = KickOff()
        d = Drive()

        #coin toss

        if numpy.random.randint(0,1) == 0:
            offense = self.home_team
            defense = self.away_team
        else:
            offense = self.away_team
            defense = self.home_team

        self.log.write_log(offense.get_name() + " has won the coin toss and elected to receive.")
        (offense, defense, yd_line) = k.kick(defense, offense, self.log, self.clock, 35)

        while not self.clock.game_over():

            (result,yd_line) = d.play_drive(offense, defense, yd_line, self.clock, self.log)

            if result == "Turnover":

                offense, defense = defense, offense

            else:

                if result == "Touchdown":

                    if offense is self.home_team:
                        self.score[0] += 7
                    else:
                        self.score[1] += 7

                if result == "Field Goal":

                    if offense is self.home_team:
                        self.score[0] += 3
                    else:
                        self.score[1] += 3

                (offense, defense, yd_line) = kick(offense, defense, self.log, self.clock, 35)





class Team(object):

    def __init__(self, name, race, home_city, stats):
        #self might be a dict of stats?
        self.name = name
        self.race = race
        self.home_city = home_city
        self.record = (0,0)
        self.stats = stats

    def hire_coach(self, coach):

        self.coach = coach



        '''needs stats'''

    def get_name(self):

        return self.name



class Coach(object):

    def __init__(self, name, stats = {'agressiveness':0, 'run_tendancy':0}):

        self.name = name
        self.agressiveness = stats['aggressiveness']    #-5 to 5
        self.run_tendancy = stats['run_tendancy']       #-5 to 5

    def choose_play(dd, yd_line, side, clock, opponent):
        '''

        simple coach AI To choose a play based on field position and dd

        :param dd: down and distance (down(int), distance(int))
        :param yd_line: field position (int)
        :param side: 'o' or 'd'
        :param opponent: opponents team
        :return: 1 of 4 offensive or 4 defensive plays
        '''

        if clock.time_sec[0] == (2 or 4) and clock.time_sec[1] < 120:
            '''2 minute drill play calling'''

        else:
            if dd[0] == 1:
            #default probability on 1st down:  1/3 run, 1/3 short pass, 1/3 long pass

            if dd[0] == 2:
                if dd[1] >= 15:
                # .5 long pass .25 short pass .25 run

                if 15 > dd[1] >= 10:
                # .4 long pass .3 short pass .3 run

                if 10 > dd[1] >= 5:
                # 1/3 long pass 1/3 short pass 1/3 run

                if 5 > dd[1] :
                # 1/3 long pass 1/3 short pass 1/3 run

            if dd[0] == 3:
                if dd[1] >= 15:
                # .7 long pass .15 run .15 short pass

                if 15 > dd[1] >= 10:
                # .6 long pass .2 run .2 short pass

                if 10 > dd[1] >= 5:
                # .15 long pass .75 short pass .1 run

                if 5 > dd[1] >=3 :
                # .15 long pass .65 short pass .2 run

                if 3 > dd[1]:
                # .05 long pass .475 run .475 short pass

            if dd[0] == 4:

                if dd[1] >= 15:

                if 15 > dd[1] >= 10:

                if 10 > dd[1] >= 5:

                if 5 > dd[1] >= 3:

                if 3 > dd[1]:



class Drive(object):

    def play_drive(self, offense, defense, yd_line, clock, log):
        '''simulates the drive'''
        p = Play()
        while p.get_outcome[0] not in  {"Field Goal", "Touchdown", "Turnover", "End Half", "End Game"}:

            (result, yd_line) = p.run_play(offense, defense, yd_line, clock, log)

        return (result, yd_line)


        return (self.result, yd_line)



class KickOff(object):


    def kick(self, logger):

        '''runs a kickoff returns a field position and the team who gained possession(in case of a turnover)'''



class Logger(object):
    def start_log(self):

    def close_log(self):

    def write_log(self,line):

    def read_log(self,name):


class Play(object):

    def run_play(self, offense, defense, dd, yd_line, clock, log):

        o_play = offense.choose_play(yd_line, 'o', dd, clock, defense)
        d_play = defense.choose_play(yd_line, 'd', dd, clock, defense)




