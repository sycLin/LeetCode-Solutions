class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = map(int, a[:-1].split("+"))
        b = map(int, b[:-1].split("+"))
        re = a[0] * b[0] - a[1] * b[1]
        im = a[0] * b[1] + a[1] * b[0]
        return str(re) + "+" + str(im) + "i"
        