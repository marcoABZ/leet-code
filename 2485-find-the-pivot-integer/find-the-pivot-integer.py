class Solution:
    def pivotInteger(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            mid = l + (r-l) // 2

            left = (1 + mid) * (mid) / 2
            right = (mid + n) * (n - mid + 1) / 2

            if left == right:
                return mid
            elif left > right:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1

        