import requests

payload = {
    'args[username]': 'Anorak',
    'args[userpassword]': '123456'
}

def fetch_data(url):
    # 发送 HTTP GET 请求
    response = requests.post(url,data=payload)
    # print(response.content)
    # 确保请求成功
    # if response.status_code == 200:
    #     # 使用 BeautifulSoup 解析 HTML
    #     soup = BeautifulSoup(response.text, 'html.parser')
    #     # 假设我们要提取所有的 <a> 标签的 href 属性
    #     for link in soup.find_all('a'):
    #         print(link.get('href'))
    # else:
    #     print('Failed to retrieve data')

    # 使用函数


login_url = 'http://ks.xlyd.com.cn/index.php?user-app-login'
index_url = 'http://ks.xlyd.com.cn/index.php?core'
fetch_data(login_url)
response = requests.get(index_url)
print(response.content)

class Login:




    def __init__(self, username, password):
        self.LOGIN_URL = 'http://ks.xlyd.com.cn/index.php?user-app-login'
        self.INDEX_URL = 'http://ks.xlyd.com.cn/index.php?core'
        self.username = username
        self.password = password
        self.payload = {
            'args[username]': str(self.username),
            'args[password]': str(self.password)
        }
        self.session = requests.Session()

