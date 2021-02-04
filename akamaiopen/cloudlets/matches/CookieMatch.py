from akamaiopen.cloudlets.matches.Match import Match, MatchOperator


class CookieMatch(Match):
    def __init__(self, match_value=None, match_operator: MatchOperator = MatchOperator.EQUALS, negate=False, case_sensitive=False):
        super().__init__(match_value, match_operator, negate, case_sensitive)

    @staticmethod
    def match_type():
        return 'cookie'

    def to_json(self):
        return {
            "caseSensitive": self.case_sensitive,
            "matchOperator": self.match_operator.value,
            "matchType": self.match_type(),
            "matchValue": self.match_value,
            "negate": self.negate
        }


"""
    {
        "caseSensitive": false,
        "matchOperator": "contains",
        "matchType": "cookie",
        "matchValue": "akavpfq_test=*~1~*",
        "negate": false
    }
"""