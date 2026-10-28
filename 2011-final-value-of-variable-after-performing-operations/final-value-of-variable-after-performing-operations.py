class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        x = 0

        for op in operations:
            if op[:2] == "--" or op[-2:] == "--":
                x -= 1
            else:
                x += 1
        
        return x