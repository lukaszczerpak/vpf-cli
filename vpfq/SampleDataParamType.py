import click
import ast


class SampleDataParamType(click.ParamType):
    name = "sample-data"

    def convert(self, value, param, ctx):
        try:
            tuples = ast.literal_eval(value)
            unzipped = list(zip(*tuples))
            return [list(unzipped[0]), list(unzipped[1])]
        except:
            self.fail(f"{value!r} is not a valid list of (x,y) tuples", param, ctx)


SAMPLE_DATA = SampleDataParamType()
