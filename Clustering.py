#           Instruction

# Use Switch ( -d ) for Dataset
# Use Switch ( -cc ) for Cluster Centroids value ( Number of Cluster ( K ) )
# Use Switch ( -ol ) for OutputLevel; like y or target
# Example of an input given below -->
# py Clustering.py -d Clustering.csv -cc 2 -ol Y

import sys
import numpy as np
import pandas as pd
import Class

if __name__ == '__main__':
    NumOfParams = len(sys.argv)
    print("\nNumber of Parameter is : ", NumOfParams)

    Class.Clustering.set_default_value(0)
    Class.Clustering.read_switch(NumOfParams)

    print("Dataset Name is             (-b) : ", Class.Clustering.datasetName)
    print("Cluster Centroids value is (-cc) : ", Class.Clustering.cc)
    print("OutputLevel is             (-ol): ", Class.Clustering.outputLevel)

    Class.Clustering.read_dataset(Class.Clustering.datasetName)
    print("\n", Class.Clustering.x)
    print("\n", Class.Clustering.y)

    x = (Class.Clustering.x.to_numpy()).T.flatten()
    y = (Class.Clustering.y.to_numpy()).T.flatten()

    if len(x) < int(Class.Clustering.cc):
        print("\n************************************ Warning ************************************\n")
        print("*** Cluster Centroids value is higher than X size which is not possible.Highest ***")
        print("***          cluster centroids acceptable for this dataset is : ",len(x), "            ***")
        print("***                   So, taking highest Cluster Centroids value                ***")
        print("\n************************************ Warning ************************************\n")
        Class.Clustering.cc = str(len(x))

    selected_Centroid = Class.Clustering.select(x, y, int(Class.Clustering.cc))
    print("\n")
    print("Selected Centroid Points: ")
    print(selected_Centroid)

    all_points = Class.Clustering.select(x, y, len(x))
    print("ALl Points: ")
    print(all_points)

    minimum_Distance_index_number = np.zeros((len(all_points),), dtype=int)

    count = 1
    while True:
        previous_minimum_Distance_index_number = minimum_Distance_index_number
        print("\n\n\nIterations Number : ", count)
        flag = True
        all_Calculated_Distance = Class.Clustering.all_distance(selected_Centroid, all_points)
        minimum_Distance_index_number = Class.Clustering.cluster_points_minimum_distance_index_number(all_Calculated_Distance)

        for i in range(len(minimum_Distance_index_number)):
            if minimum_Distance_index_number[i] != previous_minimum_Distance_index_number[i]:
                flag = False

        if flag:
            print("\nAs current Cluster points are the same as previous Cluster points. We can stop the process now.")
            break

        selected_Centroid = Class.Clustering.new_selected_centroid_points(selected_Centroid, all_points, minimum_Distance_index_number)
        count += 1

    print("So, The Final Centroid Points: ")
    print(selected_Centroid)

    print("\nSo, The Final Cluster Points: ")
    for i in range(len(selected_Centroid)):
        Class.Clustering.cluster_points(all_points, minimum_Distance_index_number, i)











