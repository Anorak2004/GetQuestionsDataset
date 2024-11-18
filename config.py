class Config(object):
    LOGIN_URL = 'http://ks.xlyd.com.cn/index.php?user-app-login'
    INDEX_URL = 'http://ks.xlyd.com.cn/index.php?core'
    INFO_URL = 'http://ks.xlyd.com.cn/index.php?exam-app-lesson-ajax-questions&knowsid={}&number={}'
    HEADERS = {
        'Referer': 'http://ks.xlyd.com.cn/index.php?exam-app-lesson',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
    }