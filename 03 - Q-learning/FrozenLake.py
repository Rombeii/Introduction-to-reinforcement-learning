import random

import gym as gym
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    num_steps = 1500
    env = gym.make('FrozenLake-v1', render_mode= "human", desc=None, map_name="4x4", is_slippery=False)
    # env = gym.make('FrozenLake-v1', render_mode= "human", desc=None, map_name="4x4", is_slippery=False)
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