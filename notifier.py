import requests
from config import SERVERCHAN_KEY

def push(flights: list):
    if not flights:
        print("没有特价机票，不推送")
        return

    # 按价格排序
    flights.sort(key=lambda x: x["price"])

    # 构建消息
    title = f"✈️ 发现 {len(flights)} 条特价机票！最低 ¥{flights[0]['price']}"
    
    lines = []
    for f in flights:
        lines.append(
            f"**{f['from']} → {f['to']}** | 📅 {f['date']} | 💰 **¥{f['price']}** | 来源: {f['source']}\n"
            f"[立即抢购]({f['url']})\n"
        )
    
    content = "\n---\n".join(lines)

    url = f"https://sctapi.ftqq.com/{SERVERCHAN_KEY}.send"
    resp = requests.post(url, data={"title": title, "desp": content})
    
    if resp.json().get("code") == 0:
        print(f"推送成功！共 {len(flights)} 条")
    else:
        print(f"推送失败: {resp.text}")
