from functools import reduce
import json
import os

# Color support (uses colorama if available, falls back to ANSI codes)
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except Exception:
    class _Ansi:
        RED = '\033[31m'
        GREEN = '\033[32m'
        YELLOW = '\033[33m'
        BLUE = '\033[34m'
        MAGENTA = '\033[35m'
        CYAN = '\033[36m'
        RESET = '\033[0m'
    class Fore:
        RED = _Ansi.RED; GREEN = _Ansi.GREEN; YELLOW = _Ansi.YELLOW
        BLUE = _Ansi.BLUE; MAGENTA = _Ansi.MAGENTA; CYAN = _Ansi.CYAN
    class Style:
        RESET_ALL = _Ansi.RESET

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
    lambda x: {"sensor": x["sensor"], "value": normalize(
        x["value"], limits[x["sensor"]]
        )},
    filtered_data
))

# Step 3️⃣: Compute average per sensor
def avg_for(sensor_type):
    readings = list(map(lambda x:
            x["value"], filter(lambda x: x["sensor"] == sensor_type, normalized_data)))
    return round(reduce(lambda a, b:
            a + b, readings) / len(readings), 2) if readings else 0

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
    sep = f"{Fore.BLUE}{'-'*51}{Style.RESET_ALL}"
    print(f"\n{Fore.CYAN}🤖 Jarvis AI — Sensor Data Analyzer v2.0 🧠{Style.RESET_ALL}")
    print(sep)

    current_log = {
        "temperature": avg_temp,
        "sound": avg_sound,
        "motion": avg_motion
    }

    prev_log = load_previous_log()
    trends = compare_trend(current_log, prev_log)

    print(f"{Fore.MAGENTA}📊 Total Data:{Style.RESET_ALL} {Fore.GREEN}{len(sensor_data)}{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}✅ Processed:{Style.RESET_ALL} {Fore.GREEN}{len(filtered_data)}{Style.RESET_ALL}\n")

    print(f"{Fore.MAGENTA}🌡️ Temperature Avg:{Style.RESET_ALL} {Fore.GREEN}{avg_temp}{Style.RESET_ALL} → {Fore.YELLOW}{trends['temperature']}{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}🔊 Sound Avg:{Style.RESET_ALL}      {Fore.GREEN}{avg_sound}{Style.RESET_ALL} → {Fore.YELLOW}{trends['sound']}{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}🚶 Motion Avg:{Style.RESET_ALL}     {Fore.GREEN}{avg_motion}{Style.RESET_ALL} → {Fore.YELLOW}{trends['motion']}{Style.RESET_ALL}\n")

    # AI Reactions
    if avg_temp > 0.6:
        print(f"{Fore.RED}🧊 AI Response:{Style.RESET_ALL} {Fore.GREEN}Cooling system activated.{Style.RESET_ALL}")
    if avg_sound > 0.6:
        print(f"{Fore.RED}🔇 AI Response:{Style.RESET_ALL} {Fore.GREEN}Noise suppression active.{Style.RESET_ALL}")
    if avg_motion > 0.5:
        print(f"{Fore.RED}🚨 AI Response:{Style.RESET_ALL} {Fore.GREEN}Movement detected! Security on.{Style.RESET_ALL}\n")

    save_current_log(current_log)
    print(f"{Fore.GREEN}🧠 AI log updated successfully.{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Jarvis System is Online ✅{Style.RESET_ALL}")
    print(sep)

if __name__ == "__main__":
    main()
