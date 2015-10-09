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

