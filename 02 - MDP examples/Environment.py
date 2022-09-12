from Tile import Tile


class Environment:

    def __init__(self, starting_location, tiles):
        self.starting_location = starting_location
        self.current_location = starting_location
        self.tiles: [Tile] = tiles
        self.current_reward = 0
        self.episode_count = 0

    def step(self, action):
        # Move according to the action
        if action == 0 and self.current_location == 0 or action == 1 and self.current_location == len(self.tiles):
            # This will never happen if the rightmost and leftmost tiles are terminal states
            print("unable to move")
        elif action == 0:
            self.current_location = self.current_location - 1
        else:
            self.current_location = self.current_location + 1

        # Check which tile the agent is on
        current_tile = self.tiles[self.current_location]

        # Add reward according to the current tile
        self.current_reward += current_tile.reward

        return [self.current_location, self.current_reward, current_tile.is_episode_ending]

    def reset(self):
        self.current_reward = 0
        self.current_location = self.starting_location
