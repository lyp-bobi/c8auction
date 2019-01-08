#coding=utf-8
import time
import urllib.request
import io
import gzip
from c8parser import c8Parser
from mailsender import sendmail


if __name__ == '__main__':
    previousName=""
    previousPrice=""
    i=1
    print("task started")
    while (True):
        try:
            print("checked at "+time.strftime('%D-%H:%M:%S',time.localtime(time.time())))
            url = "https://www.mercari.com/jp/search/?sort_order=created_desc&keyword=%E5%B0%BA%E5%85%AB&category_root=&brand_name=&brand_id=&size_group=&price_min=&price_max="
            headers = {
                'authority': 'www.mercari.com',
                'method': 'GET',
                'path': '/jp/search/?sort_order=created_desc&keyword=%E5%B0%BA%E5%85%AB&category_root=&brand_name=&brand_id=&size_group=&price_min=&price_max=',
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-CN,zh;q=0.9',
                'cache-control': 'max-age=0',
                'cookie': '_gcl_au=1.1.992364451.1544699125; _ga=GA1.2.2103937252.1544699127; _gid=GA1.2.1986750610.1544699127; _gat_UA-50190241-1=1',
                'referer': 'https://wx.qq.com/',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
            }
            req = urllib.request.Request(url=url, headers=headers)
            response = urllib.request.urlopen(req)
            content = response.read()
            encoding = response.getheader('Content-Encoding')
            if encoding == 'gzip':
                buf = io.BytesIO(content)
                gf = gzip.GzipFile(fileobj=buf)
                content = gf.read()
            c8 = c8Parser()
            c8.feed(content.decode('utf-8'))

            if c8.firstc8name != previousName:
                if i == 1:
                    # sendmail("Auto auction alert task launched")
                    pass
                else:
                    sendmail(c8.firstc8name + " appears, with price " + str(c8.firstc8price))
                previousName = c8.firstc8name
            i += 1
            time.sleep(300)
        except:
            sendmail("c8auction crashed, will start after 50 minutes")
            time.sleep(3000)


