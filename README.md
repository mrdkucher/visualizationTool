This is a visualization tool that uses Python 3 to print out various tours of vertices in a graph.

Usage: python visualizer.py [vertices file name] [tour 1 file name] [tour 2 file name] ... [tour n file name]

vertices file format:

N
X_1 Y_1
X_2 Y_2
...
X_N Y_N

tours file format:

weight
0 1 2 ... N

where 0 is the start location, corresponding to vertex (X_1, Y_1), and N is the end location, corresponding to vertex (X_N, Y_N)