import cStringIO as StringIO
import unittest
import sys
import random

import nose.tools as test
from unittest2.test.support import captured_stdout

import solution


cases = []
case0_in = """
4 3
1 2 3 4
1 2 3
13 29 71
"""

case0_out = """
13 754 2769 1508
"""
cases.append((case0_in, case0_out))


class TestSolutionModule(object):
    def __init__(self):
        global cases
        self.cases = cases
        solution.input = raw_input

    def main_with_input(self, case_input):
        case_input = StringIO.StringIO(case_input)
        sys.stdin = case_input
        with captured_stdout() as result:
            solution.main()
        sys.stdin = sys.__stdin__
        result = result.getvalue().strip()
        self.print_format(result, 'ACTUAL')
        return result

    def check_case(self, case_input, expected):

        actual = self.main_with_input(case_input)
        try:
            test.assert_equal(actual.split("\n"), expected.split("\n"))
            test.assert_equal(actual, expected)
        except:
            self.print_format(expected, 'EXPECTED')
            raise

    def test_cases(self):
        for (_in, _out) in self.cases:
            yield self.check_case, _in.strip(), _out.strip()

    @test.timed(5)
    def test_performance(self):
        n = lambda: random.randint(1, 10 ** 1)
        m = lambda: random.randint(1, 10 ** 1)
        b = lambda: [random.randint(1, n) for _ in range(n)]
        a = lambda: [random.randint(1, 10 ** 5) for _ in range(m)]
        c = lambda: [random.randint(1, 10 ** 5) for _ in range(m)]

        line_format = lambda args: ' '.join(map(str, args))
        input_format = lambda *args: '\n'.join(args)

        n, m = n(), m()
        a, b, c = a(), b(), c()
        test_input = input_format(line_format([n, m]), line_format(b),
                                  line_format(a), line_format(c))
        print test_input
        test.assert_is_not_none(self.main_with_input(test_input))

    @staticmethod
    def print_format(text, tag='', width=70):
        if tag == 'ACTUAL':
            print '\n'
        print '{:><{}}'.format(tag, width)
        print text
        print '{:<>{}}'.format(tag, width)


class TestSolutionUnit(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()