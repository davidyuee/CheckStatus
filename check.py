import urllib.request

urls = ["https://google.com", "https://github.com", "https://baidu.com"]
for url in urls:
    try:
        status = urllib.request.urlopen(url).getcode()
        print(f"{url} -> 状态码: {status} (正常)")
    except:
        print(f"{url} -> 无法访问")
