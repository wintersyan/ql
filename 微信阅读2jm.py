'''
活动入口,微信打开：http://2478987.n.6bidyd0un0.cloud/?p=2478987
打开活动入口，抓包的任意接口cookies中的gfsessionid参数,填到脚本下方的,脚本下方的,脚本下方的 CKList配置中,把xxxx替换成你的gfsessionid参数
单账户 CKList=[{'gfsessionid': 'xxxx'}]
多账户CKList=[{'gfsessionid': 'xxxx'},{'gfsessionid': 'xxxx'},{'gfsessionid': 'xxxx'},]
定时运行每小时一次 0 0 * * * *
达到标准自动提现
'''

import time #line:1
import hashlib #line:2
import requests #line:3
import random #line:4
def sha_256 (O000OO00OO000OO0O ):#line:5
    OO0O00O0OO0OOO0O0 =hashlib .sha256 ()#line:6
    OO0O00O0OO0OOO0O0 .update (O000OO00OO000OO0O .encode ())#line:7
    OO0OO0000O000OO00 =OO0O00O0OO0OOO0O0 .hexdigest ()#line:8
    return OO0OO0000O000OO00 #line:9
class HHYD ():#line:10
    def __init__ (OO000OOOOOO000OOO ,OO000OOO0O0OO0OO0 ):#line:11
        OO000OOOOOO000OOO .headers ={'Host':'2478987.jilixczlz.ix47965in5.cloud','Connection':'keep-alive','Accept':'application/json, text/plain, */*','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh','Cookie':f'gfsessionid={OO000OOO0O0OO0OO0["gfsessionid"]}',}#line:20
        OO000OOOOOO000OOO .sec =requests .session ()#line:21
        OO000OOOOOO000OOO .sec .headers =OO000OOOOOO000OOO .headers #line:22
    def user_info (O0OO0000O0OOO0O0O ):#line:23
        OO0OO00O0O0O0O000 =int (time .time ())#line:24
        O00OOO0O000000O00 =f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={OO0OO00O0O0O0O000}'#line:25
        O0O0OOOOO0O00OO0O =sha_256 (O00OOO0O000000O00 )#line:26
        O0OO0000O0OOO0O0O .sec .get ('http://2478987.wgma.kwuzc9uie925t.cloud/page?p=2478987')#line:27
        OOOO000OOO000O0O0 =f'http://2478987.jilixczlz.ix47965in5.cloud/user/info?time={OO0OO00O0O0O0O000}&sign={O0O0OOOOO0O00OO0O}'#line:28
        OOOO000O00OOO0O0O =''#line:29
        try :#line:30
            OOOO000O00OOO0O0O =O0OO0000O0OOO0O0O .sec .get (OOOO000OOO000O0O0 )#line:31
            O0O00OO000OOO0OO0 =OOOO000O00OOO0O0O .json ()#line:32
            if O0O00OO000OOO0OO0 .get ('code')==0 :#line:33
                print (f'用户UID:{O0O00OO000OOO0OO0.get("data").get("uid")}')#line:34
                return True #line:35
            else :#line:36
                print (f'获取用户信息失败，账号异常')#line:37
                return False #line:38
        except :#line:39
            print (OOOO000O00OOO0O0O .text )#line:40
            print (f'获取用户信息失败,gfsessionid无效，请检测gfsessionid是否正确')#line:41
            return False #line:42
    def msg (OOOOOO0O0OO0OOOO0 ):#line:43
        O0000000000OO0000 =''#line:44
        try :#line:45
            O0OOO00OOO0OO00OO =int (time .time ())#line:46
            O00OOOO000OO000O0 =f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={O0OOO00OOO0OO00OO}'#line:47
            O0O0OOOO000O0O0O0 =sha_256 (O00OOOO000OO000O0 )#line:48
            OO00O0OO0OOO0000O =f'http://2478987.jilixczlz.ix47965in5.cloud/user/msg?time={O0OOO00OOO0OO00OO}&sign={O0O0OOOO000O0O0O0}'#line:49
            O0000000000OO0000 =OOOOOO0O0OO0OOOO0 .sec .get (OO00O0OO0OOO0000O )#line:50
            O00000O0O0O0OO000 =O0000000000OO0000 .json ()#line:51
            print (f'系统公告:{O00000O0O0O0OO000.get("data").get("msg")}')#line:52
        except :#line:53
            print (O0000000000OO0000 .text )#line:54
            return False #line:55
    def read_info (OO0OO0O00O0000OOO ):#line:56
        O00OOO0OOO0OO00O0 =''#line:57
        try :#line:58
            O000OOO0OOOO00OOO =int (time .time ())#line:59
            OO00O000O0OO000O0 =f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={O000OOO0OOOO00OOO}'#line:60
            OO0OOO0OOO00OOOOO =sha_256 (OO00O000O0OO000O0 )#line:61
            OO00000O00O000OOO =f'http://2478987.jilixczlz.ix47965in5.cloud/read/info?time={O000OOO0OOOO00OOO}&sign={OO0OOO0OOO00OOOOO}'#line:62
            O00OOO0OOO0OO00O0 =OO0OO0O00O0000OOO .sec .get (OO00000O00O000OOO )#line:63
            OOOOO00000OO0O000 =O00OOO0OOO0OO00O0 .json ()#line:64
            OO0OO0O00O0000OOO .remain =OOOOO00000OO0O000 .get ("data").get ("remain")#line:65
            print (f'今日已经阅读了{OOOOO00000OO0O000.get("data").get("read")}篇文章，总金币{OOOOO00000OO0O000.get("data").get("gold")}，剩余{OO0OO0O00O0000OOO.remain}')#line:66
        except :#line:67
            print (O00OOO0OOO0OO00O0 .text )#line:68
            return False #line:69
    def read (O00O00OOOO00O0OOO ):#line:70
        print ('阅读开始')#line:71
        while True :#line:72
            print ('-'*50 )#line:73
            O000OO0OOOOO0OO00 =int (time .time ())#line:74
            O0O0O000O0O00OO0O =f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={O000OO0OOOOO0OO00}'#line:75
            OO0OOO00OOO00OO00 =sha_256 (O0O0O000O0O00OO0O )#line:76
            OO0OOO00O0000000O =f'http://2478987.jilixczlz.ix47965in5.cloud/read/task?time={O000OO0OOOOO0OO00}&sign={OO0OOO00OOO00OO00}'#line:77
            O0000O0O0OOOOO000 =O00O00OOOO00O0OOO .sec .get (OO0OOO00O0000000O )#line:78
            print (O0000O0O0OOOOO000 .text )#line:79
            O0OO00OO0OOOOO000 =O0000O0O0OOOOO000 .json ()#line:80
            if O0OO00OO0OOOOO000 .get ('code')==0 :#line:81
                OOO0O000O0OO00O0O =O0OO00OO0OOOOO000 .get ('data').get ('link')#line:82
                if OOO0O000O0OO00O0O :#line:83
                    print ('获取到阅读链接成功')#line:84
                    O0O00OO0OO0OOOOO0 =random .randint (7 ,30 )#line:85
                    print ('本次模拟阅读',O0O00OO0OO0OOOOO0 ,'秒')#line:86
                    time .sleep (O0O00OO0OO0OOOOO0 )#line:87
                else :#line:88
                    print ('获取到阅读链接失败')#line:89
                    return False #line:90
            else :#line:91
                return False #line:92
            O00O00OOOO00O0OOO .msg ()#line:94
            O000OO0OOOOO0OO00 =int (time .time ())#line:95
            OO0OO0OOOO00O0OOO =O00O00OOOO00O0OOO .sec .headers .copy ()#line:96
            OO0OO0OOOO00O0OOO .update ({'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8','Origin':'http://2478987.jilixczlz.ix47965in5.cloud'})#line:97
            O0O0O000O0O00OO0O =f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={O000OO0OOOOO0OO00}'#line:98
            OO0OOO00OOO00OO00 =sha_256 (O0O0O000O0O00OO0O )#line:99
            OO0OO000OO0OO00OO =f'time={O000OO0OOOOO0OO00}&sign={OO0OOO00OOO00OO00}'#line:100
            OO0OOO00O0000000O =f'http://2478987.jilixczlz.ix47965in5.cloud/read/finish'#line:101
            O0000O0O0OOOOO000 =requests .post (OO0OOO00O0000000O ,headers =OO0OO0OOOO00O0OOO ,data =OO0OO000OO0OO00OO )#line:102
            print (O0000O0O0OOOOO000 .text )#line:103
            O0OO00OO0OOOOO000 =O0000O0O0OOOOO000 .json ()#line:104
            if O0OO00OO0OOOOO000 .get ('code')==0 :#line:105
                if O0OO00OO0OOOOO000 .get ('data').get ('check')==False :#line:106
                    O0OOOOOO0O0OOO00O =O0OO00OO0OOOOO000 .get ('data').get ('gain')#line:107
                    O00O00OOOO00O0OOO .remain =O0OO00OO0OOOOO000 .get ("data").get ("remain")#line:108
                    print (f"阅读文章成功获得{O0OOOOOO0O0OOO00O}金币")#line:109
                    print (f'当前已经阅读了{O0OO00OO0OOOOO000.get("data").get("read")}篇文章，总金币{O0OO00OO0OOOOO000.get("data").get("gold")}，剩余{O00O00OOOO00O0OOO.remain}')#line:111
                else :#line:112
                    print ("遇到检测")#line:113
                    break #line:114
            else :#line:115
                return False #line:116
            time .sleep (2 )#line:117
            print ('开始本次阅读')#line:118
    def withdraw (O0O00O0OO00OO0000 ):#line:119
        if O0O00O0OO00OO0000 .remain <3000 :#line:120
            print ('没有达到提前标准')#line:121
            return False #line:122
        OOOO0OO0O0OO0O00O =int (time .time ())#line:123
        OO0OO0OOO00O000O0 =f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={OOOO0OO0O0OO0O00O}'#line:124
        O00000O0OO0O00O00 =sha_256 (OO0OO0OOO00O000O0 )#line:125
        O0O0000O0OO00000O =f'http://2478987.84.8agakd6cqn.cloud/withdraw/wechat?time={OOOO0OO0O0OO0O00O}&sign={O00000O0OO0O00O00}'#line:126
        OOOOO00O0OO000OO0 =O0O00O0OO00OO0000 .sec .get (O0O0000O0OO00000O ,headers =O0O00O0OO00OO0000 .headers )#line:127
        print ('提现结果',OOOOO00O0OO000OO0 .text )#line:128
    def run (OOOOOOO0OO00OO0O0 ):#line:129
        OOOOOOO0OO00OO0O0 .user_info ()#line:130
        OOOOOOO0OO00OO0O0 .msg ()#line:131
        OOOOOOO0OO00OO0O0 .read_info ()#line:132
        OOOOOOO0OO00OO0O0 .read ()#line:133
        time .sleep (5 )#line:134
        OOOOOOO0OO00OO0O0 .withdraw ()#line:135
if __name__ =='__main__':#line:136
    CKList =[{'name':'备注','gfsessionid':'xxxx'}]#line:139
    for i in CKList :#line:140
        api =HHYD (i )#line:141
        api .run ()