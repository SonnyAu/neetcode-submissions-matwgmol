class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq = {i:[] for i in range(numCourses)}
        for p, c in prerequisites:
            preq[c].append(p)
        visit = set()
        def dfs(c):
            if c in visit:
                return False
            if preq[c] == []:
                return True
            
            visit.add(c)
            for i in preq[c]:
                if not dfs(i):
                    return False
            visit.remove(c)
            preq[c] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        