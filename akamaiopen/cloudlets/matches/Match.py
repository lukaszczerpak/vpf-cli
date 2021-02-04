import re
from abc import abstractmethod, ABCMeta
from enum import Enum


class MatchOperator(Enum):
    EQUALS = 'equals'
    CONTAINS = 'contains'


class Match(object, metaclass=ABCMeta):

    def __init__(self, match_value=None, match_operator: MatchOperator = MatchOperator.EQUALS, negate=False, case_sensitive=False):
        self.case_sensitive = case_sensitive
        self.negate = negate
        self.match_operator = match_operator
        self.match_value = match_value

    @staticmethod
    @abstractmethod
    def match_type():
        raise NotImplemented()

    def to_json(self):
        return {
            "matchValue": self.match_value,
            "matchOperator": self.match_operator.value,
            "negate": self.negate,
            "caseSensitive": self.case_sensitive,
            "matchType": self.match_type()
        }

    def from_csv(self, value):
        if not value:
            raise ValueError("Value cannot be null!")

        self.match_value = value

        if self.match_value[0] == '!':
            self.negate = True
            self.match_value = self.match_value[1:]

        if self.match_value[0] == ':':
            self.case_sensitive = True
            self.match_value = self.match_value[1:]

        self.match_operator = MatchOperator.CONTAINS if re.search(r"(^|[^\\])\*", self.match_value) in self.match_value else MatchOperator.EQUALS

        return self
