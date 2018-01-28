class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        
        # steps
        stepsInBetween = [A[i+1] - A[i] if i < (len(A) - 1) else None for i, n in enumerate(A)]
        stepsInBetween.pop()
        
        print "stepsInBetween:", stepsInBetween
        
        # cluster the steps
        cluster = []
        current, current_count = stepsInBetween[0], 1
        for i in range(1, len(stepsInBetween)):
            if stepsInBetween[i] == current:
                current_count += 1
            else:
                cluster.append(current_count)
                current, current_count = stepsInBetween[i], 1
        cluster.append(current_count)
        
        print "cluster:", cluster
    
        # each cluster should be larger than 3
        ret = 0
        for cNum in cluster:
            # ret += (cNum - 1) if cNum >= 2 else 0
            ret += (cNum * (cNum - 1) / 2) if cNum >= 2 else 0
        return ret
    """
    cluster being 2 => 1 == 1         == (1 + 1) * 1 / 2
    cluster being 3 => 3 == 2 + 1     == (1 + 2) * 2 / 2
    cluster being 4 => 4 == 3 + 2 + 1 == (1 + 3) * 3 / 2
    """