# Lab 4: K-Means Clustering Implementation
# Student Name: Md. Muktadir Mukto
# Student ID  : 2018-2-60-063

import math
import sys
from sklearn import datasets
import pandas as pd
import numpy as np


class Clustering:
    @property
    def datasetName(self):
        return self.datasetName

    @datasetName.setter
    def datasetName(self, datasetName):
        self.datasetName = datasetName

    @property
    def cc(self):
        return self.cc

    @cc.setter
    def cc(self, Cluster_Centroids):
        self.cc = Cluster_Centroids

    @property
    def x(self):
        return self.x

    @x.setter
    def x(self, x):
        self.x = x

    @property
    def y(self):
        return self.y

    @y.setter
    def y(self, y):
        self.y = y

    @property
    def outputLevel(self):
        return self.outputLevel

    @outputLevel.setter
    def outputLevel(self, outputLevel):
        self.outputLevel = outputLevel

    # This function sets the default value
    def set_default_value(a):
        Clustering.datasetName = "Clustering.csv"
        Clustering.cc = "3"
        Clustering.outputLevel = ""

    # This function reads the given switch value
    def read_switch(NumOfParams):
        for i in range(1, NumOfParams):
            if sys.argv[i].replace(" ", "") == '-d':
                Clustering.datasetName = sys.argv[i + 1]
            elif sys.argv[i].replace(" ", "") == '-cc':
                Clustering.cc = sys.argv[i + 1]
            elif sys.argv[i].replace(" ", "") == '-ol':
                Clustering.outputLevel = sys.argv[i + 1]

    # This function reads the given dataset
    def read_dataset(datasetName):
        if datasetName == "iris":
            data = datasets.load_iris()
            Clustering.x = pd.DataFrame(data.data, columns=data.feature_names)
            dataset_y = data.target
            Clustering.y = pd.DataFrame(dataset_y, columns=['target'])
        else:
            dataset = pd.read_csv(datasetName)
            Clustering.dataset_target_split(dataset,Clustering.outputLevel)

    # This function splits the target
    def dataset_target_split(dataset, classLevel):
        if len(classLevel) != 0:
            y = dataset[classLevel]
            y = y.to_frame()
            y.columns = ["Y"]
            Clustering.y = y
            Clustering.x = dataset.drop(classLevel, axis=1)
        else:
            y = dataset.iloc[:, -1]
            y = y.to_frame()
            y.columns = ["Y"]
            Clustering.y = y
            Clustering.x = dataset
            Clustering.x = Clustering.x.iloc[:, :-1]

    # This function select the Cluster
    def select(x, y, n):
        selected = []
        for i in range(n):
            temp = [x[i], y[i]]
            selected.append(temp)
        return selected

    # This function Calculates the distance between two points
    def distance_calculation(a, b):
        return math.sqrt(math.pow((a[0]-b[0]),2)+(math.pow((a[1]-b[1]),2)))

    # This function Calculates the distance between the Cluster and all points
    def all_distance(selected_Cluster_points, all_points):
        print("\nAll Calculated Distance Between Points:")
        all_calculated_distance = []
        for i in range(len(selected_Cluster_points)):
            print("\nDistance Between ", i + 1, " Cluster points to all points.")
            temp = []
            for j in range(len(all_points)):
                value = Clustering.distance_calculation(selected_Cluster_points[i], all_points[j])
                temp.append(value)
            print(temp)
            all_calculated_distance.append(temp)
        return all_calculated_distance

    # This function Calculates the Index number of minimum distance between the Cluster
    def cluster_points_minimum_distance_index_number(all_Calculated_Distance):
        minimum_distance_index_number = []
        for i in range(len(all_Calculated_Distance[0])):
            temp = []
            for j in range(len(all_Calculated_Distance)):
                temp.append(all_Calculated_Distance[j][i])
            result = np.where(temp == np.amin(temp))
            result = np.asarray(result)
            minimum_distance_index_number.append(result[0][0])
        print("\nIndex number of minimum distance between the Cluster: ")
        print(minimum_distance_index_number)
        return minimum_distance_index_number

    # This function gets the Cluster points
    def cluster_points(all_points, minimum_Distance_index_number, i):
        temp1 = []
        for j in range(len(all_points)):
            if minimum_Distance_index_number[j] == i:
                temp1.append(all_points[j])
        print("\nCluster ", i + 1, "( C", i + 1, ") Points: ")
        print(temp1)
        return temp1

    # This function Selected the New Centroid points
    def new_selected_centroid_points(selected_Centroid, all_points, minimum_Distance_index_number):
        temp = []
        new_selected_centroid_points = []
        for i in range(len(selected_Centroid)):
            temp1 = Clustering.cluster_points(all_points, minimum_Distance_index_number, i)
            temp3 = []
            for k in range(len(temp1[0])):
                sum = 0
                for l in range(len(temp1)):
                    sum += temp1[l][k]
                temp2 = sum / len(temp1)
                temp3.append(temp2)
            new_selected_centroid_points.append(temp3)
            temp.append(temp1)
        print("\nNew Selected Cluster Points: ")
        print(new_selected_centroid_points)
        return new_selected_centroid_points
