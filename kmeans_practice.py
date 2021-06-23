import random, math
import numpy as np

class kmeans:
    def __init__(self,k):
        self.k = k

    def euclidean(self, pairs):
        return math.sqrt(sum([math.pow(x[0]-x[1],2) for x in pairs]))


    def initialize_centroids(self, dataset):
        centroids = []
        for i in range(self.k):
            index = random.randint(0, len(dataset)-1)
            centroids.append(dataset[index])
        return centroids

    def find_nearest_centroid(self, centroids, datapoint, dist_func ):
        distances = list(map(dist_func,[list(zip(datapoint,centroid)) for centroid in centroids]))
        min_distance = min(distances)
        centroid = distances.index(min_distance)
        return min_distance, centroid


    def update_centroids(self, assignments, dataset, centroids):
        updated_centroids = [centroid for centroid in centroids]
        for cluster, datapoints in assignments.items():
            for datapoint in datapoints:
                updated_centroids[cluster] = map(lambda x:x[0]+x[1], list(zip(updated_centroids[cluster], dataset[datapoint])))
            updated_centroids[cluster] = list(map(lambda x: float(x)/float(len(datapoints)+1),updated_centroids[cluster]))
        return updated_centroids



    def do_kmeans(self, dataset, dist_func, iter=5):
        centroids = self.initialize_centroids(dataset)
        distances = {i:0 for i in range(len(dataset))}
        for i in range(iter):
            assignments={i:[] for i in range(self.k)}
            for i in range(len(dataset)):
                distance, centroid = self.find_nearest_centroid(centroids, dataset[i], dist_func)
                distances[i] = distance
                assignments[centroid].append(i)
            print('centroids', centroids)
            centroids = self.update_centroids(assignments, dataset, centroids)
            sse = pow(sum([dist for dist in distances.values()]),2)
            print('sse',sse)
        sse = pow(sum([dist for dist in distances.values()]), 2)
        print("final sse:", sse)
        return sse, assignments


def load_dataset(N,k):
    dataset = np.random.rand(N,k)
    return dataset

def main(N,k,clusters,dist_metric):
    dataset = load_dataset(N,k)
    kms = kmeans(clusters)
    if dist_metric == 'euclidean':
        dist_func = kms.euclidean
    sse, assignments = kms.do_kmeans(dataset, dist_func)
    print(assignments)




if __name__=="__main__":
    main(1000,3,3,'euclidean')