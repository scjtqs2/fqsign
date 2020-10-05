#coding:utf-8
import urllib
import http.cookiejar
import json
class Qqpush:
    pushurl='https://wx.scjtqs.com/qq/push/pushMsg'
    def push(self,qq,token,data):
        url = self.pushurl+"?token="+token
        post={}
        post['qq']=qq
        post['content']=[{"msgtype":"text","text":data}]
        postdata=bytes(json.dumps(post),'utf8')
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0",
            'Content-Type': 'application/json',
        }
        req = urllib.request.Request(url=url, data=postdata, headers=header)
        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        r = opener.open(req)
        response = r.read().decode('utf-8')
        jsonret=json.loads(response)
        return jsonret