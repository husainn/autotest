import unittest
from HTMLTestRunner_PY3.HTMLTestRunner_PY3 import HTMLTestRunner

from AUTO_API_TEST.common.pro_path import result_path
from AUTO_API_TEST.common.test_http_request import TestHttpRequest

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))

with open(result_path,'wb') as stream:
    runner = HTMLTestRunner(stream,title='hugetest')
    runner.run(suite)