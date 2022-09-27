import random

import gym as gym
import numpy as np
import matplotlib.pyplot as plt


def train():
    env = gym.make('FrozenLake-v1', render_mode="human", desc=None, map_name="4x4", is_slippery=False)
    env.reset()
    epsilons = []
    rewards = []

    Q = np.zeros((env.observation_space.n, env.action_space.n))

    alpha = 0.7
    discount_factor = 0.9
    epsilon = 1
    max_epsilon = 1
    min_epsilon = 0.01
    decay = 0.001

    train_episodes = 4000
    max_steps = 100

    for episode in range(train_episodes):
        state = env.reset()[0]
        reward_earned = 0

        for step in range(max_steps):
            n = random.uniform(0, 1)

            if n > epsilon:
                # Exploit
                action = np.argmax(Q[state, :])
            else:
                # Explore
                action = env.action_space.sample()

            current_location, reward, is_episode_end, truncated, info = env.step(action)
            # reward_earned -= 0.1

            Q[state, action] = Q[state, action] + alpha * (
                    reward + discount_factor * np.max(Q[current_location, :]) - Q[state, action])

            reward_earned += reward
            state = current_location

            if is_episode_end:
                break

        # epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay * episode)

        if epsilon > min_epsilon:
            epsilon -= decay

        # Adding the total reward and reduced epsilon values
        rewards.append(reward_earned)
        epsilons.append(epsilon)
        print(epsilon)

    print("Training score over time: " + str(sum(rewards) / train_episodes))

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


def random_actions():
    num_steps = 1500
    env = gym.make('FrozenLake-v1', render_mode="human", desc=None, map_name="8x8", is_slippery=True)
    env.reset()
    env.render()

    for step in range(num_steps):
        # Get random action
        action = env.action_space.sample()

        # Step
        obs, reward, done, info, dictionary = env.step(action)

        # Render the environment
        env.render()

        # If the epsiode ended, reset
        if done:
            env.reset()


def use_q_table():
    env = gym.make('FrozenLake-v1', render_mode="human", desc=None, map_name="4x4", is_slippery=False)
    env.reset()
    epsilons = []
    rewards = []

    Q = np.asarray([[0.531441, 0.59049, 0.4782969, 0.531441],
                    [0.531441, 0, 0.43046718, 0.47829679],
                    [0.47829689, 0.58112598, 0.38646091, 0.40949937],
                    [0.42981986, 0, 0, 0.24625991],
                    [0.59049, 0.6561, 0, 0.531441],
                    [0, 0, 0, 0],
                    [0, 0.80656708, 0, 0.30068365],
                    [0, 0, 0, 0],
                    [0.6561, 0, 0.729, 0.59049],
                    [0.6561, 0.81, 0.81, 0],
                    [0.728999, 0.9, 0, 0.71516486],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0.80999999, 0.9, 0.729],
                    [0.81, 0.89999999, 1, 0.81],
                    [0, 0, 0, 0]])

    alpha = 0.7
    discount_factor = 0.9

    train_episodes = 4000
    max_steps = 100

    for episode in range(train_episodes):
        state = env.reset()[0]
        reward_earned = 0

        for step in range(max_steps):
            n = random.uniform(0, 1)

            action = np.argmax(Q[state, :])

            current_location, reward, is_episode_end, truncated, info = env.step(action)

            Q[state, action] = Q[state, action] + alpha * (
                    reward + discount_factor * np.max(Q[current_location, :]) - Q[state, action])

            reward_earned += reward
            state = current_location

            if is_episode_end:
                break

        rewards.append(reward_earned)

    print("Training score over time: " + str(sum(rewards) / train_episodes))

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


if __name__ == '__main__':
    train()
