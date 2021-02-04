import click
import pytest
from vpfq.SampleDataParamType import SampleDataParamType


@pytest.mark.parametrize(
    ("type", "value", "expect"),
    [
        (SampleDataParamType(), "(0,1), (2,3)", [[0, 2], [1, 3]]),
        (SampleDataParamType(), "(0,1), (2,3), (4.5,0.01)", [[0, 2, 4.5], [1, 3, 0.01]]),
        (SampleDataParamType(), "(0,  1), (2,3), (4.5,0.01)", [[0, 2, 4.5], [1, 3, 0.01]]),
        (SampleDataParamType(), "0,  1), (2,3), (4.5,0.01)", click.exceptions.BadParameter),
    ],
)
def test_convert(type, value, expect):
    assert type.convert(value, None, None) == expect
