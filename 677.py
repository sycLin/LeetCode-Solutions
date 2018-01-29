class Node(object):
    def __init__(self):
        pass
    
class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mapping = {}
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.mapping[key] = val
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        ret = 0
        for k, v in self.mapping.items():
            if k.startswith(prefix):
                ret += v
        return ret
        
"""
# Try method #2 if having spare time (a Trie method)
"apple" => 100
"application" => 123
"apricot" => 200

           {'a', ['p'], -1}
              /
      {'p', ['p', 'r'], -1}
           /              \
    {'p', ['l'], -1}        {'r', [], -1} <= apricot
        /
    {'l', ['e', 'i'], -1}
      /              \
  {'e', [], -1}      {'i', [], -1} <= application
"""

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)