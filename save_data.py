import json


class SaveData:
    def __init__(self, data, file_path):
        """
        初始化 SaveData 类。

        :param data: 要保存的数据，通常是字典类型
        :param file_path: 文件保存路径
        """
        self.data = data
        self.file_path = file_path

    def save(self):
        """
        将数据保存为 JSON 文件。
        """
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)
        print(f"数据已成功保存到 {self.file_path}")
