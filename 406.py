class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # terminal condition
        if len(people) == 0:
            return []
        
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        ret = [people[0]] # push the first
        for i in range(1, len(people)):
            ret.insert(people[i][1], people[i])
        return ret