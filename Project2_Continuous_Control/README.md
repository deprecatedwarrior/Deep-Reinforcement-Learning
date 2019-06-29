# Project 2: Continuous Control
The purpose of this project is to apply RL algorithms to scenarios with continuous action spaces. We intend to use the actor critic methods that utilize policy gradients (actor) as well as value based (critic) to train a smart agent that solves the given environment. 

## Introduction
In this project, we will work with the Reacher Environment. 
![Environment](https://github.com/kauravin/Deep-Reinforcement-Learning/blob/master/Project2_Continuous_Control/reacher.png)
 
What we see in the figure are double jointed robotic arms that can move toward a target location. A reward of +0.1 is provided for each step that the agent's hand is in the goal location. Thus, the goal of the agent is to maintain its position at the target location for as many time steps as possible.

### State and Action Spaces
The observation space consists of 33 variables corresponding to position, rotation, velocity, and angular velocities of the arm. Each action is a vector with four numbers, corresponding to torque applicable to two joints. Every entry in the action vector should be a number between -1 and 1.

### Solving the environment
There are 2 versions of the problem that we can work on. 
1.	Version 1 has a single robotic arm. It is an episodic task and the aim is to get an average score of +30 over 100 consecutive episodes. 
2.	Version 2 has multiple agents/robotic arms. The aim is to get an average score of +30 0ver 100 consecutive episodes over all agents. Specifically,
•	After each episode, we add up the rewards that each agent received (without discounting), to get a score for each agent. This yields 20 (potentially different) scores. We then take the average of these 20 scores.
•	This yields an average score for each episode (where the average is over all 20 agents).


## File Structure
The following files are available:

* Continuous_Control.ipynb: Jupyter notebook that contains the code to train the agent
* dqn_agent.py: Contains the Agent Class, ReplayBuffer class and OUNoise class with associated methods
* model.py: Defines the Actor and critic classes used to train the agent
* requirements.txt: Environment dependencies
* 4 checkpoint files: Saved model weights for the solved environment (ending with _solved) and the most recent episode, corresponding to both actor and critic networks
* Report.pdf: Technical report describing the project solution and results
* rewards_per_episodes.py: Plot of rewards per episode
## Getting Started
All environment dependencies can be found in Requirements.txt. To run this code, you need an environment with Python 3. The dependencies can be installed by running the following command: pip install requirements.txt

You can also follow instructions in nanodegree's prerequisite to set up the the required packages and modules.

Download the environment from one of the links below. You need only select the environment that matches your operating system:
### Note: This is for version 2 of the project. 
Linux: click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Linux.zip)

Mac OSX: click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher.app.zip)

Windows (32-bit): click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86.zip)

Windows (64-bit): click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86_64.zip)

(For Windows users) Check out [this link](https://support.microsoft.com/en-us/help/827218/how-to-determine-whether-a-computer-is-running-a-32-bit-version-or-64) if you need help with determining if your computer is running a 32-bit version or 64-bit version of the Windows operating system.

(For AWS) If you'd like to train the agent on AWS (and have not enabled a virtual screen), then please use [this link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Linux_NoVis.zip) to obtain the environment.

## Instructions to Run
* The Continuous_Control.ipynb contains the code to train the agent. The saved network weights are present as checkpoint_actor_20agents_solved_new.pth and checkpoint_critic_20agents_solved_new.pth for both the networks. Run the cells in the notebook to train the agent for the Reacher environment.
* To change the network architecture, please modify model.py
* To experiment with other hyperparamters, please modify dqn_agent.py


