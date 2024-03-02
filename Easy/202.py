class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_next_number(num):
            next_num = 0
            while num > 0:
                digit = num % 10
                next_num += digit ** 2
                num //= 10
            return next_num

        slow = n
        fast = get_next_number(n)

        while fast != 1 and slow != fast:
            slow = get_next_number(slow)
            fast = get_next_number(get_next_number(fast))

        return fast == 1
