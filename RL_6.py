import numpy as np

# Define the environment
# For this example, let's consider a simple grid world with 3 states (0, 1, 2) and 2 possible actions (0, 1)
num_states = 3
num_actions = 2
R = np.array([[0, -10], [-10, 10], [10, -10]])  # Reward matrix
Q = np.zeros((num_states, num_actions))  # Q-values

# Hyperparameters
learning_rate = 0.8
discount_factor = 0.95
exploration_prob = 0.2
num_episodes = 1000

# Q-Learning algorithm
for episode in range(num_episodes):
    state = 0  # Starting state
    done = False
    
    while not done:
        if np.random.rand() < exploration_prob:
            action = np.random.randint(num_actions)  # Explore (random action)
        else:
            action = np.argmax(Q[state, :])  # Exploit (choose action with highest Q-value)
        
        next_state = np.random.choice(num_states, p=[0.5, 0.5])  # Random transition to next state
        reward = R[state, action]
        
        Q[state, action] += learning_rate * (reward + discount_factor * np.max(Q[next_state, :]) - Q[state, action])
        
        state = next_state
        
        if state == 2:
            done = True

# After training, you can use the learned Q-values to make decisions in the environment.
# For example, to choose an action in a given state:
state = 0
action = np.argmax(Q[state, :])
print(f"In state {state}, choose action {action}")
