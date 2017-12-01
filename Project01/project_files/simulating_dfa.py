# simulating_dfa.py
# @author Diego Valdes
# CSCE 355
# Nov 14, 2017

import fileinput

'''------------------------------------------------------------------------------------------------
Creates a state node
'''
class State(object):

	'''--------------------------------------------------------------------------------------------
	Constructor
	Creates a node with alpha as keys and paths as destinations

	@alpha		array of characters
	@paths		array of destinations
	@accepting	boolean whether state is accepcing
	'''
	def __init__(self, alpha, paths, accepting):

		 self.alpha = alpha
		 self.paths = paths
		 self.accepting = accepting

		 self.nodes = {}

		 for i, key in enumerate(alpha):

		 	# keys are alpha, i are the edges to nodes
		 	self.nodes[key] = paths[i]

		 # print(self.nodes)


alpha = [] # Track alphabet
dfa = [] # Create dfa
paths = [] # Track edges
accept = None # Track accepting states
states = 0 # Number of states
check = 0 # Check if done

# Standard input from console
for line in fileinput.input():

	# Strip carriage return
	line = line.rstrip()

	# Split on ':'
	temp = line.split(":", 1)

	# Get number of states
	if (temp[0] == 'Number of states'):
		states = int(temp[1])

	# Get accepting states
	elif (temp[0] == 'Accepting states'):
		accept = temp[1].split()
		accept = list(map(int, accept))

	# Get alphabet
	elif (temp[0] == 'Alphabet'):
		alphabet = temp[1].split()

		# Accomidate ' ' being part of the alphabet
		if (temp[1][1]  == ' '):
			alpha.append(' ')

		# Go over alphabet
		for i in alphabet[0]:
			alpha.append(i)	# add alphabet to array

	# Go over dfa
	elif (check >= states):

		next = 0 # start at 0
		
		# traverse string and go through dfa
		for i in line:

			try:
				next = dfa[next].nodes[i]
			except Exception as e:
				next = 0

		if (dfa[next].accepting):
			print ('accept')
		else:
			print ('reject')
		
	# Create dfa
	elif(check < states):

		accepting = False
		paths = line.split()
		paths = list(map(int, paths))

		if (check in accept):
			accepting = True

		# Add node to dfa
		check += 1
		dfa.append(State(alpha, paths, accepting))