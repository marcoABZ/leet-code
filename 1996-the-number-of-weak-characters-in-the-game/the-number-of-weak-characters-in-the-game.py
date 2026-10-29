class Solution:
    def numberOfWeakCharacters(self, properties: list[list[int]]) -> int:
        properties.sort(reverse=True)
        mxDef = -1
        weak = 0
        cAtt, cDef = properties[0]

        for p in properties[1:]:
            if p[0] != cAtt:
                mxDef = max(mxDef, cDef)
                cAtt, cDef = p
            
            if p[1] < mxDef:
                weak += 1

        return weak