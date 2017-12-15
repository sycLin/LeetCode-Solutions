class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        three_counter = 0
        five_counter = 0
        for i in range(n):
            three_counter += 1
            five_counter += 1
            three_counter -= 3 if three_counter == 3 else 0
            five_counter -= 5 if five_counter == 5 else 0
            if three_counter == 0 and five_counter == 0:
                ret.append('FizzBuzz')
            elif three_counter == 0:
                ret.append('Fizz')
            elif five_counter == 0:
                ret.append('Buzz')
            else:
                ret.append(str(i+1))
        return ret
        