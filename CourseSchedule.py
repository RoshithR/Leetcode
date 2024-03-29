# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
#
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.


def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    from collections import defaultdict
    courseDict = defaultdict(list)

    for relation in prerequisites:
        nextCourse, prevCourse = relation[0], relation[1]
        courseDict[prevCourse].append(nextCourse)

    path = [False] * numCourses
    for currCourse in range(numCourses):
        if isCyclic(currCourse, courseDict, path):
            return False
    return True


def isCyclic(currCourse, courseDict, path):
    """
    backtracking method to check that no cycle would be formed starting from currCourse
    """
    if path[currCourse]:
        # come across a previously visited node, i.e. detect the cycle
        return True

    # before backtracking, mark the node in the path
    path[currCourse] = True

    # backtracking
    ret = False
    for child in courseDict[currCourse]:
        ret = isCyclic(child, courseDict, path)
        if ret: break

    # after backtracking, remove the node from the path
    path[currCourse] = False
    return ret


numCourses = 2
prerequisites = [[1,0]]
print(canFinish(numCourses, prerequisites))