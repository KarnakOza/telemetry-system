# 🚀 Real-Time Telemetry System (C + Python)

From raw binary packets to a live mission control dashboard.

---

## 📡 Overview

This project simulates a satellite telemetry pipeline:

- Telemetry generation in C
- Binary packet encoding
- CRC-based integrity checking
- Packet corruption simulation
- Binary parsing in Python
- Real-time visualization dashboard

---

## ⚙️ System Architecture

C (Telemetry Generator)
    ↓
Binary File (telemetry.bin)
    ↓
Python Parser (struct.unpack)
    ↓
CSV Logging
    ↓
Dash Dashboard (Live Visualization)

---

## 🔐 Features

- Custom telemetry packet (CCSDS-inspired)
- CRC32 integrity verification
- Bit-level corruption simulation
- Packet analyzer (Wireshark-style)
- Hex dump inspection
- Real-time dashboard with alerts

---

## 📊 Demo

### 🎥 Live Dashboard
![Dashboard](media/demo.gif)

### 🔍 Packet Analyzer
![Analyzer](media/analyzer.png)

### 💾 Hex View
![Hex](media/hex.png)

---

## 🛠 Tech Stack

- C (low-level telemetry)
- Python
- Dash (visualization)
- struct (binary parsing)

---

## ▶️ How to Run

### 1. Compile C
```bash
gcc src/*.c -o telemetry
