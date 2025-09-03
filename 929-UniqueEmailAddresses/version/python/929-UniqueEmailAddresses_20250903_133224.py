# Last updated: 03/09/2025, 13:32:24
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            name, domain = email.split('@')
            local = name.split('+')[0].replace('.', '')
            seen.add(local + '@' + domain)
        return len(seen)
        