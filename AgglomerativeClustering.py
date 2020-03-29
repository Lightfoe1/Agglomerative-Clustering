import math
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# The array where our clusters will be stored
clusterArray = []
# The array where our raw data is stored
dataPointsArray = []                   
                                                                                                                                                                                
# Displays the points on 3d using matplotlib | dataArray is the input array, the rest is the numpy parameters where zdir=zDirection, s=size, c=color, depthshade=depthShadeFunction
def display3DImage(dataArray, zDirection, size, color, depthShadeFunction):
    if (isinstance(dataArray[0][0], list)):
        # The input is a cluster array
        for i in range(len(dataArray)):
            xArray = makeXYZArray(dataArray[i], 0)
            yArray = makeXYZArray(dataArray[i], 1)
            zArray = makeXYZArray(dataArray[i], 2)
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.scatter(xArray, yArray, zArray, zdir=zDirection, s=size, c=color, depthshade=depthShadeFunction)
    else:
        # The input is unclustered data
        xArray = makeXYZArray(dataArray, 0)
        yArray = makeXYZArray(dataArray, 1)
        zArray = makeXYZArray(dataArray, 2)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(xArray, yArray, zArray, zdir=zDirection, s=size, c=color, depthshade=depthShadeFunction)
    plt.show()

# Randomizing a specified amount of 3d dataPoints with predetermined ranges and returning an array of dataPoints
def randomizePointsOn3D(dimensions, numberOfDatas):
    dataArray = []
    for _ in range(numberOfDatas):
        xTemp = random.randint(0, dimensions)
        yTemp = random.randint(0, dimensions)
        zTemp = random.randint(0, dimensions)
        dataArray.append([xTemp, yTemp, zTemp])
    return dataArray

# Distance calculating function takes two points as parameters and the two points must be as a1 = [x1,y1,z1] a2 = [x2,y2,z2]
def calculateDistanceBetweenTwoPoints(a1, a2):
    xDistance = ((a1[0] - a2[0])**2)
    yDistance = ((a1[1] - a2[1])**2)
    zDistance = ((a1[2] - a2[2])**2)
    distance = math.sqrt(xDistance + yDistance + zDistance)
    return distance

# Calculate center of gravity of given cluster with the format:([x1,y1,z1],[x2,y2,z2]...), with an output of: ([centerX, centerY, centerZ])
def calculateCenterOfGravity(cluster):
    xTotal = yTotal = zTotal = 0
    lengthOfCluster = len(cluster)
    for i in range(lengthOfCluster):
        xTotal += cluster[i][0]
        yTotal += cluster[i][1]
        zTotal += cluster[i][2]
    centerPoint = [(xTotal/lengthOfCluster), (yTotal/lengthOfCluster), (zTotal/lengthOfCluster)]
    return centerPoint

# Delete the given indexes from the give array
def deleteIndexesFromArray(deletionArray, indexArray):
    if (indexArray):
        indexArray.sort()
        c = -1
        while(c >= (0 - len(indexArray))):
            index = indexArray[c]
            deletionArray.pop(index)
            c -= 1

# Create clusters with two points from raw data. Parameters are; 1: Raw array of points with the format:([x1,y1,z1],[x2,y2,z2],...), 2: Array where the clusters will be stored with the output as([[x1,y1,z1],[x2,y2,z2]],...), 3: the maximum distance between two points to be clustered
def doubleClusterMaker(dataArray, clusterStorageArray, maximumClusteringDistance):
    deletionIndexes = []
    for i in range(len(dataArray)):
        # If i is already in a cluster, continue
        if i in deletionIndexes:
            continue
        # Initialize the minimum distance to compare
        lowestDistance = maximumClusteringDistance
        # point1
        a = dataArray[i]
        for t in range(i+1, len(dataArray)):
            # If t is already in a cluster, continue
            if t in deletionIndexes:
                continue
            # point2
            b = dataArray[t]
            # Calculate distance between point1 and point2
            distance = calculateDistanceBetweenTwoPoints(a, b)
            # Check to see if it is the shortest possible distance
            if distance < lowestDistance:
                # If it is save t in order to use later on, and update the shortest distance
                secondPointIndex = t
                lowestDistance = distance
        # If minimum distance is within the accepted range
        if lowestDistance < maximumClusteringDistance:
            # 1:Take second point. 2: make point1 and point2 into a cluster. 3: add this cluster to the cluster array
            b = dataArray[secondPointIndex]
            doubleCluster = [a, b]
            clusterStorageArray.append(doubleCluster)
            # Save the indexes of both points in order to delete them once everything is finished
            deletionIndexes.append(i)
            deletionIndexes.append(secondPointIndex)
    # Delete indexes from raw data
    deleteIndexesFromArray(dataArray, deletionIndexes)

# Merges single points to double clusters if distance is within specified distance, parameters as Raw array of points with the format:([x1,y1,z1],[x2,y2,z2],...), 2: Array where the clusters will be stored with the output as([[x1,y1,z1],[x2,y2,z2]],...), 3: the maximum distance to add a point to a cluster
def clusterAdder(dataArray, clusterStorageArray, maximumAddingDistance):
    deletionIndexes = []
    # Take an unclustered member
    for i in range(len(dataArray)):
        # point1
        a = dataArray[i]
        t = 0
        # Take a cluster
        for t in range(len(clusterStorageArray)):
            # Take every member of the cluster
            for m in range(len(clusterStorageArray[t])):
                # point2
                b = clusterStorageArray[t][m]
                # Calculate distance between point1 and point2
                distance = calculateDistanceBetweenTwoPoints(a, b)
                # If distance is acceptable append point to cluster and add index to the deletion list
                if(distance <= maximumAddingDistance):
                    clusterStorageArray[t].append(a)
                    deletionIndexes.append(i)
                    break
            # To break out of nested loops we use if else structure
            else:
                continue
            break
    # Delete the used points from raw data
    deleteIndexesFromArray(dataArray, deletionIndexes)

