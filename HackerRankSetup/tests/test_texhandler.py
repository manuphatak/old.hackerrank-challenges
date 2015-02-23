import filecmp
import os
import tempfile
import unittest
import cPickle
import mock
import nose.tools as test
import shutil
import HackerRankSetup.TexHandler as HRTH


class TestTexHandler(unittest.TestCase):
    temp_dir = None
    tex_response = cPickle.load(open('./tests/resources/tex_response.p', 'rb'))
    sample_tex = '$B_1, B_2, \cdots, B_M$'


    @classmethod
    def setUpClass(cls):
        tempfile.tempdir = './tests/.tmp/'
        cls.temp_dir = tempfile.mkdtemp()
        cls.temp_assets = cls.temp_dir + '/resources/'
        os.mkdir(cls.temp_assets)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.temp_dir):
            shutil.rmtree(cls.temp_dir)


    def setUp(self):
        patcher = mock.patch('HackerRankSetup.TexHandler.requests')
        self.addCleanup(patcher.stop)
        self.mock_requests = patcher.start()
        self.mock_requests.get.return_value = self.tex_response
        assert HRTH.requests is self.mock_requests

        self.tex = HRTH.TexHandler(assets=self.temp_assets)

    def tearDown(self):
        pass

    def test_requests_properly_mocked(self):
        test.assert_equals(self.mock_requests, HRTH.requests)

    def test_texhandler_initializes_properly(self):
        test.assert_equals(self.tex.assets, self.temp_assets)

    def test_get_returns_name_of_file(self):
        test.assert_equals(self.tex.get(self.sample_tex),
                           '931a66e3d5b402ced398785c46df78e4.png')

    def test_accurately_renders_png(self):
        actual = self.temp_assets + self.tex.get(self.sample_tex)
        expected = './tests/resources/931a66e3d5b402ced398785c46df78e4.png'
        test.assert_true(filecmp.cmp(actual, expected))


if __name__ == '__main__':
    unittest.main()