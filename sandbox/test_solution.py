# coding=utf-8
import sys
from cStringIO import StringIO

import pytest

import solution


cases = []
case0_in = """
7
1 3 9 8 2 7 5
"""

case0_out = """
1 3 2 5 9 7 8
1 2 3 5 9 7 8
1 2 3 5 7 8 9
"""
cases.append((case0_in, case0_out))


@pytest.fixture(params=cases)
def case(request):
    return request.param


# noinspection PyShadowingNames
def test_cases(case, capsys):
    actual, expected = map(str.lstrip, case)
    sys.stdin = StringIO(actual)
    solution.main()
    out, _ = capsys.readouterr()
    sys.stdin = sys.__stdin__

    assert out == expected
