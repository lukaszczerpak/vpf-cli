from akamaiopen.cloudlets.CloudletRule import CloudletRule


class ForwardSettings:
    def __init__(self, origin_id=None, percent=None):
        self.origin_id = origin_id
        self.percent = percent

    def to_json(self):
        return {
            "originId": self.origin_id,
            "percent": int(self.percent)
        }


class PhasedReleaseRule(CloudletRule):

    def __init__(self):
        super().__init__()
        self.forward_settings = None

    @staticmethod
    def match_type():
        return "cdMatchRule"

    def to_json(self):
        return {**super().to_json(), **{
            "forwardSettings": self.forward_settings.to_json(),
        }}
