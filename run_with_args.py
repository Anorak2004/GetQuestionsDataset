from process_info import QuestionProcessor
from login import Login
from fetch_data import Fetch
from controller import *
from argparse import ArgumentParser


def main(number):
    # 填写用户名和密码
    username = 'Anorak'  # 替换为你的用户名
    password = '123456'  # 替换为你的密码

    # 创建登录实例并执行登录
    login = Login(username, password)
    login_response = login.login()

    # 如果登录成功，获取数据
    """if login_response.status_code == 200:
        fetch = Fetch(login)
        info = fetch.fetch_data(knowsid=10,number=1)  # 获取数据
        processor = QuestionProcessor(info)
        result = processor.process()
        print(result)

    else:
        print("登录失败，无法继续获取数据")
    """
    
    if login_response.status_code == 200:
        controller = Controller(login)
        controller.process_loop(number)

if __name__ == "__main__":
    parser = ArgumentParser(description="Run with custom infomation")
    parser.add_argument('number', type=int, help='The number of question knowsid')
    args = parser.parse_args()

    if not args.number:
        print("lack of necessary value")
    else:
        main(args.number)
