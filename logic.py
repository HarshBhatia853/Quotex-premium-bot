import random
import datetime

# Edit this list with only real OTC pairs visible on Quotex
pairs = ["EURUSD", "USDJPY", "NZDCAD", "AUDJPY", "EURJPY", "GBPUSD"]

def generate_signal():
    pair = random.choice(pairs)
    direction = random.choice(["UP", "DOWN"])
    confidence = random.randint(90, 98)
    
    # Get current IST time + 30 seconds ahead
    now = (datetime.datetime.utcnow() + datetime.timedelta(seconds=19800 + 30)).strftime("%H:%M")
    
    return f"{pair} OTC - {now} - {direction} (Confidence: {confidence}%)"
