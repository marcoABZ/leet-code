class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        result = [i[:] for i in img]

        for i in range(len(img)):
            for j in range(len(img[0])):
                pos = [img[p[0]][p[1]] for p in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i,j), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)] if p[0] >= 0 and p[0]< len(img) and p[1] >= 0 and p[1] < len(img[0])]
                result[i][j] = sum(pos) / len(pos)
        
        return result