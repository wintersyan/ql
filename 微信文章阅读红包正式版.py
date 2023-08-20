'''
活动入口,微信打开：https://entry-1318684421.cos.ap-nanjing.myqcloud.com/cos_b.html?openId=oiDdr54Nefy0xxsTr6SGgdSzpWj0
打开活动入口，抓包的任意接口cookies中的authtoken参数,填到脚本最下方的,脚本最下方的，脚本最下方的mycklist中，把xxxx替换成你的authtoken参数
填写格式
单账户mycklist=[{'authtoken': 'xxxx'}]
多账户mycklist=[{'authtoken': 'xxxx'},{'authtoken': 'xxxx'},{'authtoken': 'xxxx'},]
定时运行每两小时一次 0 0 1-12/2 * * *
达到标准，自动提现

运行脚本要先安装python的pycryptodome依赖
依赖安装失败，试试先安装一下linux依赖
python3-dev
libc-dev
gcc
'''

import requests
import re
import random
import time
from urllib.parse import urlparse, parse_qs
from Crypto.Cipher import AES
import base64
def aes_encrypt(text):
    bs = AES.block_size
    pad = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
    cipher = AES.new(b'5e4332761103722eb20bb1ad53907c6e', AES.MODE_ECB)
    data = cipher.encrypt(pad(text).encode())
    t = str(base64.b64encode(data), encoding='utf-8')
    return t
class WXYD:
    def __init__(self, cg):
        self.homeHost = self.get_readHome()
        self.headers = {
            'Host': self.homeHost,
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue',
            'token': '',
            'Accept': '*/*',
            'Referer': f'http://{self.homeHost}/app/main?openId=oiDdr54Nefy0xxsTr6SGgdSzpWj0',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh',
            'Cookie': f'authtoken={cg["authtoken"]}; snapshot=0',
        }

    def get_readHome(self):
        h = {
            'Host': 'sss.mvvv.fun',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue',
            'Accept': '*/*',
            'Origin': 'https://entry-1318684421.cos.ap-nanjing.myqcloud.com',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://entry-1318684421.cos.ap-nanjing.myqcloud.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh',
        }
        u = 'https://sss.mvvv.fun/app/enter/read_home'
        r = requests.get(u, headers=h)
        print(r.text)
        rj = r.json()
        if rj.get('code') == 0:
            homeurl = rj['data']['location']
            hosturl = re.findall('//(.*?)/', homeurl)[0]
            print('get home url is', homeurl)
            print('-' * 50)
            return hosturl
        else:
            print('get home page err')
            return "http://5x034gb8z4.qqaas.fun"

    def myPickInfo(self):
        print('-'*30)
        u = f'http://{self.homeHost}/app/user/myPickInfo'
        r = requests.get(u, headers=self.headers)
        rj = r.json()
        print(r.text)
        data = rj.get('data')
        goldNow=data.get('goldNow')
        if goldNow >0:
            txu='http://mhxbn1se67.qqaas.fun/app/user/pickAuto'
            p='{"moneyPick":goldNow}'.replace('goldNow',str(goldNow))
            payload=aes_encrypt(p)
            self.headers.update({'Content-Type': 'application/json'})
            r = requests.post(txu, headers=self.headers,json=payload)
            print('提现结果',r.text)
        else:
            print('没有达到提现标准')

    def myInfo(self):
        requests.get(self.headers.get('Referer'), headers=self.headers)#增加拉人头成功率，顺便模拟访问主页
        u = f'http://{self.homeHost}/app/user/myInfo'
        r = requests.get(u, headers=self.headers)
        rj = r.json()
        print(r.text)
        data = rj.get('data')
        msg = rj.get('success')
        nameNick = data.get('nameNick')
        self.goldNow = data.get('goldNow')
        completeTodayCount = data.get('completeTodayCount')
        completeTodayGold = data.get('completeTodayGold')
        readable = data.get('readable')
        remainSec = data.get('remainSec')
        print(
            f'当前用户{nameNick}，当前积分:{self.goldNow}，今日已读{completeTodayCount}篇文章，获得了{completeTodayGold}积分，用户状态:{readable},提示信息:{msg}。')
        if remainSec == 0:
            print('当前是读文章的状态')
        else:
            ms = int(remainSec / 60)
            print('当前不是是读文章的状态,距离下次阅读还有', ms,'分钟')
            return False
        print('-' * 50)
        return True

    def getkey(self):
        u = f'http://{self.homeHost}/app/read/get'
        r = requests.get(u, headers=self.headers)
        rj = r.json()
        print(r.text)
        location = rj.get('data').get('location')
        p = parse_qs(urlparse(location).query)
        hn = urlparse(location)
        uk = p.get('u')[0]
        print('get key is ', uk)
        print('-' * 50)
        u2 = f'https://sss.mvvv.fun/app/task/doRead?u={uk}&type=1'
        h = {
            'Host': 'sss.mvvv.fun',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept': '*/*',
            'Origin': f'https://{hn}',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': f'https://{hn}/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh',
        }
        r2 = requests.get(u2, headers=h)
        print(r2.text)
        rj2 = r2.json()
        if rj2.get('code') == 0:
            taskKey = rj2.get('data').get('taskKey')
            bizCode = rj2.get('data').get('bizCode')
            if bizCode == 20:
                print('The article is being updated. Please try again later.')
                return False
            if taskKey == None:
                print()
                return False
            print('this task key is ', taskKey)
            print('-' * 50)
            ts = random.randint(10, 15)
            print(f'本次模拟读{ts}秒')
            print('-' * 50)
            time.sleep(ts)
            return taskKey, uk, h
        else:
            print('get taskKey err')
            print('-' * 50)
            return False

    def do_read(self):
        info = self.getkey()
        if info == False:
            print('read wenzhang err')
            return False
        self.taskKey = info[0]
        while True:
            u = f'https://sss.mvvv.fun/app/task/doRead?u={info[1]}&type=1&key={self.taskKey}'
            r = requests.get(u, headers=info[2])
            print(r.text)
            rj = r.json()
            if rj.get('code') != 0:
                break
            detail = rj.get('data').get('detail')
            print(f'上次一篇阅读结果：{detail}')
            self.taskKey = rj.get('data').get('taskKey')
            print('this task key is ', self.taskKey)
            if self.taskKey==None:
                break
            print('-' * 50)
            ts = random.randint(20, 50)
            print(f'本次模拟读{ts}秒')

            time.sleep(ts)
        print('read over')

    def run(self):
        if self.myInfo():
            time.sleep(10)
            self.do_read()
            time.sleep(2)
            self.myInfo()
        time.sleep(2)
        self.myPickInfo()

if __name__ == '__main__':
    # 下边填authtoken，把xxxx替换成你的authtoken参数
    mycklist=[
        {'authtoken': 'xxxx'}
    ]
    for i in mycklist:
        api = WXYD(i)
        api.run()
        time.sleep(5)
