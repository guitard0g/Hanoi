# Hanoi
An exploration of the towers of hanoi problem, solving it iteratively and recursively through pattern analysis

##### hanoi.py is the main project file

##### hanoiNextMove.py uses the iterative algorithm to give you the next move in an optimal solution given some arrangement of disks

##### To see the optimal solution for any Towers of Hanoi puzzle run, "python3 hanoi.py N" where N is the number of disks.

The towers of Hanoi problem is an old classic in computer science classrooms. This is mostly due to the fact that

it can be solved with a pretty simple recursive algorithm. However the problem gets a lot more interesting when asked

to look at it iteratively. 

### The Iterative Solution

The Towers of Hanoi problem is extremely interesting due to the number of patterns that are going on within the problem

that many people don't even realize. In order for me to start explaining the iterative solution, I would like you to first

take a look at this 4 disk puzzle solution. While watching this solution, pay close attention to the smallest disk. Watch 

only the smallest disk and what direction it moves in. 


![alt text](https://github.com/jjrylearn/Hanoi/blob/master/animations/hanoi.gif "puzzle solution n=4")

Notice how the smallest disk moves in a distinct pattern. It moves from the first pole, to the second pole, to the third

pole, back to the first pole and continues with this pattern throughout the entirety of the solution. 

Now that you see this, try and take a look at the second smallest disk, and the third smallest disk. The second disk clearly

follows the same pattern, but moving in the opposite direction from first pole, to third pole, to second pole, back to first. 

The third smallest disk follows the same pattern as the first. Hmm..... what's going on here???

It turns out that if we number the disks 1, 2, 3...., N, where N is the largest disk, then 

#### all of the disks with the same parity (even or odd) of N will move strictly in one direction, while all the disks with 

#### parity of N+1 will move strictly in the opposite direction.

Using this we can look at any towers of hanoi setup with different disks on different poles and be able to easily tell what 

the next optimal move is in O(1) time to advance towards the solution. This is one of the algorithms implemented in my 

programmatic exploration of this puzzle. 


### The Recursive (boring) Solution

In my exploration of this problem, I implemented the recursive solution as well. The recursive solution is very well known.

The premise goes like this: In order to solve the Towers of Hanoi puzzle for N disks, we must first move the top N-1 disks

to the alterative pole, then move the Nth disk to the destination pole, and then move the N-1 disks on top of the Nth disk

on the destination pole. 

The pseudo code looks like this:

```python

def recursivelySolve(numDisks, startPole, destinationPole):

	if numDisks==1:
		moveDisk(startPole, destinationPole)
	else:
		recursivelySolve(numDisks-1, startPole, alternativePole)
		makeMove(startPole, destinationPole)
		recursivelySolve(numDisks-1, alternativePole, destinationPole)
```
