from abc import abstractmethod, ABCMeta


class CloudletRule(object, metaclass=ABCMeta):

    def __init__(self):
        self.name = ''
        self.match_url = None
        self.matches = []

    @staticmethod
    @abstractmethod
    def match_type():
        raise NotImplemented()

    def to_json(self):
        o = {
            "type": self.match_type(),
            "name": self.name
        }

        if self.match_url:
            o['matchURL'] = self.match_url
        else:
            o['matches'] = list(map(lambda m: m.to_json(), self.matches))

        return o
