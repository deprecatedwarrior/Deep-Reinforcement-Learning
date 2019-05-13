import torch 
import torch.nn as nn
import torch.nn.functional as F 

use_dropout = False

class QNetwork(nn.Module):
	""" Policy model that maps state to actions """

	def __init__(self, state_size, action_size):
		""" Initialize parameters and build model """
		super().__init__()

        # Network structure
		hidden_layers_units = [128, 64, 32]
		keep_prob = 0.5

		# Add the first layer
		self.layers = nn.ModuleList([nn.Linear(state_size, hidden_layers_units[0])])

		# Add more hidden layers 
		layer_sizes = zip(hidden_layers_units[:-1], hidden_layers_units[1:])
		self.layers.extend([nn.Linear(h1, h2) for h1, h2 in layer_sizes])

		# Add last layer 
		self.output = nn.Linear(hidden_layers_units[-1], action_size)

		# Dropout
		self.dropout = nn.Dropout(p=1-keep_prob)

	def forward(self, x):
		""" Forward pass """

		for layer in self.layers:
			x = F.relu(layer(x))
			if use_dropout:
				x = self.dropout(x)

		x = self.output(x)

		return x

if __name__ == '__main__':

	net = QNetwork(state_size=37, action_size=4)
	print("net:", net)
