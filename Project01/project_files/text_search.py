# text_search.py
# @author Diego Valdes
# CSCE 355
# Nov 14, 2017
# /home/diego/Downloads/CSCE_355/project_files
# /home/valdeslab/Downloads/Project01/project_files

import fileinput

'''------------------------------------------------------------------------------------------------
Creates a state node
'''
class Node(object):

	'''--------------------------------------------------------------------------------------------
	Constructor
	Creates a node with a dictionary to track edges
	'''
	def __init__(self):

		self.edges = {}


noStates = None 	# no of states
noAccepting = None 	# no of accepting states
alphabet = 'abcdefghijklmnopqrstuvwxyz'	# possible alphabet
alpha = set()	# set to track real alphabet
string = []		# array for the string
dfa = []		# array for the dfa

'''-----------------------------------------------------------------------------------------------
Get the line and set up variables
'''
# Standard input from console
for line in fileinput.input():

	# Strip carriage return
	line = line.rstrip()

	noStates = len(line) + 1
	noAccepting = len(line)

	for i in line:
		alpha.add(i) # actual alphabet
		string.append(i) # line to an array

fileinput.close()	

'''-----------------------------------------------------------------------------------------------
Set up first node
'''
stateOne = Node()

for i in alpha:
	# set up first edge from start state
	if i == string[0]: 
		stateOne.edges[i] = 1
	else:
		stateOne.edges[i] = 0

# print(stateOne.edges)
dfa.append(stateOne)

'''-----------------------------------------------------------------------------------------------
Create the dfa
'''
for i, letter in enumerate(string):
	
	# Test if reached the end
	if i+1 == len(string):
		break

	search = string[ :i+1] # array tracking string walk and used to generate comparison[]
	next = string[i+1] # next char in string
	node = i+1 # node working on creating
	comparison = [] # array used to map out back edges
	
	# generate comparison array to walk dfa to generate back edges
	for j in alpha:
		if j != next:
			test = string[ :i+1]
			test.append(j)
			comparison.append(test[1:])

	newNode = Node() # create new node 

	# create edge to next correct char
	for key in alpha:
		if key == next:
			# print("COMPARISON WORKED!!!")
			newNode.edges[next] = node + 1
		else:
			newNode.edges[key] = 0

	dfa.append(newNode) # add node to dfa

	# Walk comparison to get back edges
	for k in comparison:

		dest = 0 # start walking dfa in start state

		# Walk dfa
		for keyCom in k:
			dest = dfa[dest].edges[keyCom]

		dfa[node].edges[keyCom] = dest	# set back edge

'''-----------------------------------------------------------------------------------------------
Print the dfa
'''
print("Number of states: %d" %(noStates))
print("Accepting states: %d" %(noAccepting))
print("Alphabet: %s" %(alphabet))

accepts = str(noAccepting)
accepts += ' '

for state in dfa:

	toPrint = ''
	lastState = ''

	for i in alphabet:

		try:
			edge = str(state.edges[i])
			edge += ' '
			toPrint += edge
			lastState += accepts

		except Exception as e:
			toPrint += '0 '
			lastState += accepts

	print(toPrint.strip())

print(lastState.strip())