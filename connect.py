import requests
import os


"""
bjtu校园网登录
要先在连接界面获取信息(fn+F12打开开发者工具获取如下信息):
url: 发送请求的地址
header: 请求的头信息
data: 请求的信息
"""

url = 'http://10.10.42.3/drcom/login?callback=dr1637137279766&DDDDD=20121257&upass=30099294&0MKKey=123456&R1=0&R3=0&R6=0&para=00&v6ip=&_=1637137262225'
header = {'Access-Control-Allow-Origin': '*',
              'Cache-Control': 'no-cache',
              'Content-Length': '527',
              'Content-Type': 'application/javascript; charset=gbk',
              'Server': 'DrcomServer1.2'}


def connect(user: str, password: str):
    data = {'callback': 'dr1637137279766',
            'DDDDD': user,
            'upass': password,
            '0MKKey': '123456',
            'R1': '0',
            'R3': '0',
            'R6': '0',
            'para': '00',
            '_': '1632549527638'}

    response = requests.post(url, data, headers=header).status_code
    print(response)


if __name__ == '__main__':
    message_path = 'connect_message.txt'

    if os.path.exists(message_path):
        with open(message_path, 'r') as f_r:
            lines = f_r.readlines()
            user = str(lines[0])
            password = str(lines[1])

        connect(user=user, password=password)
