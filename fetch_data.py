import requests
from config import Config
from login import Login


class Fetch:
    def __init__(self, login):
        """
        初始化 Fetch 类。

        :param login: 登录模块实例
        """
        self.login = login
        self.info_url = Config.INFO_URL

    def test_connection(self):
        """
        测试与网站连接是否正常
        """
        response = self.login.session.get(self.login.index_url, headers=self.login.headers)
        print("连接测试响应状态:", response.status_code)
        if response.status_code == 200:
            print("连接成功")
        else:
            print("连接失败，状态码：", response.status_code)
        return response

    def fetch_data(self, knowsid, number):
        """
        获取指定 knowsid 和 number 的数据并打印结果。

        :param knowsid: 题库 ID
        :param number: 题号
        """
        url = self.info_url.format(knowsid, number)
        # 发送请求
        response = self.login.session.get(url, headers=self.login.headers)

        if response.status_code == 200:
            print(f'获取数据成功：knowsid={knowsid}，number={number}')
            info = response.content.decode('utf-8')
            return info

        elif response.status_code == 302:
            print("被重定向到登录页面，请检查登录状态")
        else:
            print(f'获取数据失败：knowsid={knowsid}，number={number}，状态码：{response.status_code}')
