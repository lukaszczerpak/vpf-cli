from akamaiopen.cloudlets.matches.Match import Match, MatchOperator


class URLRegexMatch(Match):
    def __init__(self, match_value=None, match_operator: MatchOperator = MatchOperator.EQUALS, negate=False, case_sensitive=False):
        super().__init__(match_value, match_operator, negate, case_sensitive)

    @staticmethod
    def match_type():
        return 'regex'

"""
    {
        "caseSensitive": false,
        "matchOperator": "equals",
        "matchType": "regex",
        "matchValue": "^([^\\?]*)([^\\w|^\\?]|^)(techfit-collection)([^\\w|^\\?]|$)([^\\?]*)$",
        "negate": false
    }
"""