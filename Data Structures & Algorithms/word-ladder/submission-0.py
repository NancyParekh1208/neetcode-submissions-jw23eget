class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0

        if beginWord == endWord:
            return 0
        
        m ,n = len(wordList), len(wordList[0])

        adj = [[] for _ in range(m)] # create adj list of size m * m
        mp = {}
        for i in range(m):
            mp[wordList[i]] = i # store the word list and map with index

        for i in range(m):
            for j in range(i + 1, m): # compare it with every other word
                count = 0
                for k in range(n):
                    if wordList[i][k] != wordList[j][k]:
                        count += 1
                if count == 1:
                    adj[i].append(j)
                    adj[j].append(i)
        
        q, res = deque(), 1
        visit = set()
        # Find all the words that differ by one letter compared to the beginword. And it to the queue
        for i in range(n):
            for c in range(97, 123):
                if chr(c) == beginWord[i]:
                    continue
                word = beginWord[:i] + chr(c) + beginWord[i+1:] # replacing one letter
                if word in mp and mp[word] not in visit:
                    q.append(mp[word])
                    visit.add(mp[word])
        
        while q:
            res += 1
            for i in range(len(q)):
                node = q.popleft()
                if wordList[node] == endWord:
                    return res
                for nei in adj[node]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)
        
        return 0
        
        
        