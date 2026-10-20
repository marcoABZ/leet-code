class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        cap = 0
        apples = sum(apple)
        capacity.sort(reverse=True)

        for i, c in enumerate(capacity):
            cap += c
            if cap >= apples:
                break
        
        return i+1
