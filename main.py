import schedule
import time
from config import ORIGINS, MIN_PRICE
from scrapers.ctrip import fetch_low_price as ctrip_fetch
from scrapers.qunar import fetch_low_price as qunar_fetch
from notifier import push

def run():
    print(f"开始抓取特价机票（低于 ¥{MIN_PRICE}）...")
    all_flights = []
    
    for city in ORIGINS:
        print(f"  查询出发城市：{city['name']}")
        all_flights += ctrip_fetch(city["code"], city["name"], MIN_PRICE)
        all_flights += qunar_fetch(city["code"], city["name"], MIN_PRICE)
    
    # 去重（同出发/目的地/日期/价格）
    seen = set()
    unique = []
    for f in all_flights:
        key = (f["from"], f["to"], f["date"], f["price"])
        if key not in seen:
            seen.add(key)
            unique.append(f)
    
    print(f"共找到 {len(unique)} 条特价票")
    push(unique)

# 每天早上 9 点和下午 3 点各跑一次
schedule.every().day.at("09:00").do(run)
schedule.every().day.at("15:00").do(run)

if __name__ == "__main__":
    run()  # 启动时先跑一次
    while True:
        schedule.run_pending()
        time.sleep(60)
