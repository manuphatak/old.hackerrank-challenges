![HackerRank]
#Cavity Map
[HackerRank \ Algorithms \ Implementation \ Cavity Map](https://www.hackerrank.com/challenges/cavity-map)

Depict cavities on the map

##Problem Statement

You are given a square $n \times n$ map. Each cell of the map has a value in it denoting the depth of the appropriate area. We will call a cell of the map a cavity if and only if this cell is not on the border of the map and each cell adjacent to it has strictly smaller depth. Two cells are adjacent if they have a common side.

You need to find all the cavities on the map and depict them with character uppercase **X**.

**Input Format**


The first line contains an integer $n$ $(1 \le n \le 100)$, denoting the size of the map. Each of the following $n$ lines contains $n$ positive digits without spaces. A digit (1-9) denotes the depth of the appropriate area.

**Output Format**


Output $n$ lines, denoting the resulting map. Each cavity should be replaced with character `X`.

**Sample Input**


    4
	1112
	1912
	1892
	1234

**Sample Output**


	1112
	1X12
	18X2
	1234

[HackerRank]:https://www.hackerrank.com/assets/brand/typemark_60x200.png