# 🤖 Jarvis AI — Sensor Data Analyzer v2.0 🧠  

An intelligent **AI sensor-data analytics engine** built using Python’s functional programming capabilities.  
This module processes simulated sensor readings, applies **lambda functions** for filtering and transformation, computes **statistical trends**, and learns from previous runs through **JSON-based AI memory**.

---

## 🚀 Overview  

Jarvis AI Sensor Analyzer observes real-world-style input streams — temperature, sound, and motion — then filters, normalizes, and interprets them in real time.  
The system maintains an **adaptive memory**, comparing new averages with historical data to detect whether environmental patterns have 📈 increased, 📉 decreased, or 🔁 remained stable.

---

## 🧩 Core Features  

- ⚙️ **Functional Data Processing:** Uses `filter()`, `map()`, and `reduce()` with `lambda` expressions.  
- 🧠 **AI Trend Memory:** Persists averages to a JSON file (`ai_log.json`) and compares with prior data.  
- 🌡️ **Dynamic Sensor Handling:** Tracks temperature, sound, and motion values, normalizing to a 0–1 scale.  
- 💬 **Intelligent Feedback:** Generates contextual AI responses such as activating cooling, muting sound, or detecting movement.  
- 📊 **Trend Visualization:** Displays sensor averages and trend indicators after each run.  

---

## 🧠 How It Works  

| Step | Process | Description |
|------|----------|-------------|
| 1️⃣ | **Filtering** | Keeps only relevant sensor data (temperature > 25, sound > 50, motion > 0). |
| 2️⃣ | **Normalization** | Scales sensor readings between 0–1 using lambda functions. |
| 3️⃣ | **Computation** | Uses `reduce()` to compute sensor averages. |
| 4️⃣ | **Trend Analysis** | Compares new averages to previous logs stored in JSON. |
| 5️⃣ | **AI Decisions** | Prints adaptive system responses based on sensor behavior. |

---

 
---

## 🧪 Technologies Used  

- **Python 3.11+**  
- Built-in modules: `functools`, `json`, `os`  
- Functional programming tools: `map()`, `filter()`, `reduce()`, `lambda`  

---

## 🧭 Future Enhancements  

- 🧩 Integrate real-time sensor simulation or live data streams.  
- 📉 Add visualization dashboards (Matplotlib/Plotly).  
- 🧠 Implement anomaly detection with adaptive thresholds.  
- 🔐 Introduce encrypted AI memory logging.  

---

## 💡 Author  

Developed by **Jay**, an AI developer passionately exploring **Artificial Intelligence architecture and data intelligence**.  
This project is part of the growing *Jarvis AI ecosystem* — a step toward building a full self-learning assistant.

---
