class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        merged = s.replace("-", "")
        i, j = 0, len(merged) % k if len(merged) % k != 0 else k
        parts = []
        print(merged)
        while j <= len(merged):
            parts.append(merged[i:j])
            i = j
            j += k
        
        return "-".join(parts).upper()