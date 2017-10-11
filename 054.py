class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # boundary case
        if len(matrix) == 0:
            return []
        # init
        current_position = [0, 0]
        current_velocity = [0, 1]

        # define turn right:
        # [0, 1] => [1, 0] => [0, -1] => [-1, 0]
        def turnRight(originalVelocity):
            if str(originalVelocity) == "[0, 1]":
                return [1, 0]
            if str(originalVelocity) == "[1, 0]":
                return [0, -1]
            if str(originalVelocity) == "[0, -1]":
                return [-1, 0]
            if str(originalVelocity) == "[-1, 0]":
                return [0, 1]

        ret = []
        ret.append(matrix[current_position[0]][current_position[1]])
        matrix[current_position[0]][current_position[1]] = None
        while True:
            # try walking in the original direction
            next_position = [current_position[0] + current_velocity[0], current_position[1] + current_velocity[1]]
            try:
                assert matrix[next_position[0]][next_position[1]] != None
                ret.append(matrix[next_position[0]][next_position[1]])
                current_position = next_position
                matrix[current_position[0]][current_position[1]] = None
            except:
                # need to turn right
                current_velocity = turnRight(current_velocity)
                next_position = [current_position[0] + current_velocity[0], current_position[1] + current_velocity[1]]
                try:
                    assert matrix[next_position[0]][next_position[1]] != None
                    ret.append(matrix[next_position[0]][next_position[1]])
                    current_position = next_position
                    matrix[current_position[0]][current_position[1]] = None
                except:
                    # cannot even turn right
                    break
        return ret
