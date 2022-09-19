import random

import matplotlib.pyplot as plt
import numpy as np

from Agent import Agent
from Environment import Environment
from Tile import Tile

if __name__ == '__main__':

    # TODO try different alphas
    # TODO try different gammas
    # TODO try different learning rates
    # TODO try without decreasing the learning rate
    # TODO try with different starting positions
    # TODO try without decreasing the learning rate

    # Environment setup
    starting_pos = 2
    tiles = [Tile(-1, True), Tile(0, False), Tile(0, False), Tile(0, False), Tile(0, False), Tile(1, True)]
    agent = Agent()
    environment = Environment(starting_pos, tiles)
    epsilons = []
    rewards = []

    # Q-table initialization
    Q = np.zeros((len(tiles), 2))

    # Hyperparameters
    alpha = 0.7
    discount_factor = 0.9
    epsilon = 1
    max_epsilon = 1
    min_epsilon = 0.01
    decay = 0.001

    train_episodes = 4000
    max_steps = 100

    for episode in range(train_episodes):
        environment.reset()
        state = starting_pos
        reward_earned = 0

        for step in range(max_steps):
            n = random.uniform(0, 1)

            if n > epsilon:
                # Exploit
                action = np.argmax(Q[state, :])
            else:
                # Explore
                action = agent.getAction()

            current_location, reward, is_episode_end = environment.step(action)
            reward_earned -= 0.1

            Q[state, action] = Q[state, action] + alpha * (reward + discount_factor * np.max(Q[current_location, :]) - Q[state, action])

            reward_earned += reward
            state = current_location

            if is_episode_end:
                break

        # epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay * episode)

        if epsilon > min_epsilon:
            epsilon -= decay / 2

        # Adding the total reward and reduced epsilon values
        rewards.append(reward_earned)
        epsilons.append(epsilon)

    print("Training score over time: " + str(sum(rewards) / train_episodes))

    print(Q)
    x = range(train_episodes)
    plt.plot(x, rewards)
    plt.xlabel('Episode')
    plt.ylabel('Training total reward')
    plt.title('Total rewards over all episodes in training')
    plt.show()

    plt.plot(epsilons)
    plt.xlabel('Episode')
    plt.ylabel('Epsilon')
    plt.title("Epsilon for episode")
    plt.show()
