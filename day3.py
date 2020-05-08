# 136. Single Number
# https://leetcode.com/problems/single-number/

from typing import List


class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result ^= n
        return result


class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums)) - sum(nums)
        

if __name__ == '__main__':
    s1 = Solution1()
    result = s1.singleNumber([2, 2, 1])
    assert result == 1
    result = s1.singleNumber([4, 4, 2, 1, 1])
    assert result == 2
    print('OK')

    s2 = Solution2()
    result = s2.singleNumber([2, 2, 1])
    assert result == 1
    result = s2.singleNumber([4, 4, 2, 1, 1])
    assert result == 2
    print('OK')