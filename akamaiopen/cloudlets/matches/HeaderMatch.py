from akamaiopen.cloudlets.matches.Match import Match, MatchOperator


class HeaderMatch(Match):
    def __init__(self, match_value=None, match_operator: MatchOperator = MatchOperator.EQUALS, negate=False, case_sensitive=False):
        super().__init__(match_value, match_operator, negate, case_sensitive)
        self.name = match_value.split('=')[0]
        self.value = [ match_value.split('=')[1] ]
        # TODO add support for all header type match attributes

    @staticmethod
    def match_type():
        return 'header'

    def to_json(self):
        return {
            "matchOperator": self.match_operator.value,
            # "negate": self.negate,
            # "caseSensitive": self.case_sensitive,
            "matchType": self.match_type(),
            "objectMatchValue": {
                "name": self.name,
                "options": {
                    "value": self.value,
                    "valueEscaped": True
                },
                "type": "object"
            }
        }


"""
        {
            "caseSensitive": false,
            "matchOperator": "contains",
            "matchType": "header",
            "negate": false,
            "objectMatchValue": {
                "name": "hdr3",
                "options": {
                    "value": [
                        "value1",
                        "value2*"
                    ]
                },
                "type": "object"
            }
        }
        {
            "caseSensitive": false,
            "matchOperator": "equals",
            "matchType": "header",
            "negate": false,
            "objectMatchValue": {
                "name": "hdr2",
                "options": {
                    "value": [
                        "value1",
                        "value2",
                        "abc def"
                    ],
                    "valueEscaped": true
                },
                "type": "object"
            }
        }
        {
            "caseSensitive": false,
            "matchOperator": "exists",
            "matchType": "header",
            "negate": false,
            "objectMatchValue": {
                "name": "hdr1",
                "options": {
                    "value": []
                },
                "type": "object"
            }
        }

"""