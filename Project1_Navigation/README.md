# Project 1: Navigation
This project aims at training a smart agents that navigates and collects yellow bananas from a large, square banana world created in Unity ML agents. 
We train a Deep Q Network to accomplish this task. 

## Introduction
For this project, we will train an agent to navigate (and collect bananas!) in a large, square world.
A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana. Thus, the goal of your agent is to collect as many yellow bananas as possible while avoiding blue bananas.
The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around the agent's forward direction. Given this information, the agent has to learn how to best select actions. Four discrete actions are available, corresponding to:
-	0 - move forward.
-	1 - move backward.
-	2 - turn left.
-	3 - turn right.

The task is episodic, and in order to solve the environment, the agent must get an average score of +13 over 100 consecutive episodes.

## File Structure
The following files are available:
1. `Navigation.ipynb`: Jupyter notebook that contains the code to train the agent
2. `config.json`: Contains the model training as well as system parameters
3. `dqn_agent.py`: Contains the Agent Class and ReplayBuffer class with associated methods
4. `main.py`: Main script to train the agent for your local machine
5. `model.py`: Defines the Q network class used to map state to action values
6. `Requirements.txt`: Environment dependencies
7. `/saved/DQN_exp/`: Contains the saved model weights
8. `Report.pdf`: Technical report describing the project solution and results
9. `plot.py`: Plot of score per episode

## Getting Started
All environment dependencies can be found in `Requirements.txt`. To run this code, you need an environment with Python 3. The
dependencies can be installed by running the following command:
`pip install requirements.txt`

You can also follow instructions in [nanodegree's prerequisite](https://github.com/udacity/deep-reinforcement-learning/#dependencies) to set up the the required packages and modules.

Download the environment from one of the links below. You need only select the environment that matches your operating system:

- Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
- Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
- Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
- Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)
- (For Windows users) Check out [this link](https://support.microsoft.com/en-us/help/827218/how-to-determine-whether-a-computer-is-running-a-32-bit-version-or-64) if you need help with determining if your computer is running a 32-bit version or 64-bit version of the Windows operating system.

- (For AWS) If you'd like to train the agent on AWS (and have not [enabled a virtual screen](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md)), then please use [this link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux_NoVis.zip) to obtain the environment.


## Instructions to Run
The `Navigation.ipynb` contains the code to train the agent. The saved network weights are present in /saved/DQN_exp/model_train_solved.pth
Run the cells in the notebook to train the agent that navigates the Banana World. 







