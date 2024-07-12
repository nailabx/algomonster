from typing import Set, List

class UniqueEmailAddresses:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique: Set = set()
        for  email in emails:
            name, domain = email.split("@")
            localname = name.split('+')[0].replace('.', '')
            unique.add(localname + '@' + domain)
        return len(unique)