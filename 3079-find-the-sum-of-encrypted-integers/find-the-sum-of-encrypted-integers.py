class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def encrypt(n):
            largest = 0
            digits = 0

            while n:
                digits += 1
                largest = max(largest, n % 10)
                n //= 10
            
            cypher = 0
            for i in range(digits):
                cypher *= 10
                cypher += largest
            
            return cypher
        
        return sum([encrypt(n) for n in nums])
        