import abc
from enum import Enum

from akamaiopen.cloudlets.matches.Match import Match, MatchOperator


class CheckIPsType(Enum):
    CONNECTING = 'CONNECTING_IP'
    XFF = 'XFF_HEADERS'
    BOTH = 'CONNECTING_IP XFF_HEADERS'


class GeoMatch(Match, metaclass=abc.ABCMeta):
    def __init__(self, match_value=None, match_operator: MatchOperator = MatchOperator.EQUALS, negate=False, case_sensitive=False, checkips=CheckIPsType.BOTH):
        super().__init__(match_value, match_operator, negate, case_sensitive)
        self.checkips = checkips

    def to_json(self):
        o = super().to_json()
        o['checkIPs'] = self.checkips.value
        return o

    def from_csv(self, value):
        super().from_csv(value)

        # region_info = record['region'].split(';', 1)
        # region = region_info[0]
        # checkips = CheckIPsType.BOTH if len(region_info) == 1 else CheckIPsType(region_info[1])

        return self


class CountryCodeMatch(GeoMatch):
    @staticmethod
    def match_type():
        return 'countrycode'


class RegionCodeMatch(GeoMatch):
    @staticmethod
    def match_type():
        return 'regioncode'
