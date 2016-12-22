## Project Rush Hour

The goal of this projects was to write algorithms that could solve a number of boards ranging from size 6x6 to 12x12.
A Breadth First Search, Limited Depth First and Random algorithm was implemented.

Custom boards can also be created in .txt files. See custom boards conditions below.
Small adjustments to code needs to be made to run those custom boards.

Make sure to install python before you start.

**Installation**

* Install [Python](https://www.python.org/) 2.7.10 or higher

Usage
---

The "rushhour.py" file contains a a general purpose Vehicle and Board class. And also acts as a script
that accepts command line arguments to choose the wanted algorithm and problem. Problems are provided in the problems directory.
rushhour.py can be run with:
```
python rushhour.py algorithm problems/problem
```
where algorithm can be: 
```
 breadthfirst
 random
 breadthfirst
```
where problem can be
```
1,2,3,4,5,6 or 7.
```


**custom boards conditions**

*example of a configuration*

aCAV
ADAH
bFAV
xDCH
cDDV
BEDH
CAEV
DBEH
EEFH


*Andrea van den Hooff  (10439080)<br>
Lisa Habermehl (10549404)<br>
Jim Boelrijk (10452506)*

