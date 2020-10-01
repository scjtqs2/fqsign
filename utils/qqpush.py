#coding:utf-8
import urllib
import http.cookiejar
import json
class Qqpush:
    pushurl='https://wx.scjtqs.com/qq/push/singlePush'
    def push(self,qq,data):
        url = self.pushurl
        postdata = urllib.parse.urlencode({
            'cqq': qq,
            'content': data
        }).encode('utf-8')
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0",
            'X-Requested-With': 'XMLHttpRequest',
        }
        req = urllib.request.Request(url, postdata, header)
        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        r = opener.open(req)
        response = r.read().decode('utf-8')
        jsonret=json.loads(response)
        return jsonret