class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        n = len(accounts)
        emailIdx = {} # email -> node index
        emails = [] # set of emails of all accounts
        emailtoAcc = {} # map email index -> account holder id 

        m = 0 # node number
        for accId, a in enumerate(accounts):
            for i in range(1, len(a)):
                email = a[i] # email address
                if email in emailIdx:
                    continue
                emails.append(email)
                emailIdx[email] = m
                emailtoAcc[m] = accId
                m += 1

        adj = [[] for i in range(m)] # create adj list of nodes
        for a in accounts:
            for i in range(2, len(a)): # 0 index is the name 
                idx1 = emailIdx[a[i]]
                idx2 = emailIdx[a[i-1]]
                adj[idx1].append(idx2)
                adj[idx2].append(idx1)

        emailGroup = defaultdict(list) # index of acc -> list of emails (connected comp)

        visited = [False] * m  
        
        def dfs(node, accId):
            visited[node] = True
            emailGroup[accId].append(emails[node])
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei, accId)
        
        for i in range(m):
            if not visited[i]:
                dfs(i,emailtoAcc[i])
        
        res = []
        for accId in emailGroup:
            name = accounts[accId][0]
            res.append([name]+sorted(emailGroup[accId]))

        return res

        