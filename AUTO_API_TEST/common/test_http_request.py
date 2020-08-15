import unittest

from ddt import ddt, data, unpack

from AUTO_API_TEST.common import http_request
from AUTO_API_TEST.common.do_excel import Do_excel
from AUTO_API_TEST.common.http_request import Http_request

# test_data = [{'url':'https://pagead2.googlesyndication.com/getconfig/sodar',
#               'param':{'sv':200,'tid':'gda','tv':'r20200805','st':'env'},
#               'method':'get',
#               'expected':'sodar2'},
#              {'url': 'https://pagead2.googlesyndication.com/getconfig/sodar',
#               'param': {'sv': 200, 'tid': 'gda', 'tv': 'r20200805', 'st': 'env'},
#               'method': 'get',
#               'expected': 'sodar2'}
#              ]
from AUTO_API_TEST.common.pro_path import testdata_path

test_data = Do_excel(testdata_path,'test_data').do_excel()

@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        self.t = Do_excel(testdata_path,'test_data')

    @data(*test_data)
    @unpack
    def test_api(self,case_id,url,param,method,expected,row):
        print('正在执行第{}条用例'.format(case_id))
        print('请求的地址是：{}'.format(url))
        print('发起请求的参数是：{}'.format(param))
        http = Http_request()
        try:
            if isinstance(param,str):
                param = eval(param)
                response = http.http_request(url, param=param, method=method)
                self.assertEqual(expected, response['injector_basename'])
            else:
                response = http.http_request(url,param=param,method=method)
                self.assertEqual(expected,response['injector_basename'])
            Test_result = 'PASS'
        except Exception as e:
            print('断言出错了，错误是{}'.format(e))
            Test_result = 'FAIL'
            raise e
        else:
            print('执行成功，执行结果是{}'.format(response.keys()))
        finally:
            self.t.write(row, 7, Test_result)
            if response:
                self.t.write(row,6,str(response['injector_basename']))
            else:
                self.t.write(row, 6, 'no response')

# if __name__ == '__main__':
#     unittest.main()