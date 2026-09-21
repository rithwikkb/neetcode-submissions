class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [set() for i in range(numCourses)]

        indegree = [0] * numCourses
        isprereq = [set() for i in range(numCourses)]
        # connect the prerequisite to the course
        for pre, crs in prerequisites:
            adj[pre].add(crs)
            # indegree represents the number of incoming edges(so in this case the incoming prerequisites(is there a prerequisite to this course))
            indegree[crs] += 1
        # so we start the bfs from the course which has no prerequisites beforehand(aka the first prerequisite)
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            for n in adj[node]:
                # so we add the node itself to the prereqs of the neighbor, but we also add the prereqs of the node. because if node 3 has prereq of 2 and 2 has prereq of 1 that means node 3 has prereq of 1 too.
                isprereq[n].add(node)
                isprereq[n].update(isprereq[node])
                # if indegree reaches 0 that means we can add it to the queue and continue the bfs
                # decrement indegree since we processed that node
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)
        # now we go over the queries and check if they are prereqs
        res = []
        for i, j in queries:
            if i in isprereq[j]:
                res.append(True)
            else:
                res.append(False)
        return res