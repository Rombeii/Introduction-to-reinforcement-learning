import time

import gym as gym

if __name__ == '__main__':

    num_steps = 1500
    env = gym.make('FrozenLake-v1', render_mode= "human", desc=None, map_name="8x8", is_slippery=True)
    env.reset()
    env.render()

    for step in range(num_steps):
        # Get random action
        action = env.action_space.sample()

        # Step
        obs, reward, done, info, dictionary = env.step(action)

        # Render the environment
        env.render()
        time.sleep(0.001)

        # If the epsiode ended, reset
        if done:
            env.reset()
