from GetQuestionsDataset.process_info import QuestionProcessor
from login import Login
from fetch_data import Fetch


def main():
    # 填写用户名和密码
    username = 'Anorak'  # 替换为你的用户名
    password = '123456'  # 替换为你的密码

    # 创建登录实例并执行登录
    login = Login(username, password)
    login_response = login.login()

    # 如果登录成功，获取数据
    if login_response.status_code == 200:
        fetch = Fetch(login)
        info = fetch.fetch_data(knowsid=10,number=1)  # 获取数据
        processor = QuestionProcessor(info)
        result = processor.process()
        print(result)

    else:
        print("登录失败，无法继续获取数据")


if __name__ == "__main__":
    main()
