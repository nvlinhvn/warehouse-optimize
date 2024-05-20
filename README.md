# Warehouse item placement optimization

Finding the best location for some items in an aisle in an warehouses.
In this warehouse aisle, we are storing a number of items that are to be picked up and shipped to customers.

We want to place the items such that we minimise the distance that the warehouse staff need to move when picking the orders.
This maximises the overall efficiency of the warehouse.

we also have a list of representative orders.

## Problem Definition

Figure out in what sequence to put the items in this aisle, and where the items should be placed relative to the door.
(identifying relative x-coordinate of each item w.r.t the door)

The objective is to minimize the total distance that staff needs to move to pick up the items.

Assumption:

- Only one aisle in the whole warehouse.
- The coworkers that pick up the items start by entering through the door, and they finish by exiting through the same door.
- Given the sequence of items, they are placed as closely as possible, with respect to their respective widths.
- The door is located somewhere inside the aisle. You can e.g. imagine that the aisle runs from west to east and the door is located in the north wall. The x-coordinate indicates how far east the door is placed, relative to the middle of the first item (which is assumed to be at `x=0`). Larger x-values mean that the door is placed further to the east.
- Items are going to be picked in the sequence given by the order. Sequence can be changed for optimizing purpose
- There is an unlimited amount of items available to be picked in each of the item locations

## Data

In the file `data.json` contains:

- For every item to be placed, the width it occupies in the aisle
- A list of items
- A list of orders, where each order is a list of articles to be picked up

## Problem Formulation

##### Let the non-negative x-coordinate of door offset, and 14 items as follow:

$$\begin{bmatrix} \text{door offset} \\ \text{Billy} \\ \text{Poang} \\ ... \\ \text{Dvala} \end{bmatrix} = \begin{bmatrix} X_{0} \\ X_{1} \\ ... \\ X_{14} \end{bmatrix} $$

##### The objective function needs to be optimized is (15 variables):

$
\begin{align}
\text{argmin}
\sum \limits _{order=1} ^{m} \big(\sum \limits _{i=1} ^{n - 1} \big\lvert{X_{i+1} - X_{i}}\big\rvert + \big\lvert{X_{n} - X_{0}}\big\rvert \big)
\end{align}
$  
where:

- $X_{i}$: X-coordinate of item $i$. <br>
- $X_0$: Door offset <br>
- $m$: Total order (in this case study $m = 50$) <br>
- $n$: Article list per order<br>

##### Constraints. Since all items are placed as closely as possible, the constraints can be described:

$\begin{align}
\frac{1}{2}(w_{i} + w_{j}) \leq \big\lvert{X_i - X_j}\big\rvert \leq W - \frac{1}{2}(w_{i} + w_{j}) \newline
\frac{1}{2}w_{i} \leq X_{i} \leq W - \frac{1}{2}w_{i} \newline
\frac{1}{2}min(w_{i}) \leq X_{0} \leq W - \frac{1}{2}min(w_{i})
\end{align}
$
where:

- $w_{i}, w_{j}$: width of item $i$ $\neq$ $j$. <br>
- $W$: Total width of all 14 items <br>
- $min(w_{i})$: Smallest width value <br>

##### Since the result is absolute coordinate, and we want the first item to be at 0. So the output needs to substract the minimal absolute coordinates. Items x-coordinate is:

- 'Malm': 0.0 <br>
- 'Dvala': 2.98 <br>
- 'Ribba': 3.5 <br>
- 'Lack': 4.25 <br>
- 'Ektorp': 7.1 <br>
- 'Billy' and door_offset: 10.9 <br>
- 'Fargrik': 12.55 <br>
- 'Klippan': 14.3 <br>
- 'Stockholm': 17.15 <br>
- 'Poang': 18.85 <br>
- 'Frakta': 19.6 <br>
- 'Docksta': 21.15 <br>
- 'Kallax': 23.3 <br>
- 'Raskog': 24.75 <br>
  --> Total Distance = 1754.1

##### Improvement. The above result is assumed the sequence per order is fixed. But we can actually permute the sequence to optimize the walking distance for each order (>= 2 item in sequence). This can be done at following simple algorithm

FUNCTION NextItem <br>

> Helper Recursive function to find the next nearest item of the given item <br>

FOR each order <br>

> IF order has at least 2 items THEN <br>
>
> > COMPUTE default distance of sequence <br>
> > FOR item on sequence <br>
> >
> > > SET item first in the sequence <br>
> > > CALL NextItem <br>
> > > COMPUTE Distance of sequence <br>
> > > REPLACE default sequence by sequence with minimal distance <br>

##### order sequence is changed at {1, 2, 5, 6, 9, 10, 12, 21, 22, 26, 27, 29, 32, 34, 37, 38, 45, 46, 48, 50}

##### Total (new) distance = 1440.35
