class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(done,next):
            if next in done:
                return False
            done = done.copy()
            done.add(next)
            if len(done) == numCourses and len(course[next]) == 0:
                return True
            res = False
            for c in course[next]:
                res = res or dfs(done,c)
            return res
        course = [[] for _ in range(numCourses)]
        for done, req in prerequisites:
            course[done].append(req)
        for n in range(numCourses):
            if dfs(set(),n):
                return True
        return False

        