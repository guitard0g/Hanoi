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
poles = [poleOne, poleTwo, poleThree]
# ------------------------------------------------

N = int(sys.argv[1])
holder1 = sys.argv[2]
holder2 = sys.argv[3]
holder3 = sys.argv[4]
poleOneTemp = []
poleTwoTemp = []
poleThreeTemp = []
for i in range(len(holder1)):
	poleOneTemp.append(holder1[i])
poleOneTemp.sort()

for i in range(len(holder2)):
	poleTwoTemp.append(holder2[i])
poleTwoTemp.sort()

for i in range(len(holder3)):
	poleThreeTemp.append(holder3[i])
poleThreeTemp.sort()

for i in range(len(holder1)-1,-1,-1):
	poleOne.append(int(poleOneTemp[i]))

for i in range(len(holder2)-1,-1,-1):
	poleTwo.append(int(poleTwoTemp[i]))

for i in range(len(holder3)-1,-1,-1):
	poleThree.append(int(poleThreeTemp[i]))

# print(poles)
# if len(sys.argv)==5:
# 	pass
# if len(sys.argv)==6:
# 	pass
# if len(sys.argv)==7:
# 	pass

# Start all the disks out on poleOne (append them backwards since we are treating these as stacks)
endResult = []
for i in range(N,0,-1):
	endResult.append(i)

# One more array to show what the end result should be on poleThree
# -----------------------------------------------------------------

################################< METHODS >#######################################################
# 
# # Method to update the array of poles, this is to be used whenever any move is made (UNNECESSARY)
# def updateGame():
# 	poles = [0, poleOne, poleTwo, poleThree]

# Method to check if a move is viable
def viableMove(fromPole, toPole):
	if fromPole>2 or fromPole<0 or toPole>2 or toPole<0:
		return False
	if poles[fromPole][-1] < poles[toPole][-1]:
		return True
	return False

# pretty self explanatory u stupid 
def makeMove(fromPole, toPole):
	if viableMove(fromPole, toPole):
		poles[toPole].append( poles[fromPole].pop() )
		print(fromPole, " -> ", toPole)

# Checks if poleThree has all of the disks stacked onto it 
def isFinished():
	return np.array_equal(poleTwo, endResult)

def findLargestPossibleMove(isPoleOneViable, isPoleTwoViable, isPoleThreeViable):

	movePieces = []
	if isPoleOneViable:
		movePieces.append(poles[0][-1])
	else:
		movePieces.append(0)
	if isPoleTwoViable:
		movePieces.append(poles[1][-1])
	else:
		movePieces.append(0)
	if isPoleThreeViable:
		movePieces.append(poles[2][-1])
	else:
		movePieces.append(0)

	return movePieces.index( max(movePieces) ) 


def iterativelySolve(fromPole, toPole):
	global N
	global count
	moveDefinitionArray = [float("inf"),]
	for i in range(1,N+1):
		if N%2==0:
			moveDefinitionArray.append((-1)**(i))
		if N%2==1:
			moveDefinitionArray.append((-1)**(i+1))
	poleOneTo = None
	poleTwoTo = None
	poleThreeTo = None



	if isFinished()!=True:
		print(poles)
		count+=1
		if poles[0][-1]==float("inf"):
			poleOneTo = 10
		else:
			if moveDefinitionArray[ poles[0][-1] ]==-1:
				poleOneTo = 2
			else:
				poleOneTo = 1

		if poles[1][-1]==float("inf"):
			poleTwoTo = 10
		else:
			poleTwoTo = (1 + ( moveDefinitionArray[ poles[1][-1] ] )) 

		if poles[2][-1]==float("inf"):
			poleThreeTo = 10
		else:
			poleThreeTo = (2 + ( moveDefinitionArray[ poles[2][-1] ] )) % 3

		maxMove = findLargestPossibleMove( viableMove( 0 , poleOneTo) , viableMove( 1 , poleTwoTo ) , viableMove( 2 , poleThreeTo ) )
		if maxMove==0:
			makeMove( 0, poleOneTo )
		if maxMove==1:
			makeMove( 1, poleTwoTo)
		if maxMove==2:
			makeMove( 2, poleThreeTo)
	print(poles)


	# print(moveDefinitionArray)


iterativelySolve(1, 2)
# # recursivelySolve(N, 0, 2)		
# print(isFinished(), " in ", count, " moves.")

# End program
# Unravel acoustic