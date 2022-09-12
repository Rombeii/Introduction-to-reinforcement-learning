import matplotlib.pyplot as plt

from Agent import Agent
from Environment import Environment
from Tile import Tile

if __name__ == '__main__':
    tiles = [Tile(-1, True), Tile(0, False), Tile(0, False), Tile(0, False), Tile(0, False), Tile(1, True)]
    agent = Agent()
    environment = Environment(2, tiles)
    rewards = []

    for step in range(100):
        action = agent.getAction()

        current_location, reward, is_episode_end = environment.step(action)

        if is_episode_end:
            rewards.append(reward)
            environment.reset()

    plt.plot(rewards, 'o')
    plt.show()
