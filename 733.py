class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        #
        # let's try using the Python set
        #
        #
        # init
        #
        processedSet = set()
        processQueue = []
        nRows, nCols = len(image), len(image[0])
        oldColor = image[sr][sc]
        #
        # process first pixel
        #
        processQueue.append((sr, sc))
        #
        while len(processQueue) > 0:
            r, c = processQueue.pop()
            image[r][c] = newColor
            processedSet.add((r, c))
            if r - 1 >= 0 and (r-1, c) not in processedSet and image[r-1][c] == oldColor:
                processQueue.append((r-1, c))
            if r + 1 < nRows and (r+1, c) not in processedSet and image[r+1][c] == oldColor:
                processQueue.append((r+1, c))
            if c - 1 >= 0 and (r, c-1) not in processedSet and image[r][c-1] == oldColor:
                processQueue.append((r, c-1))
            if c + 1 < nCols and (r, c+1) not in processedSet and image[r][c+1] == oldColor:
                processQueue.append((r, c+1))
        return image