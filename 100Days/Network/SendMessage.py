import urllib.parse
import http.client
import json


def main():
    host = "106.ihuyi.com"
    sms_send_url = '/webservice/sms.php?method=Submit'
    params = urllib.parse.urlencode({
        'account':'xxxxxxxxx',                                      # APIID
        'password':'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',              # APIKEY
        'content':"您的验证码是：741313。请不要把验证码泄露给其他人。", # 短信内容要使用报备过的模板
        'mobile':'15216805515',
        'format':'json'
    })
    headers = {
        'Content-type':'application/x-www-form-urlencoded',
        'Accept':'text/plain'
    }
    conn = http.client.HTTPConnection(host, port=80,timeout=30)
    conn.request('POST', sms_send_url,params, headers)
    response = conn.getresponse()
    response_str = response.read()
    jsonstr = response_str.decode('utf-8')
    print(json.loads(jsonstr))
    conn.close()


if __name__ == "__main__":
    main()