# Merges clusters to form new clusters if the clusters' center of gravity are within specified range
def clusterMergerCentreOfGravity(clusterStorageArray, maximumMergingDistance):
    # Take cluster 1 and find centre of gravity
    deletionIndexes = []
    tempClusterArray = []
    for i1 in range(len(clusterStorageArray)):
        if i1 in deletionIndexes:
            continue
        # Centre of gravity of cluster1
        centerPoint1 = calculateCenterOfGravity(clusterStorageArray[i1])
        # Take cluster 2 and find centre of gravity
        for i2 in range(i1+1, len(clusterStorageArray)):
            # Check if cluster is already used
            if i2 in deletionIndexes:
                continue
            # Centre of gravity of cluster 2
            centerPoint2 = calculateCenterOfGravity(clusterStorageArray[i2])
            distance = calculateDistanceBetweenTwoPoints(
                centerPoint1, centerPoint2)
            # If the distance is acceptable
            if (distance <= maximumMergingDistance):
                tempClusterArray.append(
                    clusterStorageArray[i1] + clusterStorageArray[i2])
                deletionIndexes.append(i1)
                deletionIndexes.append(i2)
                break
    # Delete the used clusters
    deleteIndexesFromArray(clusterStorageArray, deletionIndexes)
    # Add temporary cluster array back to the main array
    clusterStorageArray.append(tempClusterArray)

# Merges clusters if any point in cluster1 is within specified distance to any point in cluster2, parameters as the array where the clusters are stored and the distance
def clusterMergercalculateDistanceBetweenTwoPoints(clusterStorageArray, maximumMergingDistance):
    length = len(clusterStorageArray)
    deletionIndexes = []
    # Take cluster1
    for i1 in range(length):
        # If i1 is already used you shouldn't us it a second time
        if i1 in deletionIndexes:
            continue
        # Take point1
        for ip1 in range(len(clusterStorageArray[i1])):
            point1 = clusterStorageArray[i1][ip1]
            # Start from next index to avoid comparing with itself
            # Take cluster2
            for i2 in range(i1+1, length):
                # If i2 is already used you shouldn't use it again
                if i2 in deletionIndexes:
                    continue
                # Take point2
                for ip2 in range(len(clusterStorageArray[i2])):
                    point2 = clusterStorageArray[i2][ip2]
                    # Calculate the distance
                    distance = calculateDistanceBetweenTwoPoints(
                        point1, point2)
                    # If distance is ok merge two clusters and add them to the array
                    if(distance <= maximumMergingDistance):
                        clusterStorageArray.append(
                            clusterStorageArray[i1] + clusterStorageArray[i2])
                        deletionIndexes.append(i1)
                        deletionIndexes.append(i2)
                        break
                else:
                    continue
                break
            else:
                continue
            break
    # Delete the used clusters
    deleteIndexesFromArray(clusterStorageArray, deletionIndexes)

# Clears clusterArray of clusters smaller than the size specified and adds them back to our raw data
def clearSmallClusters(dataArray, clusterStorageArray, minimumClusterSize):
    deletionIndexes = []
    for i1 in range(len(clusterStorageArray)):
        # If the cluster is small add the points back to the raw data
        if(len(clusterStorageArray[i1]) <= minimumClusterSize):
            deletionIndexes.append(i1)
            for i2 in range(len(clusterStorageArray[i1])):
                # Add back to raw data(we don't want any data loss)
                dataArray.append(clusterStorageArray[i1][i2])
    # Delete indexes from clusterArray
    deleteIndexesFromArray(clusterStorageArray, deletionIndexes)

# Makes the x y or z array from the input of points to be used in plotting, as a key use 0 for x, 1 for y, 2 for z
def makeXYZArray(dataArray, key):
    if not isinstance(key, int):
        print("Key is not an integer!!(enter 0,1 or 2)\n")
        return 0
    elif key >= 3:
        print("Key is bigger than 2!!(enter 0,1 or 2)\n")
        return 0
    elif key < 0:
        print("Key is smaller than 0!!(enter 0,1 or 2)\n")
    xyzArray = []
    for i in range(len(dataArray)):
        xyzArray.append(dataArray[i][key])
    return xyzArray


# Randomize the array
dataPointsArray = randomizePointsOn3D(100, 128)
# Print the raw data
print(
    "Raw data before clustering as ([x1,y1,z1], [x2,y2,z2]...): \n", dataPointsArray, "\n")
# Create clusters with the size 2
doubleClusterMaker(dataPointsArray, clusterArray, 15)
# Check if there is any point left available that can be put into a cluster
clusterAdder(dataPointsArray, clusterArray, 15)
# Merge the clusters n times
for _ in range(5):
    clusterMergercalculateDistanceBetweenTwoPoints(clusterArray, 15)
# Clear the small clusters
clearSmallClusters(dataPointsArray, clusterArray, 3)
# Print clusters
print(
    "Clusters as ([point1, point2...],[point1, point2...]...):\n", clusterArray, "\n")
# Print raw data
print(
    "Raw data after clustering as ([x1,y1,z1], [x2,y2,z2]...) \n", dataPointsArray, "\n")
# Display clusters
#display3DImage(clusterArray, 'z', 1, 'blue', True)
# Display raw data that is left behind
display3DImage(dataPointsArray, 'z', 1, 'black', True)
