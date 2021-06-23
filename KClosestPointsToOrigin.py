# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

# #This is O(NlogN) solution it is possible to achieve O(N) with quickselect.
# def kClosest(points, k):
#     points.sort(key=lambda p: p[0]**2+p[1]**2)
#     return points[:k]
#
#
#
# points = [[1,3],[-2,2]]
# k = 1
# print(kClosest(points,k))


# Solving for run time complexity O(N)

def kClosest(points,k):
    distances = {str(x):x[0]**2+x[1]**2 for x in points}

    def partition(low, high):
        pivot_index = (low+high)//2
        pivot_dist = distances[str(points[pivot_index])]
        points[pivot_index], points[high] = points[high], points[pivot_index]
        indx = 0
        for i in range(len(points)):
            if distances[str(points[i])]<pivot_dist:
                points[indx], points[i] = points[i], points[indx]
                indx+=1
        points[indx], points[high] = points[high], points[indx]
        return indx



    def select(low, high, ksmallest):
        if low==high:
            return
        pivot = partition(low,high)
        if ksmallest==pivot:
            return
        elif ksmallest<pivot:
            select(low, pivot-1, ksmallest)
        else:
            select(pivot+1,high, ksmallest)
    n = len(points)
    select(0,n-1,k)
    return points[:k]

points = [[1,3],[-2,2]]
k = 1


points = [[3,3],[5,-1],[-2,4]]
k = 2
print(kClosest(points,k))