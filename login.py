import requests
from config import *


class Login:
    def __init__(self, username, password):
        self.login_url = Config.LOGIN_URL
        self.index_url = Config.INDEX_URL
        self.username = username
        self.password = password
        self.payload = {
            'args[username]': str(self.username),
            'args[password]': str(self.password)
        }
        self.session = requests.Session()
        self.headers = Config.HEADERS

    def login(self):
        # 发送登录请求
        response = self.session.post(self.login_url, data=self.payload, headers=self.headers)

        # 输出cookies确认是否保存
        print("登录后 Cookies:", self.session.cookies.get_dict())

        if response.status_code == 200:
            print("登录成功")
        else:
            print("登录失败，状态码：", response.status_code)
        return response

    def get_session_cookies(self):
        import urllib.parse

        # 获取并解码 cookies
        exam_currentuser_cookie = self.session.cookies.get('exam_currentuser')
        decoded_cookie = urllib.parse.unquote(exam_currentuser_cookie)
        print(f"解码后的 exam_currentuser: {decoded_cookie}")

        return self.session.cookies.get_dict()

