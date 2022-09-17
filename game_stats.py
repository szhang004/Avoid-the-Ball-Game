class GameStats():

    def __init__(self, bg_settings):

        self.bg_settings = bg_settings
        self.reset_stats()

    def reset_stats(self):
        self.level = 1
        self.score = 0