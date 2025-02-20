from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create a mapping for each course to a list of its prerequisites.
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # 'cycle' is used to track courses in the current DFS recursion stack.
        # If we encounter a course that is already in this set, a cycle exists.
        cycle = set()
        
        def dfs(crs):
            # If the current course is already in the cycle set, a cycle is detected.
            if crs in cycle:
                return False
            
            # If the current course has no prerequisites (empty list), it's safe to take.
            # This acts as our base case.
            if preMap[crs] == []:
                return True
            
            # Add the current course to the cycle set before exploring its prerequisites.
            cycle.add(crs)
            
            # Recursively perform DFS on each prerequisite of the current course.
            for nei in preMap[crs]:
                if not dfs(nei):
                    return False  # If any prerequisite leads to a cycle, return False.
            
            # Remove the course from the cycle set after processing.
            cycle.remove(crs)
            # Mark the course as processed by clearing its prerequisites list.
            # This is a form of memoization: once processed, the course doesn't need to be re-checked.
            preMap[crs] = []
            return True
        
        # Try to perform DFS for every course.
        # If any course cannot be completed due to a cycle, return False.
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        # If all courses can be completed (i.e., no cycles detected), return True.
        return True
