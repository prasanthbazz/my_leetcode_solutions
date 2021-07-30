'''
#677
https://leetcode.com/problems/map-sum-pairs/
'''
class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = TrieNode()
        self.map = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        if key in self.map:
            temp = val
            val = val - self.map[key]
            self.map[key] = temp
        else:
            self.map[key] = val
        node = self.head
        for l in key:
            if l not in node.children:
                node.children[l] = TrieNode()
            node = node.children[l]
            node.mapSum += val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.head
        for l in prefix:
            if l not in node.children:
                return 0
            node = node.children[l]
        return node.mapSum

class TrieNode():
    
    def __init__(self):
        self.children = {}
        self.mapSum = 0
# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)