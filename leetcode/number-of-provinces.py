class Solution:

    def findCircleNum(self, isConnected) -> int:
        def dfs(v, visited):
            visited.add(v)
            for i in range(len(isConnected[0])):
                if isConnected[v][i]==1 and i not in visited:
                    dfs(i, visited)

        count = 0
        visited = set()
        for i in range(len(isConnected)):
            if i not in visited:
                count+=1
                dfs(i,visited)
        return count
