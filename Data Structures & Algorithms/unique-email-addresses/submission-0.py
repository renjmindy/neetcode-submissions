class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        ans = set()

        for email in emails:
            local = email.split('@')[0]
            local = ''.join(local.split('.'))
            local = local.split('+')[0]

            domain = email.split('@')[1]

            ans.add(local + '@' + domain)

        return len(ans)