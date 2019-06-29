# Project 3: Collaboration and Competition
The purpose of this project is to apply RL algorithms to train two agents simultaneously that are capable of collaborating (by controlling rackets to bounce a ball over a net) to keep a table tennis ball on the table. This is for an episodic task and the overall score depends on the collaboration of both the agents. 

## Introduction
In this project, we will work with the Unity ML Agents: Tennis Environment. 
![Environment](https://github.com/kauravin/Deep-Reinforcement-Learning/blob/master/Project3_Collaboration_Competition/env.png)

* In this environment, two agents control rackets to bounce a ball over a net. If an agent hits the ball over the net, it receives a reward of +0.1. If an agent lets a ball hit the ground or hits the ball out of bounds, it receives a reward of -0.01. Thus, the goal of each agent is to keep the ball in play.
* The observation space consists of 8 variables corresponding to the position and velocity of the ball and racket. Each agent receives its own, local observation. Two continuous actions are available, corresponding to movement toward (or away from) the net, and jumping.
* The task is episodic, and in order to solve the environment, your agents must get an average score of +0.5 (over 100 consecutive episodes, after taking the maximum over both agents). Specifically,
  * After each episode, we add up the rewards that each agent received (without discounting), to get a score for each agent. This yields 2 (potentially different) scores. We then take the maximum of these 2 scores.
  * This yields a single score for each episode.
The environment is considered solved, when the average (over 100 episodes) of those scores is at least +0.5.


## File Structure
The following files are available:

* Tennis.ipynb: Jupyter notebook that contains the code to train the agent
* dqn_agent.py: Contains the Agent Class, ReplayBuffer class and OUNoise class with associated methods
* model.py: Defines the Actor and critic classes used to train the agent
* requirements.txt: Environment dependencies
* 2 checkpoint files: Saved model weights for the solved environment corresponding to both actor and critic networks
* Report.pdf: Technical report describing the project solution and results
* rewards_per_episodes.py: Plot of rewards per episode

## Getting Started
All environment dependencies can be found in requirements.txt. To run this code, you need an environment with Python 3. The dependencies can be installed by running the following command: pip install requirements.txt

You can also follow instructions in nanodegree's prerequisite to set up the the required packages and modules.

Download the environment from one of the links below. You need only select the environment that matches your operating system:
Note: Downloading Unity is not required

Linux: click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Linux.zip)

Mac OSX: click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis.app.zip)

Windows (32-bit): click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Windows_x86.zip)

Windows (64-bit): click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Windows_x86_64.zip)

(For Windows users) Check out [this link](https://support.microsoft.com/en-us/help/827218/how-to-determine-whether-a-computer-is-running-a-32-bit-version-or-64) if you need help with determining if your computer is running a 32-bit version or 64-bit version of the Windows operating system.

(For AWS) If you'd like to train the agent on AWS (and have not enabled a virtual screen), then please use [this link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Linux_NoVis.zip) to obtain the environment.

## Instructions to Run
* The Tennis.ipynb contains the code to train the agent. The saved network weights are present as checkpoint_actor.pth and checkpoint_critic.pth for both the networks. Run the cells in the notebook to train the agent for the Tennis environment.
* To change the network architecture, please modify model.py
* To experiment with other hyperparamters, please modify dqn_agent.py
