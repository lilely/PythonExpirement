class TrieNode:
    def __init__(self, children, isWord):
        self.children = children
        self.isWord = isWord

class Solution:
    def __init__(self):
        self.trie = None

    def build(self, words):
        self.trie = TrieNode({},False)
        for word in words:
            current = self.trie
            for char in word:
                if not char in current.children:
                    current.children[char] = TrieNode({},False)
                current = current.children[char]
            current.isWord = True
        self.dumpTrie(self.trie)

    def dumpTrie(self, trieNode):
        for char in trieNode.children:
            print(char+"->")
        for char in trieNode.children:
            self.dumpTrie(trieNode.children[char])

    def findTheWord(self, current ,prefix):
        result = []
        if current.isWord == True:
            print(prefix)
            result.append(prefix) 
        for char in current.children:
            result.extend(self.findTheWord(current.children[char], prefix+char))
        return result

    def autoComplete(self, prefix):
        current = self.trie
        result = []
        for char in prefix:
            if not char in current.children:
                return []
            current = current.children[char]
        ret = self.findTheWord(current, prefix)
        result.extend(ret)
        return result
        

solution = Solution()
solution.build(["op","ot","oq","opx","oww","op123"])
result = solution.autoComplete("op")
print(result)