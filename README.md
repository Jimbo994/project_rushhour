## Project Rush Hour

The goal of this project was to write algorithms that could solve a number of Rush Hour boards ranging from size 6x6 to 12x12.
A Breadth First Search, Limited Depth First and Random algorithm were implemented.
Breadth First Search is able to solve problems 1 untill 6. But has not been able to solve problem 7 yet.
Running 9x9 Rush hour boards on Breadth first may take several hours.
Random is able to solve all problems, but since it is random these may not be the best solutions.
Limited Depth-first is not advisable to use to solve Rush hour boards.

Custom boards can also be created. See custom boards conditions below.
Small adjustments to code needs to be made to run those custom boards at other dimensions than 6x6, 9x9 and 12x12.

Make sure to install python before you start.

**Installation**

* Install [Python](https://www.python.org/) 2.7.10 or higher

Usage
---

The "rushhour.py" file contains a a general purpose Vehicle and Board class. And also acts as a script
that accepts command line arguments to choose the wanted algorithm and problem. Problems are provided in the problems directory.<br>
rushhour.py can be run with:
```
python rushhour.py algorithm problems/problem
```
where algorithm can be: 
```
  breadthfirst
  random
  depthfirst
```
where problem can be
```
1,2,3,4,5,6 or 7.
```

rushhour.py will then transform a problem into a board and solve it
```
_ _ a A A b
_ _ a _ _ b
_ _ a x x b
_ _ _ c B B
C D D c _ _
C _ _ c E E
```

Visualisation
---
A simple visualisation was implemented for breadth first search since this algorithm gives best results.
visualisation.py can be run as follows:

```
python visualisation.py problems/problem
```
Mind that on changing board dimensions, some code in __INIT__ needs to be adjusted, like board width and height.
Also the win function needs to be adjusted to dimensions.


Making a custom board
---

*Requirements*

* A vehicle must have the following format: ID X-Coordinate, Y-Coordinate, Orientation (example aCAV)
* Coordinates need to be in capital letters where A stands for 0, B stands for 1 etc
* Vehicles cannot have bigger coordinates than board dimensions
* The red car has to have ID: 'x'
* The red car needs to be placed in the middle of the boards (see win function in rushhour.py)
* Cars need to have small letters 
* Trucks need to have big letters
* 6x6 by six boards need to be named 1, 2 or 3. 9x9 boards need to be name 4, 5 or 6. 12x12 boards need to be named 7
* If you want to use different names for boards, If statements on line 151 needs to be adjusted.

*example of a configuration*
```
aCAV
ADAH
bFAV
xDCH
cDDV
BEDH
CAEV
DBEH
EEFH
```

By
---
*Andrea van den Hooff  (10439080)<br>
Lisa Habermehl (10549404)<br>
Jim Boelrijk (10452506)*

