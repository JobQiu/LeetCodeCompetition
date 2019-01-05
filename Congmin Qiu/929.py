class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """

        nameDomainPairs = [email.split("@") for email in emails]
        keys = [name.split("+")[0].replace(".","") + domain for (name, domain) in nameDomainPairs]
        return len(set(keys))
