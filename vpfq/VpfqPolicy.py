from akamaiopen.cloudlets.VisitorPrioritizationRule import VisitorPrioritizationRule
from akamaiopen.cloudlets.matches.CookieMatch import CookieMatch
from akamaiopen.cloudlets.matches.Match import MatchOperator
from akamaiopen.cloudlets.matches.PathMatch import PathMatch
from vpfq.model.LinearInterpolation import LinearInterpolation


class VpfqPolicy:

    def __init__(self, path, cookie_name):
        self.__path = path
        self.__cookie_name = cookie_name

    def __create_fq_rule(self, segment, probability, exact_segment_match=True):
        vpr = VisitorPrioritizationRule()
        vpr.name = f'segment:{segment}'
        vpr.pass_through_percent = probability
        vpr.matches.extend([
            PathMatch(match_value=self.__path),
            CookieMatch(match_value=f'{self.__cookie_name}=*~{segment}~*', match_operator=MatchOperator.CONTAINS)
            if exact_segment_match else
            CookieMatch(match_value=f'{self.__cookie_name}=*', match_operator=MatchOperator.CONTAINS)
        ])
        return vpr

    def __create_default_rule(self):
        vpr = VisitorPrioritizationRule()
        vpr.name = 'default'
        vpr.pass_through_percent = 0
        vpr.matches.append(PathMatch(match_value='/*', match_operator=MatchOperator.CONTAINS))
        return vpr

    def generate_json(self, ix, iy, segments, base_prob, description="automatically generated"):
        values = LinearInterpolation.generate_values(ix, iy, segments, base_prob)

        match_rules = []
        for s, p in values:
            match_rules.append(self.__create_fq_rule(s, p, not s == segments).to_json())
        match_rules.append(self.__create_default_rule().to_json())

        policy = {
            "description": description,
            "matchRuleFormat": "1.0",
            "matchRules": match_rules
        }

        return policy
