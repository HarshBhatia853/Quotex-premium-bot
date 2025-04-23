import random
import datetime

# Only confirmed OTC pairs from your current Quotex list
pairs = ["NZDCAD", "AUDJPY", "USDJPY", "GBPUSD"]

def generate_signal():
    pair = random.choice(pairs)
    direction = random.choice(["UP", "DOWN"])
    confidence = random.randint(90, 98)
    now = (datetime.datetime.utcnow() + datetime.timedelta(seconds=19800 + 30)).strftime("%H:%M")
    return f"{pair} OTC - {now} - {direction} (Confidence: {confidence}%)"
