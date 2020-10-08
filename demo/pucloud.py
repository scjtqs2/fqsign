#coding:utf-8
'''
author scjtqs@qq.com
https://pucloud.vip/ 的飞机场每日签到，多账户版，多余的账户，请于List中删除
'''
import urllib
import http.cookiejar
import json
import utils
from utils.qqpush import Qqpush
class pucloud:
    list=[
        {'email':'你的账号','passwd':'你的密码'},
    ]
    cqq = '你的qq号'  #请到 https://wx.scjtqs.com/qq 里面开启，访问需要先登录
    token = '你的token'  #请到 https://wx.scjtqs.com/qq 里面开启，访问需要先登录
    def run(self):
        push = utils.qqpush.Qqpush()
        accounts=self.list
        for account in accounts:
            ## 登录
            url = "https://pucloud.vip/auth/login"
            postdata =urllib.parse.urlencode({
                'email': account['email'],
                'passwd': account['passwd']
            }).encode('utf-8')
            header = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"
            }
            req = urllib.request.Request(url,postdata,header)
            #自动记住cookie
            cj = http.cookiejar.CookieJar()
            opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
            r = opener.open(req)
            response=r.read().decode('utf-8')
            logincheck=json.loads(response)
            if logincheck['ret']!=1 :
                print('登录失败')
                ret=push.push(self.cqq,self.token,'账号'+account['email']+'签到pucloud登录失败')
                print(ret)
                continue
            print('账号'+account['email']+'登录成功')
            ## 签到
            url = "https://pucloud.vip/user/checkin"
            postdata =urllib.parse.urlencode({}).encode('utf-8')
            header = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0",
                "Content-Type":"application/json",

            }
            req = urllib.request.Request(url,postdata,header)
            opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
            r = opener.open(req)
            response=r.read().decode('utf-8')
            try:
                ret = json.loads(response)
                print(ret)
            except ValueError:
                print('签到失败')
                push.push(self.cqq,self.token,'账号'+account['email']+'签到pucloud失败 msg:'+ret['msg'])
                print(ret)
                continue
            if ret['ret']!=1:
                print('签到失败')
                ret=push.push(self.cqq,self.token,'账号'+account['email']+'签到pucloud失败 msg:'+ret['msg'])
                print(ret)
                continue
            print(ret)
            #登出
            url = "https://pucloud.vip/user/logout"
            header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0",
            }
            req = urllib.request.Request(url, None, header)
            opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
            r = opener.open(req)
            response = r.read().decode('utf-8')
            # print(response)
            push.push(self.cqq,self.token,'账号'+account['email']+'签到pucloud成功'+','+ret['msg']+',剩余流量'+ret['traffic'])
        return True
if __name__ == '__main__':
    pucloud().run()