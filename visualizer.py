import matplotlib.pyplot as plt
import numpy as np
import re
import sys

def visualizeTour(pointsFile, tourFiles):
	#read in points
	vtxFile = open(pointsFile, "rb")
	vtxCount = re.findall('\d+', vtxFile.readline())
	vtxCount = int(vtxCount[0])

	#create array of vertices
	vertices = np.zeros(vtxCount, dtype='i,i').tolist()
	#print(vertices)
	for i in range(vtxCount):
		coords = vtxFile.readline()
		coords = re.findall('\d+', coords)
		vertices[i] = (coords[0], coords[1])

	#create a plot
	tourAxes = np.empty(len(tourFiles), dtype=object)

	tours = np.ndarray(shape=(len(tourFiles), vtxCount), dtype='i')
	sortedVertices = np.ndarray(shape=(len(tourFiles), vtxCount + 1), dtype ='i,i')
	
	#read in tours and create plots
	for i in range(len(tourFiles)):
		tourFile = open(tourFiles[i])
		weight = tourFile.readline()
		vtx = re.findall('\d+', tourFile.readline())
			
		#create a copy of the vertices in the order of the tour
		for v in range(vtxCount):
			tours[i, v] = vtx[v]
			sortedVertices[i, v] = vertices[tours[i, v]]
		
		#include a return to the first vertex of the tour
		sortedVertices[i, vtxCount] = vertices[0]
		
		#get the tour in a format that can be plotted
		vtxX, vtxY = np.array(sortedVertices[i].tolist()).T
		
		tourAxes[i] = plt.subplot(len(tourFiles), 1, i)
		tourAxes[i].plot(vtxX, vtxY, linestyle='-', color='b', markerfacecolor='red', marker='o')
		tourAxes[i].set_title(tourFiles[i] + " - Weight: " + weight)
		plt.show()
	return

def visualizeTree(pointsFile, edgesFile):
	#read in points
	vtxFile = open(pointsFile, "rb")
	vtxCount = re.findall('\d+', vtxFile.readline())
	vtxCount = int(vtxCount[0])

	#create array of vertices
	vertices = np.zeros(vtxCount, dtype='i,i').tolist()
	#print(vertices)
	for i in range(vtxCount):
		coords = vtxFile.readline()
		coords = re.findall('\d+', coords)
		vertices[i] = (coords[0], coords[1])
	
	#read in edges
	eFile = open(edgesFile)
	weight = eFile.readline()
	
	edges = np.zeros(vtxCount - 1, dtype='i,i').tolist()
	for i in range(vtxCount - 1):
		edge = re.findall('\d+', eFile.readline())
		edges[i] = (int(edge[0]), int(edge[1])) 

	x, y = np.array(vertices).T

	plt.plot(x[np.array(edges).T], y[np.array(edges).T], linestyle='-', color='b', markerfacecolor='red', marker='o') 
	plt.title(edgesFile + " - Weight: " +  weight)
	plt.show()
	return

#create a List of each tour to visualize: Max = 4 tours
if(len(sys.argv) < 4):
	print("Error. Usage: python visualizer.py [MST|TSP] [vertices file] [tour 1 file] [tour 2 file] ... [tour n file]")
	exit

vFile = sys.argv[2]
tFiles = sys.argv[3:]

if(sys.argv[1] == "MST"):
	visualizeTree(vFile, tFiles[0])
else:
	visualizeTour(vFile, tFiles)
