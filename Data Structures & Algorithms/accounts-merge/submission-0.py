class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        email_to_name = {}
        def find(email):
            if parent[email] == email:
                return email

            parent[email] = find(parent[email])
            return parent[email]
        # Initialize every email
        for account in accounts:
            name = account[0]

            for email in account[1:]:
                if email not in parent:
                    parent[email] = email

                email_to_name[email] = name

        # Union emails belonging to the same account
        for account in accounts:
            first_email = account[1]

            for email in account[2:]:
                root_first = find(first_email)
                root_email = find(email)

                if root_first != root_email:
                    parent[root_email] = root_first

        # Group emails by their root
        groups = defaultdict(list)

        for email in parent:
            root = find(email)
            groups[root].append(email)

        # Build final answer
        result = []

        for root, emails in groups.items():
            emails.sort()

            name = email_to_name[root]

            result.append([name] + emails)

        return result

        