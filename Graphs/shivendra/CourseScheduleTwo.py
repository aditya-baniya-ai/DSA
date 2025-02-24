from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build a prerequisite map: for each course (key), store a list of courses
        # that must be taken before it (its prerequisites).
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # 'res' will hold the final ordering of courses.
        res = []
        # 'visited' keeps track of courses that are fully processed (no cycles found).
        # 'cycle' tracks courses currently in the recursion stack to detect cycles.
        visited, cycle = set(), set()

        def dfs(crs):
            # If the course is already in the recursion stack, a cycle is detected.
            if crs in cycle:
                return False
            # If the course has been fully processed before, we can skip it.
            if crs in visited:
                return True
            
            # Add the current course to the recursion stack.
            cycle.add(crs)
            
            # Process all prerequisites (neighbors) for this course.
            for nei in preMap[crs]:
                if not dfs(nei):
                    return False  # If a cycle is detected in any prerequisite, return False.
            
            # Remove the course from the recursion stack after processing.
            cycle.remove(crs)
            # Mark the course as fully processed.
            visited.add(crs)
            # Append the course to the result order. It is safe to take this course now.
            res.append(crs)
            return True

        # Try to process every course. If any course leads to a cycle, return an empty list.
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        # Return the final course order. Note that the ordering in 'res' may be in reverse
        # depending on the problem's expectations; adjust by reversing if needed.
        return res
