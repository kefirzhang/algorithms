class TrieNode:
    def __init__(self):
        self.isWord = False
        self.next = [None for _ in range(26)]


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root

        n = len(word)
        for i in range(n):
            if node.next[ord(word[i]) - ord('a')] is None:
                node.next[ord(word[i]) - ord('a')] = TrieNode()
            node = node.next[ord(word[i]) - ord('a')]
        node.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        n = len(word)
        for i in range(n):
            if node.next[ord(word[i]) - ord('a')] is None:
                return False
            node = node.next[ord(word[i]) - ord('a')]
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        n = len(prefix)
        for i in range(n):
            if node.next[ord(prefix[i]) - ord('a')] is None:
                return False
            node = node.next[ord(prefix[i]) - ord('a')]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('word')
param_2 = obj.search('wordc')
param_3 = obj.startsWith('awo')
print(param_2, param_3)
