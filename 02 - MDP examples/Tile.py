class Tile:
    def __init__(self, reward, is_episode_ending) -> None:
        super().__init__()
        self.reward = reward
        self.is_episode_ending = is_episode_ending
