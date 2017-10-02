class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = [int(c) for c in a]
        b = [int(c) for c in b]
        indexA = len(a) - 1
        indexB = len(b) - 1
        carry = 0
        ret = []
        while indexA >= 0 or indexB >= 0:
            tmp = 0
            if indexA >= 0:
                tmp += a[indexA]
                indexA -= 1
            if indexB >= 0:
                tmp += b[indexB]
                indexB -= 1
            tmp += carry
            ret.insert(0, tmp % 2)
            carry = tmp / 2
        while carry > 0:
            ret.insert(0, carry % 2)
            carry /= 2
        return "".join([str(n) for n in ret])
