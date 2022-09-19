import random


class Agent:
    def __init__(self) -> None:
        super().__init__()

    # 0 means left, 1 means right
    def getAction(self):
        return random.choice([0, 1])
