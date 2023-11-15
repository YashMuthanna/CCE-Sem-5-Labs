import math
data = [
    [2, 10], [2, 5], [8, 4],  
    [5, 8], [7, 5], [6, 4],  
    [1, 2], [4, 9]  
]

x = [i[0] for i in data]
y = [i[1] for i in data]


def dist(center, point):
    d = 0.0
    for i in range(0, len(point)):
        d += (center[i]-point[i])**2
    return math.sqrt(d)

def assign_clusters(data, centers):
  clusters = []
  #Create empty lists in clusters to add the points to
  for i in range(k):
    clusters.append([])
  for i in range(len(data)):
    distances = []
    for j in range(len(centers)):
      distance = dist(centers[j], data[i])
      distances.append(distance)
    for x in range(len(distances)):
      if distances[x] == min(distances):
        clusters[x].append(data[i])

  for i in range(len(clusters)):
    print(f"Cluster {i+1}: ", clusters[i])
          
  return clusters

def mean_centers(clusters):
    new_centers = []
    for cluster in clusters:
        x_sum = sum(point[0] for point in cluster)
        y_sum = sum(point[1] for point in cluster)
        new_centers.append([x_sum / len(cluster), y_sum / len(cluster)])

    return new_centers


centers = [
    [2, 10],  # Initial center for Cluster 1
    [5, 8],  # Initial center for Cluster 2
    [1, 2]  # Initial center for Cluster 3
]
k = 3
print("Initial Centers: ", centers)
for i in range(10):
  print(f"Iteration {i}")
  clusters = assign_clusters(data, centers) #the function call prints the clusters as well
  #assign new centers
  new_centers = mean_centers(clusters)
  print("Updated Centers: \n", new_centers)
  if centers != new_centers:
      centers = new_centers
  else:  
    print("Convergence Point Reached!!!! \n")
    print("\n --- FINAL CLUSTERS --- \n")
    for i in range(len(clusters)):
      print(f"Cluster {i+1}: ", clusters[i])
    break