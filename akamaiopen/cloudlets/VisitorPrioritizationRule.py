from akamaiopen.cloudlets.CloudletRule import CloudletRule


class VisitorPrioritizationRule(CloudletRule):

    def __init__(self):
        super().__init__()
        self.pass_through_percent = None

    @staticmethod
    def match_type():
        return "vpMatchRule"

    def to_json(self):
        return {**super().to_json(), **{
            "passThroughPercent": round(self.pass_through_percent, 2)
        }}

    def to_csv(self):
        return {**super().to_csv(), **{
            "result.passThroughPercent": round(self.pass_through_percent, 2)
        }}
