# 导入所需的库
import requests

# URL
url = "https://ispip.clang.cn/all_cn_cidr.txt"

# 使用requests库从URL获取数据
response = requests.get(url)

# 通过检查响应状态码确认请求成功
if response.status_code == 200:
    # 将请求的数据转换为文本
    data = response.text.splitlines()

    # 开启新的文件并以写入模式打开
    with open('Chinaip.txt', 'w') as f:
        #通过遍历数据列表，我们可以通过使用字符串方法添加' - IP-CIDR,'前缀
        for line in data:
            f.write('- IP-CIDR,' + line + 'n')
