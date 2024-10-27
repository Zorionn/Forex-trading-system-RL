import numpy as np
import random

# Define the environment as a 2D grid
# 0 indicates free space, -1 indicates obstacles, and 1 indicates the goal
env = np.array([
    [0, -1, 0, 0, 0],
    [0, -1, 0, -1, 0],
    [0, 0, 0, -1, 0],
    [0, -1, 0, 0, 0],
    [0, 0, 0, -1, 1]  # Goal at (4, 4)
])

# Define the possible actions
# 0 = up, 1 = down, 2 = left, 3 = right
actions = [0, 1, 2, 3]

# Define the dimensions of the environment
n_rows, n_cols = env.shape

# Initialize the Q-table with zeros
Q = np.zeros((n_rows, n_cols, len(actions)))

# Hyperparameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Probability of choosing a random action (exploration factor)
num_episodes = 1000  # Number of training episodes

# Function to choose an action based on an epsilon-greedy policy
def choose_action(state):
    if random.uniform(0, 1) < epsilon:
        return random.choice(actions)  # Explore: choose a random action
    else:
        return np.argmax(Q[state[0], state[1], :])  # Exploit: choose the best action

# Function to take a step in the environment
def take_step(state, action):
    # Define the next state based on the chosen action
    if action == 0:  # Up
        next_state = (max(state[0] - 1, 0), state[1])
    elif action == 1:  # Down
        next_state = (min(state[0] + 1, n_rows - 1), state[1])
    elif action == 2:  # Left
        next_state = (state[0], max(state[1] - 1, 0))
    else:  # Right
        next_state = (state[0], min(state[1] + 1, n_cols - 1))
    
    # Check if the next state is an obstacle
    if env[next_state] == -1:
        next_state = state  # Remain in the current state
    
    # Get the reward for moving to the next state
    reward = env[next_state]
    
    return next_state, reward

# Training loop
for episode in range(num_episodes):
    # Initialize the starting state (top-left corner)
    state = (0, 0)
    
    while True:
        # Choose an action based on the current state
        action = choose_action(state)
        
        # Take a step in the environment
        next_state, reward = take_step(state, action)
        
        # Update the Q-value using the Bellman equation
        best_next_action = np.argmax(Q[next_state[0], next_state[1], :])
        Q[state[0], state[1], action] += alpha * (
            reward + gamma * Q[next_state[0], next_state[1], best_next_action] - Q[state[0], state[1], action]
        )
        
        # Transition to the next state
        state = next_state
        
        # Check if we have reached the goal state
        if reward == 1:
            break

def print_q_table(Q, env):
    n_rows, n_cols, n_actions = Q.shape
    actions = ['↑', '↓', '←', '→']  # Action symbols corresponding to [up, down, left, right]

    for i in range(n_rows):
        for j in range(n_cols):
            if env[i, j] == -1:  # Obstacle
                print("  ####  ", end="  ")
            elif env[i, j] == 1:  # Goal
                print("  GOAL  ", end="  ")
            else:
                # Display the Q-values for the state (i, j) with action symbols
                q_values = Q[i, j, :]
                max_q = np.max(q_values)  # To find the best action in this state
                best_actions = [actions[a] for a in range(n_actions) if q_values[a] == max_q]
                best_action_str = ", ".join(best_actions)  # Display multiple best actions if they are tied
                print(f"Q={q_values.round(2)} ({best_action_str})", end="  ")
        print()  # Move to the next line for the next row

# Call the function to print the Q-table
print("Learned Q-values (Q-Table):")
print_q_table(Q, env)

# Print the learned Q-values for each state-action pair
print("Learned Q-values:")
print(Q)