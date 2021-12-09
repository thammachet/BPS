import math
import numpy as np
def distance(point1,point2):
    return math.sqrt(math.pow(point1[0]-point2[0],2)+math.pow(point1[1]-point2[1],2)+math.pow(point1[2]-point2[2],2))

# Calculate angle between two vector
def angle(vector1,vector2):
    dot = np.dot(vector1,vector2)
    det = np.linalg.norm(vector1)*np.linalg.norm(vector2)
    return math.degrees(math.acos(dot/det))

# Calculate vector from two point
def vector(point1,point2):
    vector = np.array([point2[0]-point1[0],point2[1]-point1[1],point2[2]-point1[2]])
    return vector

# Calculate angle between three points
def angle_3(point1,point2,point3):
    vector1 = vector(point1,point2)
    vector2 = vector(point3,point2)
    return angle(vector1,vector2)


def flip_graph(graph):
    graph_flip = np.zeros(graph.shape)
    for i in range(graph.shape[0]):
        for j in range(graph.shape[1]):
            graph_flip[i,j] = graph[graph.shape[0]-i-1,graph.shape[1]-j-1]
    return graph_flip