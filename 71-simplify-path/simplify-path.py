class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        st = []

        for part in [p for p in path.split("/") if p]:
            if part == '.':
                continue
            elif part == '..':
                if st:
                    st.pop()
            else:
                st.append(part)
        
        return "/" + "/".join(st)