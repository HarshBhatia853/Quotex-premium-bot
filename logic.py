import random
import datetime

pairs = ["EURUSD", "GBPUSD", "USDJPY", "AUDUSD", "USDCAD", "NZDCAD", "USDCHF", "EURJPY", "GBPJPY", "AUDCAD", "AUDJPY", "CADCHF", "EURGBP"]

def generate_signal():
    pair = random.choice(pairs)
    direction = random.choice(["UP", "DOWN"])
    confidence = random.randint(90, 98)
    now = (datetime.datetime.utcnow() + datetime.timedelta(seconds=30)).strftime("%H:%M")
    return f"{pair} OTC - {now} - {direction} (Confidence: {confidence}%)"
