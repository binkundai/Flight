from dotenv import load_dotenv
import os

load_dotenv()

SERVERCHAN_KEY = os.getenv("SERVERCHAN_KEY")
MIN_PRICE = int(os.getenv("MIN_PRICE", 300))

# 出发城市（江浙沪）
ORIGINS = [
    {"name": "上海", "code": "SHA"},
    {"name": "南京", "code": "NKG"},
    {"name": "杭州", "code": "HGH"},
    {"name": "无锡", "code": "WUX"},
    {"name": "宁波", "code": "NGB"},
    {"name": "南通", "code": "NTG"},
]
