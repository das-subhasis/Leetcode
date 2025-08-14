#
# @lc app=leetcode id=2685 lang=python3
#
# [2685] Count the Number of Complete Components
#

# @lc code=start
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {i: [] for i in range(n)}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()
        count = 0

        def dfs(node, component):
            visited.add(node)
            component.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        for i in range(n):
            if i not in visited:
                component = set()
                dfs(i, component)
                
                total_edges = sum(len(adj_list[node]) for node in component) // 2
                k = len(component)
                if total_edges == (k * (k - 1)) // 2:  
                    count += 1

        return count




# @lc code=end

