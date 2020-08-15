import requests


class Http_request:

    def http_request(self,url,method,param=None):
        if method.upper() == 'GET':
            try:
                response = requests.get(url,param)
                return response.json()
            except Exception as e:
                print('get请求出错：{0}'.format(e))
        else:
            try:
                response = requests.post(url,param)
                return response.json()
            except Exception as e:
                print('get请求出错：{0}'.format(e))


# if __name__ == '__main__':
#     url = 'https://pagead2.googlesyndication.com/getconfig/sodar?sv=200&tid=gda&tv=r20200805&st=env'
#     url2 = 'https://pagead2.googlesyndication.com/getconfig/sodar'
#     param = {'sv':200,'tid':'gda','tv':'r20200805','st':'env'}
#     url1 = 'https://www.toutiao.com/api/pc/feed/?max_behot_time=1596965841&category=__all__&utm_source=toutiao&widen=1&tadrequire=true&as=A1F5EF23C0F12BA&cp=5F30B1C2BBCA9E1&_signature=_02B4Z6wo00101QZIm3gAAIBASwZJIVl.kA0GTZ.AAB6ks0T71FkT94ea2BTshcTvtdKOwpSrWx-w9NMZZZrNkETXtGc6K1o7ygU3DqMlsiG384kfEJWIWQZsu0gD0gdcgMA9GhQ95Lb.LI4716'
#     http = Http_request()
#     response = http.http_request(url,method='get')
#     print(response.json().keys())
#     response1 = http.http_request(url1, method='get')
#     print(response1.json().keys())
#     response2 = http.http_request(url2,param=param, method='get')
#     print(response2.json().keys())