import requests

# 待检查的网站列表
urls = [
    "https://google.com", 
    "https://github.com", 
    "https://baidu.com",
    "https://not_exist_website_test.com" # 测试一个不存在的地址
]

print("--- 网站状态实时监控 ---")

for url in urls:
    try:
        # timeout=5 表示如果 5 秒内没有响应就断开连接
        # allow_redirects=True 会自动跟踪重定向（如 http 自动跳到 https）
        response = requests.get(url, timeout=5, allow_redirects=True)
        
        # 状态码 200-299 之间通常表示正常
        if response.status_code == 200:
            print(f"✅ {url} -> 状态码: {response.status_code} (正常)")
        else:
            print(f"⚠️ {url} -> 状态码: {response.status_code} (响应异常)")
            
    except requests.exceptions.Timeout:
        print(f"❌ {url} -> 请求超时 (超过 5 秒)")
    except requests.exceptions.ConnectionError:
        print(f"❌ {url} -> 无法访问 (网络连接错误或域名不存在)")
    except Exception as e:
        print(f"❌ {url} -> 发生未知错误: {e}")
