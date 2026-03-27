import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Referer": "https://flight.qunar.com/",
}

def fetch_low_price(origin_code: str, origin_name: str, min_price: int) -> list:
    """抓取去哪儿低价机票（低价地图接口）"""
    results = []
    url = "https://flight.qunar.com/site/low_price_map.htm"

    params = {
        "fromCode": origin_code,
        "from": origin_name,
        "type": "dom",   # dom=国内
    }

    try:
        resp = requests.get(url, params=params, headers=HEADERS, timeout=10)
        data = resp.json()
        
        for dest in data.get("data", []):
            price = dest.get("price", 9999)
            if price <= min_price:
                results.append({
                    "source": "去哪儿",
                    "from": origin_name,
                    "to": dest.get("arrCityName", "未知"),
                    "date": dest.get("departDate", ""),
                    "price": price,
                    "url": f"https://flight.qunar.com/site/oneway_index.htm?searchDepartureAirport={origin_name}&searchArrivalAirport={dest.get('arrCityName','')}"
                })
    except Exception as e:
        print(f"[去哪儿] 抓取失败: {e}")
    
    return results
