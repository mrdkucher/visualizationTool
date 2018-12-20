# Graph Traversal Visualizer

This is a visualization tool that uses Python(2.7.10) to print out various tours of vertices in a graph.

![alt text](https://user-images.githubusercontent.com/13631603/50305089-7c902c80-0457-11e9-8a60-ad6f33bcc2d3.png)

```
Usage: python visualizer.py [MST|TSP] [vertices file name] [[mst file name] | [tour 1 file name] [tour 2 file name] ... [tour n file name]]
```

## Formatting

Vertices file format:
```
N
X_1 Y_1
X_2 Y_2
...
X_N Y_N
```

Tours file format:
```
weight
0 1 2 ... N
```
where 0 is the start location, corresponding to vertex (X_1, Y_1), and N is the end location, corresponding to vertex (X_N, Y_N)

MST file format:
```
weight
EDGES
```
With V - 1 edges of format:
```
V1 V2
```

### Example Usage
```
python visualizer.py MST vertices.txt mst.out
python visualizer.py TSP vertices.txt tsp1.out tsp2.out tsp3.out
```
