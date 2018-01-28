class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # method: use stack
        # time: O(n)
        ret = [0 for i in range(len(temperatures))]
        stack = [] # {push: append(), pop: pop(), top: [-1]}
        
        for i, t in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][1] < t:
                index, temp = stack.pop()
                ret[index] = i - index
            stack.append((i, t))
        return ret
        