class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        formated = set()
        for email in emails:
            local, domain = email.split("@")

            plus = None
            for i, c in enumerate(local):
                if c == '+':
                    plus = i
                    break
            local = local if plus is None else local[:plus]

            formated.add(local.replace(".", "") + "@" + domain)
        
        return len(formated)