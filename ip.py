import requests

# URL
url = "https://ispip.clang.cn/all_cn_cidr.txt"

# 获取数据
response = requests.get(url)

# 检查响应状态码
if response.status_code == 200:
    # 准备数据
    converted_data = ["payload:"]
    converted_data += ['  - IP-CIDR,' + line for line in response.text.splitlines()]

    # 使用with语句写入文件
    with open('Chinaip.txt', 'w') as f:
        f.write('\n'.join(converted_data))

else:
    # 处理错误，例如引发异常或打印错误消息
    print("获取数据失败。")
