import requests, random
TOKEN = "8308171886:AAHj2c2K3C4QZ7t0J0J0J0J0J0"
CHANNEL = "-1004430722755"
def send_photo(photo, caption):
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    requests.post(url, data={"chat_id": CHANNEL, "photo": photo, "caption": caption, "parse_mode": "HTML"}, timeout=20)
resp = requests.get("https://api.binance.com/api/v3/ticker/24hr", timeout=15).json()
usdt = [x for x in resp if x['symbol'].endswith('USDT')]
top5 = sorted(usdt, key=lambda x: float(x['priceChangePercent']), reverse=True)[:5]
top = top5[0]
send_photo("https://images.unsplash.com/photo-1640340434855-6084ec1f490c?w=800", f"🚀 <b>بامب جديد!</b>\n\n💰 {top['symbol']}\n📈 {float(top['priceChangePercent']):.2f}%\n💵 {top['lastPrice']}")
coin = random.choice(top5)
send_photo("https://images.unsplash.com/photo-1621761191319-c6fb62004040?w=800", f"💎 <b>اكتتاب جديد!</b>\n\n🪙 {coin['symbol'].replace('USDT','')}\n🏦 Binance / Bybit / OKX")
