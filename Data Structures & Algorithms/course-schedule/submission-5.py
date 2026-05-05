class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True
        def dfs(done,next):
            if next in done:
                return False
            done = done.copy()
            done.add(next)
            for c in course[next]:
                if not dfs(done,c):
                    return False
            return True
        course = [[] for _ in range(numCourses)]
        for done, req in prerequisites:
            course[done].append(req)
        for n in range(numCourses):
            if not dfs(set(),n):
                return False
        return True

        