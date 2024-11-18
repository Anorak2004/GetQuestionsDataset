# E:\WorkSpace\js\GetQuestionsDataset\controller.py
from fetch_data import Fetch
from process_info import QuestionProcessor
import json


class Controller:
    def __init__(self, login):
        """
        初始化 Controller 类，负责协调各个模块之间的关系。

        :param login: 登录模块实例
        """
        self.fetch = Fetch(login)
        self.processor = None

    def process_loop(self,knowsid):
        number = 1
        initial_info = controller.get_and_process_data(knowsid=knowsid, number=number)
        initial_info['number'] = number
        all_info = [initial_info]
        while number<int(initial_info['total_number']):
            number += 1
            try:
                next_info = controller.get_and_process_data(knowsid=knowsid, number=number)
                next_info['number'] = number
                all_info.append(next_info)
            except Exception as e:
                print(e)
                break
        self.save_to_file(all_info,'questions_of_knowsid{}.json'.format(knowsid))



    def get_and_process_data(self, knowsid, number):
        """
        获取数据并处理。

        :param knowsid: 题库 ID
        :param number: 题号
        :return: 处理后的结果字典
        """
        # 获取数据
        info = self.fetch.fetch_data(knowsid, number)

        # 处理数据
        if info:
            self.processor = QuestionProcessor(info)
            return self.processor.process()
        return None

    def save_to_file(self, data, filename):
        """
        将处理后的数据保存到文件。

        :param data: 处理后的数据字典
        :param filename: 保存的文件名
        """
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"数据已保存到 {filename}")


# 示例用法
if __name__ == "__main__":
    from login import Login

    # 填写用户名和密码
    username = 'Anorak'  # 替换为你的用户名
    password = '123456'  # 替换为你的密码

    # 创建登录实例并执行登录
    login = Login(username, password)
    login_response = login.login()

    # 如果登录成功，获取并处理数据
    if login_response.status_code == 200:
        controller = Controller(login)

        # # 获取并处理数据
        # result = controller.get_and_process_data(knowsid=10, number=1)
        #
        # # 如果成功处理数据，则保存到文件
        # if result:
        #     controller.save_to_file(result, 'question_data.json')

        controller.process_loop(10)
    else:
        print("登录失败，无法继续获取数据")
