# 抢票脚本
import requests
import time

# 设置请求头部信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Referer': 'https://www.example.com/',
    'Origin': 'https://www.example.com/',
    'Host': 'www.example.com',
    'X-Requested-With': 'XMLHttpRequest'
}

# 设置请求参数
params = {
    'train_date': '2022-01-01',
    'from_station': '北京',
    'to_station': '上海',
    'purpose_codes': 'ADULT'
}

# 设置请求URL
url = 'https://www.example.com/query'

# 循环查询余票信息
while True:
    try:
        # 发送GET请求
        r = requests.get(url, params=params, headers=headers)

        # 解析JSON响应
        data = r.json()

        # 获取余票数量
        left_tickets = data['data']['left_tickets']

        # 如果有余票，立即购买
        if int(left_tickets) > 0:
            # 发送POST请求购买车票
            buy_url = 'https://www.example.com/buy'
            payload = {
                'train_date': '2022-01-01',
                'from_station': '北京',
                'to_station': '上海',
                'purpose_codes': 'ADULT',
                'left_tickets': left_tickets
            }
            r = requests.post(buy_url, data=payload, headers=headers)

            # 输出购买结果
            print(r.text)
            break

        # 如果没有余票，等待一段时间后再次查询
        else:
            print('No tickets available, waiting...')
            time.sleep(5)

    # 捕获异常并输出错误信息
    except Exception as e:
        print(e)
        break
