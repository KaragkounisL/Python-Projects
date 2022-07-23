# Given an m x n board of characters and a list of strings words, return all words on the board.
# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once in a word.

class TreeNode:
    def __init__(self):
        self.isWord = False
        self.children = {}

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]
        cur.isWord = True

    def pruneWord(self, word) -> None:
        cur: TreeNode = self
        nodeAndChildKey: list[tuple[TreeNode, str]] = []
        for char in word:
            nodeAndChildKey.append((cur, char))
            cur = cur.children[char]
        for parentNode, childKey in reversed(nodeAndChildKey):
            targetNode = parentNode.children[childKey]
            if len(targetNode.children) == 0:
                del parentNode.children[childKey]
            else:
                return


class Solution:
    def findWords(self, board, words):
        root = TreeNode()
        for word in words:
            root.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        result, visited = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visited or board[r][c] not in node.children):
                return
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                result.add(word)
                node.isWord = False
                root.pruneWord(word)
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(result)


'''
# Solution from Leetcode Forum
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
"""
Even we use trie, TLE still could happen for Python implementation.
We should incorporate a remove function to remove the found word from the trie
Then we add numchild for each node, if the numchild==0, then it is safe to remove this entry
"""
class TrieNode:
    def __init__(self):
        self.isword = None
        self.children = {}
        self.word = None
        self.numchild = 0

    def add(self, word):
        node = self
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()                
            node.numchild += 1
            node = node.children[w]
        node.isword = True
        node.word = word
    
    def remove(self, word):
        node = self
        stack = []
        for w in word:
            stack.append([node, w])
            node = node.children.get(w)
            if not node:
                return
        # now node is the leaf node, stack.top is [its parent, and key]
        while stack:
            node, w = stack.pop()
            if node.children[w].numchild == 0:
                del node.children[w]
            node.numchild -= 1                

"""
Backtracking with prune
Note: once a word is found, then the word should be remove from the trie which
can reduce the complexity of trie search. Thus, the TLE problem can be solved.
"""
class Solution:
    def findWords(self, board, words):
        def dfs(r, c, node, visited):            
            if not node: return            
            if len(result) == len(words):  return            
            
            if node.isword:
                result.add(node.word)
                # update trie for time saving
                root.remove(node.word)
            
            for dr, dc in DIRECTIONS:
                r_new = r + dr
                c_new = c + dc
                if not (0 <= r_new < ROW and 0 <= c_new < COL) or (r_new, c_new) in visited:
                    continue

                visited.add((r_new,c_new))
                dfs(r_new, c_new, node.children.get(board[r_new][c_new]), visited)
                visited.remove((r_new,c_new))                                        
        
        result = set()
        ROW, COL = len(board), len(board[0])

        root = TrieNode()
        for w in words:
            root.add(w)

        for r in range(ROW):
            for c in range(COL):
                ch = board[r][c]
                dfs(r, c, root.children.get(ch), set([(r,c)]))
        return list(result)
'''
