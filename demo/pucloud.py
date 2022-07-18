# coding:utf-8
'''
author scjtqs@qq.com
https://pucloud.vip/ 的飞机场每日签到，多账户版，多余的账户，请于List中删除
注册即送100GB流量,充值一块即可成为会员获得2T流量,邀请返利更变态可无限白嫖,更有专属客户端加持！http://invcode.puyun.me/0Vi15Z
'''
import urllib
import http.cookiejar
import json
import utils
import logging
from utils.qqpush import Qqpush
from utils.config import Config


class pucloud:
    config = utils.config.Config.readJson()
    config_name = "pcloud"  ## 对应config配置的key
    list = config['users'][config_name] if ('users' in config and config_name in config['users']) else []
    cqq = config['qqpush']['qq'] if (
            'qqpush' in config and 'qq' in config['qqpush']) else ''  # 请到 https://wx.scjtqs.com/qq 里面开启，访问需要先登录
    token = config['qqpush']['token'] if (
            'qqpush' in config and 'token' in config['qqpush']) else ''  # 请到 https://wx.scjtqs.com/qq 里面开启，访问需要先登录

    def run(self):
        push = utils.qqpush.Qqpush()
        accounts = self.list
        for account in accounts:
            if 'email' not in account or 'passwd' not in account:
                continue
            ## 登录
            url = "https://pucloud.vip/auth/login"
            postdata = urllib.parse.urlencode({
                'email': account['email'],
                'passwd': account['passwd']
            }).encode('utf-8')
            header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"
            }
            req = urllib.request.Request(url, postdata, header)

            userCqq = account['cqq'] if ('cqq' in account) else self.cqq
            userToken = account['token'] if ('token' in account) else self.token

            # 自动记住cookie
            cj = http.cookiejar.CookieJar()
            opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
            r = opener.open(req)
            response = r.read().decode('utf-8')
            logincheck = json.loads(response)
            if logincheck['ret'] != 1:
                print('登录失败')
                ret = push.push(userCqq, userToken, '账号' + account['email'] + '签到pucloud登录失败')
                print(ret)
                continue
            print('账号' + account['email'] + '登录成功')
            ## 签到
            url = "https://pucloud.vip/user/checkin"
            postdata = urllib.parse.urlencode({}).encode('utf-8')
            header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0",
                "Content-Type": "application/json",

            }
            req = urllib.request.Request(url, postdata, header)
            opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
            r = opener.open(req)
            response = r.read().decode('utf-8')
            try:
                ret = json.loads(response)
                print(ret)
            except ValueError:
                print('签到失败')
                push.push(userCqq, userToken, '账号' + account['email'] + '签到pucloud失败 msg:' + ret['msg'])
                print(ret)
                continue
            if ret['ret'] != 1:
                print('签到失败')
                ret = push.push(userCqq, userToken, '账号' + account['email'] + '签到pucloud失败 msg:' + ret['msg'])
                print(ret)
                continue
            print(ret)
            # 登出
            url = "https://pucloud.vip/user/logout"
            header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0",
            }
            req = urllib.request.Request(url, None, header)
            opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
            r = opener.open(req)
            response = r.read().decode('utf-8')
            # print(response)
            if userCqq == '' or userToken == '':
                logging.info('账号' + account['email'] + '签到pucloud成功' + ',' + ret['msg'])
            else:
                push.push(userCqq, userToken, '账号' + account['email'] + '签到pucloud成功' + ',' + ret['msg'])
        return True


if __name__ == '__main__':
    pucloud().run()
