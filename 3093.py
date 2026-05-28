class Node:
    def __init__(self):
        self.child = [-1] * 26
        self.idx = -1

class Solution:
    
    def updateIndex(self,storedIdx,newIdx,wordsContainer):
        if storedIdx == -1:
            return newIdx

        oldLen = len(wordsContainer[storedIdx])
        newLen = len(wordsContainer[newIdx])

        if newLen < oldLen:
            return newIdx

        if newLen == oldLen and newIdx < storedIdx:
            return newIdx

        return storedIdx

    def stringIndices(self, wordsContainer, wordsQuery):
        trie = [Node()]  

        
        for i in range(len(wordsContainer)):
            word = wordsContainer[i][::-1]

            node = 0

           
            trie[node].idx = self.updateIndex(trie[node].idx,i,wordsContainer)

            for ch in word:
                c = ord(ch) - ord('a')

                if trie[node].child[c] == -1:
                    trie[node].child[c] = len(trie)
                    trie.append(Node())

                node = trie[node].child[c]

                trie[node].idx = self.updateIndex(trie[node].idx,i,wordsContainer)

        ans = []

        
        for query in wordsQuery:
            query = query[::-1]

            node = 0

            for ch in query:
                c = ord(ch) - ord('a')

                if trie[node].child[c] == -1:
                    break

                node = trie[node].child[c]

            ans.append(trie[node].idx)

        return ans
