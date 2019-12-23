"""
对不同的请求方式进行封装
"""

import json
import requests

requests.packages.urllib3.disable_warnings()


class RunMethod:
    def post_main(self, url, data=None, headers=None):
        res = None
        if headers != None:
            res = requests.post(url=url, data=data, headers=headers, verify=False)
        else:
            res = requests.post(url=url, data=data, verify=False)
        return res.json()

    def get_main(self, url, data=None, headers=None):
        res = None
        if headers != None:
            res = requests.get(url=url, params=data, headers=headers, verify=False)
        else:
            res = requests.get(url=url, params=data, verify=False)
        return res.json()

    def run_main(self, method, url, data=None, headers=None):
        res = None
        if method == 'POST':
            res = self.post_main(url, data, headers)
        else:
            res = self.get_main(url, data, headers)
        return json.dumps(res, indent=2, sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':
    # 测试版本
    headers = {
        'ck': 'example',
        'v': '1.0.0',
        'dt': 'ios',
    }
    # url = 'http://192.168.30.77:8031/v3/login/user'
    url = 'http://xsapi.ynmfz.com/v2/user/login'
    data = {
        "userName": "zhouangou",
        "password": "111111"
    }


    run = RunMethod()
    run_test = run.run_main(method="POST", url=url, data=data)
    print(run_test)