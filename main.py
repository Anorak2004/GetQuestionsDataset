from process_info import QuestionProcessor
from login import Login
from fetch_data import Fetch
from controller import *


def main():
    # 填写用户名和密码
    username = 'test'  # 替换为你的用户名
    password = '135246'  # 替换为你的密码

    # 创建登录实例并执行登录
    login = Login(username, password)
    login_response = login.login()

    if login_response.status_code == 200:
        controller = Controller(login)
        
        for i in range(251,300):
            controller.process_loop(i)

if __name__ == "__main__":
    main()
