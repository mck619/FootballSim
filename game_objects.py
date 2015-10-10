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

    def time(self):
        mins = int(self.q_time/60)
        secs = self.q_time%60
        return "Q"+str(self.q)+" "+str(mins).zfill(2)+":"+str(secs).zfill(2)

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

    def run_play(self, offense, defense, dd, yd_line, log):

        o_play = offense.choose_play(yd_line, 'o', dd)
        d_play = defense.choose_play(yd_line, 'd', dd)




