# Hanoi
An exploration of the towers of hanoi problem, solving it iteratively and recursively through pattern analysis

The towers of Hanoi problem is an old classic in computer science classrooms. This is mostly due to the fact that

it can be solved with a pretty simple recursive algorithm. However the problem gets a lot more interesting when asked

to look at it iteratively. 

###The Iterative Solution

The Towers of Hanoi problem is extremely interesting due to the number of patterns that are going on within the problem

that many people don't even realize. In order for me to start explaining the iterative solution, I would like you to first

take a look at this 4 disk puzzle solution. While watching this solution, pay close attention to the smallest disk. Watch 

only the smallest disk and what direction it moves in. 


![alt text](https://github.com/jjrylearn/Hanoi/blob/master/animations/hanoi.gif "puzzle solution n=4")

Notice how the smallest disk moves in a distinct pattern. It moves from the first pole, to the second pole, to the third

pole, back to the first pole and continues with this pattern throughout the entirety of the solution. 

Now that you see this, try and take a look at the second smallest disk, and the third smallest disk. 