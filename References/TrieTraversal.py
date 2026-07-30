class TreeNode:
    def __init__(self, val=0, left=TreeNode, right=TreeNode):
        self.val = val
        self.left = left
        self.right = right

class TrieNode:
    def __init__(self, val=0, next:list[TrieNode]=[]):
        self.val = val
        self.next = next

class TrieTraversal:
    def __init__(self):
        self.b_tree = TreeNode(val = 10,
                             left=TreeNode(val=5,
                                           left=TreeNode(val=3,
                                                         left=TreeNode(val=1),
                                                         right=TreeNode(val=4)),
                                            right=TreeNode(val=8,
                                                         left=TreeNode(val=7),
                                                         right=TreeNode(val=9))),
                             right=TreeNode(val=20,
                                            left=TreeNode(val=15,
                                                          left=TreeNode(val=13),
                                                          right=TreeNode(val=16)),
                                            right=TreeNode(val=25,
                                                           left=TreeNode(val=23),
                                                           right=TreeNode(val=27))))
    """
    The above should look like; (B-Tree)
              10
        5             20
     3     8      15     25
    1 4   7 9   13 16   23 27
    """
    self.bp_trie = TrieNode(val='C',
                            next=[TrieNode(val='A',
                                           next=[TrieNode(val='T'), TrieNode(val='R')]),
                                  TrieNode(val='O',
                                           next=[TrieNode(val='P'), TrieNode(val='G')])])
    
    def dfs_height(head:TreeNode) -> int:
        res = 1
        if head.left:
            res += dfs_height(head.left)
        if head.right:
            res += dfs_height(head.right)
        if head == None:
            return 0
        return res