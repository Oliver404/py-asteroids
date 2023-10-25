class GManager:
    STATE_START = 0
    STATE_PLAYING = 1
    STATE_PAUSE = 2
    STATE_GAME_OVER = -1

    START_GAME = 'start'
    GAME_OVER = 'game_over'

    def __init__(self, on_state_change):
        self.playing_state = GManager.STATE_START
        self.on_state_change = on_state_change

    def on(self, event: str): 
        if event == GManager.START_GAME:
            self.playing_state = GManager.STATE_PLAYING
        elif event == GManager.GAME_OVER:
            self.playing_state = GManager.STATE_GAME_OVER

        self.on_state_change()