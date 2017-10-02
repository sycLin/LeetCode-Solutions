class Solution(object):
	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		# This is the O(N^2) version
		# => TLE
		"""
		ret = float("-INF")
		for start in range(len(nums)):
			s = nums[start]
			if s > ret:
				ret = s
			for end in range(start+1, len(nums)):
				s += nums[end]
				if s > ret:
					ret = s
		return ret
		"""
		# This is the O(N) version
		# => ACCEPT
		"""
		ret = float("-INF")
		tmpSum = float("-INF")
		for number in nums:
			if tmpSum + number > number:
				tmpSum = tmpSum + number
			else:
				tmpSum = number
			if tmpSum > ret:
				ret = tmpSum
		return ret
		"""
		# This is the O(NlogN) version
		# => also ACCEPT
		# terminal condition
		if len(nums) == 1:
			return nums[0]
		if len(nums) == 2:
			return max(nums[0], nums[1], nums[0] + nums[1])
		# optimal sub-solution
		left = nums[:len(nums)/2]
		right = nums[len(nums)/2:]
		leftAnswer = self.maxSubArray(left)
		rightAnswer = self.maxSubArray(right)
		# cross-over solution
		subLeftSum, subLeftIndex = nums[len(nums)/2-1], len(nums)/2 - 2
		subRightSum, subRightIndex = nums[len(nums)/2], len(nums)/2 + 1
		subLeftOptimal, subRightOptimal = subLeftSum, subRightSum
		while subLeftIndex >= 0:
			subLeftSum += nums[subLeftIndex]
			subLeftIndex -= 1
			if subLeftSum > subLeftOptimal:
				subLeftOptimal = subLeftSum
		while subRightIndex < len(nums):
			subRightSum += nums[subRightIndex]
			subRightIndex += 1
			if subRightSum > subRightOptimal:
				subRightOptimal = subRightSum
		# return the ultimate answer
		return max(leftAnswer, rightAnswer, subLeftOptimal + subRightOptimal)
