#TOWERS OF HANOIIIII
#JOSHUA LEARN

# Imports
import sys
import math
import copy
import numpy as np
# 
#------------Number of moves to solve-------------
count = 0
#-------------------------------------------------

#3 Stacks, one for each pole ---------------------
poleOne = [ float("inf"), ]
poleTwo = [ float("inf"), ]
poleThree = [ float("inf"), ]
# ------------------------------------------------

# DIAGRAM ########################################
# 
#	 ||         ||         ||
#	 ||         ||         ||
#	 ||         ||         ||
#	 ||         ||         ||
#	  1          2          3
##################################################

# keep the poles in an array for quick referencing
poles = [0, poleOne, poleTwo, poleThree]
# ------------------------------------------------

N = int(sys.argv[1])

# Start all the disks out on poleOne (append them backwards since we are treating these as stacks)
for i in range(N,0,-1):
	poleOne.append(i)

# One more array to show what the end result should be on poleThree
endResult = poleOne[:]
# -----------------------------------------------------------------

################################< METHODS >#######################################################
# 
# # Method to update the array of poles, this is to be used whenever any move is made (UNNECESSARY)
# def updateGame():
# 	poles = [0, poleOne, poleTwo, poleThree]

# Method to check if a move is viable
def viableMove(fromPole, toPole):
	if fromPole>3 or fromPole<1 or toPole>3 or toPole<1:
		return False
	if poles[fromPole][-1] < poles[toPole][-1]:
		return True
	return False

# pretty self explanatory
def makeMove(fromPole, toPole):
	if viableMove(fromPole, toPole):
		poles[toPole].append( poles[fromPole].pop() )
		print("Disk ",poles[toPole][-1]," from pole ", fromPole-1, " to pole ", toPole-1)

# Checks if poleThree has all of the disks stacked onto it 
def isFinished():
	return np.array_equal(poleThree, endResult)

def findLargestPossibleMove(isPoleOneViable, isPoleTwoViable, isPoleThreeViable):

	movePieces = [float("-inf"), ]
	if isPoleOneViable:
		movePieces.append(poles[1][-1])
	else:
		movePieces.append(0)
	if isPoleTwoViable:
		movePieces.append(poles[2][-1])
	else:
		movePieces.append(0)
	if isPoleThreeViable:
		movePieces.append(poles[3][-1])
	else:
		movePieces.append(0)

	return movePieces.index( max(movePieces) ) 

def recursivelySolve(numDisks, fromPole, toPole):
	# Used for counting the number of moves
	global count
	count+=1
	#---------------------------------------

	if numDisks==1:
		makeMove(fromPole, toPole)
	else:
		recursivelySolve(numDisks-1, fromPole, 6 - fromPole - toPole)
		makeMove(fromPole, toPole)
		recursivelySolve(numDisks-1, 6 - fromPole - toPole, toPole)

def iterativelySolve(fromPole, toPole):
	global N
	global count
	moveDefinitionArray = [float("inf"),]
	for i in range(1,N+1):
		if N%2==0:
			moveDefinitionArray.append((-1)**(i+1))
		if N%2==1:
			moveDefinitionArray.append((-1)**(i))
	print(moveDefinitionArray)
	poleOneTo = None
	poleTwoTo = None
	poleThreeTo = None



	while isFinished()!=True:
		count+=1
		# print(poles)
		if poles[1][-1]==float("inf"):
			poleOneTo = 10
		else:
			if moveDefinitionArray[ poles[1][-1] ]==-1:
				poleOneTo = 3
			else:
				poleOneTo = 2

		if poles[2][-1]==float("inf"):
			poleTwoTo = 10
		else:
			poleTwoTo = (2 + ( moveDefinitionArray[ poles[2][-1] ] )) 

		if poles[3][-1]==float("inf"):
			poleThreeTo = 10
		else:
			poleThreeTo = (3 + ( moveDefinitionArray[ poles[3][-1] ] )) % 3

		maxMove = findLargestPossibleMove( viableMove( 1 , poleOneTo) , viableMove( 2 , poleTwoTo ) , viableMove( 3 , poleThreeTo ) )
		if maxMove==1:
			makeMove( 1, poleOneTo )
		if maxMove==2:
			makeMove( 2, poleTwoTo)
		if maxMove==3:
			makeMove( 3, poleThreeTo)


	# print(moveDefinitionArray)


iterativelySolve(1, 3)
# recursivelySolve(N, 1, 3)		
print(isFinished(), " in ", count, " moves.")

# End program
# Unravel acoustic