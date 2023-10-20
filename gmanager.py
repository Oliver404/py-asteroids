class GManager:
    STATE_START = 0
    STATE_PLAYING = 1
    STATE_PAUSE = 2
    STATE_GAME_OVER = -1

    def __init__(self, playing_state = STATE_START, score = 0):
        self.playing_state = playing_state
        self.score = 0