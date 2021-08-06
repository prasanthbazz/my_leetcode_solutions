'''
#429
https://leetcode.com/problems/n-ary-tree-level-order-traversal/
'''
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        res = []
        while(queue):
            res.append([x.val for x in queue])
            nxt = []
            for node in queue:
                nxt += node.children
            queue = nxt
        return res