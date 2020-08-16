import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
sys.path.append(curPath)

from AUTO_API_TEST.common.pro_path import result_path
from AUTO_API_TEST.common.test_http_request import TestHttpRequest
import unittest
from HTMLTestRunner_PY3.HTMLTestRunner_PY3 import HTMLTestRunner

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))

if __name__ == '__main__':
    with open(result_path,'wb') as stream:
        runner = HTMLTestRunner(stream,title='hugetest')
        runner.run(suite)
        print('ok')