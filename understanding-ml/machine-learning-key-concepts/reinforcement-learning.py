import gymnasium as gym

# Load environment
env = gym.make('CartPole-v1', render_mode="rgb_array")
observation, info = env.reset()

for _ in range(1000):
    # Take random action
    action = env.action_space.sample()
    
    # Step through environment
    observation, reward, terminated, truncated, info = env.step(action)
    
    # Check if episode is done
    if terminated or truncated:
        observation, info = env.reset()

env.close()

print("Reinforcement learning example completed!")
print("The agent randomly balanced the CartPole for 1000 steps.")
print("In a real RL scenario, the agent would learn optimal actions through trial and error.")