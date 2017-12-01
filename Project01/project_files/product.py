# product.py
# @author Diego Valdes
# CSCE 355
# Nov 14, 2017
# /home/diego/Downloads/CSCE_355/project_files
# /home/valdeslab/Downloads/Project01/project_files

import sys, fileinput

accept = None # Track accepting states
states = 0 # Number of states
alpha = [] # Track alphabet

# Do the compliment
if len(sys.argv) == 2:

	for line in fileinput.input():

		# Strip carriage return
		line = line.rstrip()

		# Split on ':'
		temp = line.split(":", 1)

		if (temp[0] == 'Number of states'):
			states = int(temp[1])
			print(line)

		# Get accepting states
		elif (temp[0] == 'Accepting states'):
			# print(temp[1])
			accept = temp[1].split()
			accept = list(map(int, accept))

			# Establish new accepting states
			newAccepting = []
			for i in range(0,states):
				if i not in accept:
					newAccepting.append(str(i))

			noAccepting = " ".join(newAccepting)

			print("Accepting states: %s" %(noAccepting))

		# Get alphabet
		elif (temp[0] == 'Alphabet'):
			print (line)

		else:
			print(line)


newNoStates = 1 # Track number of states
firstPass = {} # Track 1st dfa edges
secondPass = {} # Track 2nd dfa edges
translater = {} # Used to identify dfa1 x dfa2 to index
turn = 0 # Track dfa
node = 0 # Track node
acceptOne = [] # Track accepting states first dfa
acceptTwo = [] # Track accepting states second dfa
alphabetPrint = None # record alphabet for easy printing
newAccepting =[] # Accepting states x dfa

# Do the Intersection
if len(sys.argv) == 3:
	#received 2 files

	for line in fileinput.input():

		# Strip carriage return
		line = line.rstrip()

		# Split on ':'
		temp = line.split(":", 1)

		if (temp[0] == 'Number of states'):
			newNoStates *= int(temp[1]) # Get the number of states for intersection

			turn += 1 # Increment turn
			node = 0 # reset node counter

		elif (temp[0] == 'Accepting states'):
			# Accepting states for first dfa
			if turn == 1:
				acceptOne = list(map(int, temp[1].split()))

			# Accepting states for second dfa
			if turn == 2:
				acceptTwo = list(map(int, temp[1].split()))				

		# Get alphabet
		elif (temp[0] == 'Alphabet'):
			alphabet = temp[1].split()
			alphabetPrint = temp[1].strip()

			# Accomidate ' ' being part of the alphabet
			if (temp[1][1]  == ' '):
				alpha.append(' ')

			# Go over alphabet
			for i in alphabet[0]:

				# add alphabet to array
				if i not in alpha:
					alpha.append(i)

		# Get paths of nodes for alphabet
		else:
			paths = list(map(int, line.split()))
			routes = {} # Hold alpha node combinations
			routeHolder = [] # Hold combinations for nodes

			# First dfa
			if turn == 1:
				for i in range(0, len(alpha)):
					# Alphabet character has the path
					routes[alpha[i]] = paths[i]
					
				# add all possible edges to node
				routeHolder.append(routes)
				firstPass[node] = routeHolder
				node += 1 # Increment node count

			# second dfa
			if turn == 2:

				for i in range(0, len(alpha)):

					routes[alpha[i]] = paths[i]
					
				routeHolder.append(routes)
				secondPass[node] = routeHolder
				node += 1

	index = 0
	for i in firstPass:
		for j in secondPass:
			# Create a translator to convert dfa pairings to node index
			newKey = '00' + str(i) + '00' + str(j) # ensures uniqueness of keys
			translater[newKey] = index
			
			# Find new accepting states x dfa
			if i in acceptOne and j in acceptTwo:
				newAccepting.append(str(index))

			index += 1
		
	#Print out the x dfa as we do the work
	print("Number of states: %d" %(newNoStates))
	print("Accepting states: %s" %(' '.join(newAccepting)))
	print("Alphabet: %s" %(alphabetPrint))

	for i in firstPass:
		for j in secondPass:
			toPrint = ''
			test = ''

			for index, k in enumerate(alpha):	
				dest1 = firstPass[i][0][k] # Get the destination for node in dfa 1
				dest2 = secondPass[j][0][k] # Get the destination for the node in dfa 2	
				travel = '00' + str(dest1) + '00' + str(dest2)  # Get where the x of two nodes
				toPrint += str(translater[travel]) + ' '
				test += travel + ' '

			print(toPrint.strip()) # print result
			# print(test)
