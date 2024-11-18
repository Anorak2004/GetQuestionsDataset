import requests
import random
from config import Config

class Login:
    def __init__(self, username, password):
        self.login_url = Config.LOGIN_URL
        self.index_url = Config.INDEX_URL
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.headers = Config.HEADERS

    def generate_userhash(self):
        """生成两个不同的 userhash 值"""
        userhash1 = str(random.random())
        userhash2 = str(random.random())
        return userhash1, userhash2

    def login(self):
        # 随机生成 userhash
        userhash1, userhash2 = self.generate_userhash()

        # 构建 POST 请求的 payload
        self.payload = {
            'args[username]': str(self.username),
            'args[userpassword]': str(self.password),
            'userlogin': '1',
            'userhash1': userhash1,  # 使用第一个 userhash
            'userhash2': userhash2,  # 使用第二个 userhash
        }

        # 发送登录请求
        response = self.session.post(self.login_url, data=self.payload, headers=self.headers)

        # 检查响应状态码
        if response.status_code == 200:
            print("登录成功")
        else:
            print("登录失败，状态码：", response.status_code)

        return response
