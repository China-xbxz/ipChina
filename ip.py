import requests
import output_files

# URL
url = "https://ispip.clang.cn/all_cn_cidr.txt"

# 获取数据
response = requests.get(url)

# 检查响应状态码
if response.status_code == 200:
    # 转换数据
    converted_data = ['- IP-CIDR, ' + line for line in response.text.splitlines()]

    # 使用output_files写入文件
    with output_files.write('Chinaip.txt') as f:
        f.writelines(converted_data)

    # 打印成功消息
    print("成功将转换后的数据保存到Chinaip.txt文件中。")
