from functools import reduce
import json
import os

LOG_FILE = "ai_log.json"

sensor_data = [
    {"sensor": "temperature", "value": 42},
    {"sensor": "sound", "value": 85},
    {"sensor": "motion", "value": 0},
    {"sensor": "temperature", "value": 10},
    {"sensor": "sound", "value": 40},
    {"sensor": "motion", "value": 1},
    {"sensor": "temperature", "value": 20},
    {"sensor": "sound", "value": 60},
    {"sensor": "motion", "value": 1},
    {"sensor": "temperature", "value": 30},
    {"sensor": "sound", "value": 70},
    {"sensor": "motion", "value": 1},
    {"sensor": "temperature", "value": 40},
    {"sensor": "sound", "value": 80},
    {"sensor": "motion", "value": 1},
    {"sensor": "temperature", "value": 50},
    {"sensor": "sound", "value": 90},
    {"sensor": "motion", "value": 1}
]

# Step 1️⃣: Filter relevant readings
filtered_data = list(filter(
    lambda x: (x["sensor"] == "temperature" and x["value"] > 25)
    or (x["sensor"] == "sound" and x["value"] > 50)
    or (x["sensor"] == "motion" and x["value"] > 0),
    sensor_data
))

# Step 2️⃣: Normalize data (AI-style)
normalize = lambda value, max_value: round(value / max_value, 2)
limits = {"temperature": 100, "sound": 120, "motion": 1}

normalized_data = list(map(
    lambda x: {"sensor": x["sensor"], "value": normalize(x["value"], limits[x["sensor"]])},
    filtered_data
))

# Step 3️⃣: Compute average per sensor
def avg_for(sensor_type):
    readings = list(map(lambda x: x["value"], filter(lambda x: x["sensor"] == sensor_type, normalized_data)))
    return round(reduce(lambda a, b: a + b, readings) / len(readings), 2) if readings else 0

avg_temp = avg_for("temperature")
avg_sound = avg_for("sound")
avg_motion = avg_for("motion")

# Step 4️⃣: AI Trend Analyzer
def load_previous_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            logs = json.load(f)
            return logs[-1] if logs else None
    return None

def save_current_log(log):
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            logs = json.load(f)
    logs.append(log)
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2)

def compare_trend(current, previous):
    trends = {}
    for key in current:
        if previous and key in previous:
            if current[key] > previous[key]:
                trends[key] = "📈 increased"
            elif current[key] < previous[key]:
                trends[key] = "📉 decreased"
            else:
                trends[key] = "🔁 stable"
        else:
            trends[key] = "🆕 no previous data"
    return trends

# Step 5️⃣: AI Decision Engine
def main():
    print("\n🤖 Jarvis AI — Sensor Data Analyzer v2.0 🧠")
    print("---------------------------------------------------")

    current_log = {
        "temperature": avg_temp,
        "sound": avg_sound,
        "motion": avg_motion
    }

    prev_log = load_previous_log()
    trends = compare_trend(current_log, prev_log)

    print(f"📊 Total Data: {len(sensor_data)}")
    print(f"✅ Processed: {len(filtered_data)}\n")

    print(f"🌡️ Temperature Avg: {avg_temp} → {trends['temperature']}")
    print(f"🔊 Sound Avg: {avg_sound} → {trends['sound']}")
    print(f"🚶 Motion Avg: {avg_motion} → {trends['motion']}\n")

    # AI Reactions
    if avg_temp > 0.6: print("🧊 AI Response: Cooling system activated.")
    if avg_sound > 0.6: print("🔇 AI Response: Noise suppression active.")
    if avg_motion > 0.5: print("🚨 AI Response: Movement detected! Security on.\n")

    save_current_log(current_log)
    print("🧠 AI log updated successfully.")
    print("Jarvis System is Online ✅")
    print("---------------------------------------------------")

if __name__ == "__main__":
    main()
