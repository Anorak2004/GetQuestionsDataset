import requests
from config import *
from login import Login

class Fetch:
    def __init__(self, login):
        self.login = login
        self.info_url = Config.INFO_URL

    def test_connection(self):
        # 测试与网站连接是否正常
        response = self.login.session.get(self.login.index_url, headers=self.login.headers)
        print("连接测试响应状态:", response.status_code)
        if response.status_code == 200:
            print("连接成功")
        else:
            print("连接失败，状态码：", response.status_code)
        return response

    def fetch_data(self):
        number = 1
        for knowsid in range(177, 180):
            url = self.info_url.format(knowsid, number)
            # 打印当前 cookies
            print(f"请求前 Cookies: {self.login.session.cookies.get_dict()}")

            # 发送请求
            response = self.login.session.get(url, headers=self.login.headers)

            print(f'请求网址: {url}')
            print("请求返回状态码:", response.status_code)

            if response.status_code == 200:
                print(f'获取数据成功：knowsid={knowsid}')
                print(response.content.decode('utf-8'))  # 输出获取的数据
            elif response.status_code == 302:
                print("被重定向到登录页面，请检查登录状态")
            else:
                print(f'获取数据失败：knowsid={knowsid}，状态码：{response.status_code}')
