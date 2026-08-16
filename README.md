# ZenithAlgo Pro - Algorithmic Trading & Indicator Studio

ZenithAlgo Pro is an institutional-grade, dark-themed Algorithmic Trading Software Terminal designed specifically for Indian retail traders using **Upstox API v2** and **ICICI Direct (Breeze API)**.

---

## 🌟 Key Features

1. **Live Interactive Candlestick Chart**: Real-time canvas charting engine for NIFTY 50, BANK NIFTY, RELIANCE, TCS, TATA MOTORS, and HDFC BANK.
2. **Dynamic BUY ▲ / SELL ▼ Signals**: Visual alerts placed directly on candles based on multi-indicator conditions.
3. **Best Proven Technical Indicators**:
   - EMA (9 & 21 Period Crossovers)
   - Supertrend (10, 3)
   - VWAP (Volume Weighted Average Price)
   - Bollinger Bands (20, 2)
   - RSI (14 Period Sub-Chart with 70/30 bounds)
4. **Dad's Safety Guard (Capital Protection)**:
   - Daily Circuit Breaker Loss Limit (e.g. ₹10,000 max daily loss)
   - Strict 1.5% Risk per trade position sizing calculator
   - Emotionless automated order execution
5. **Historical Strategy Backtester**:
   - Test strategies on 12 months of historical data with Win Rate %, Profit Factor, Max Drawdown %, and Equity Curve.
6. **Broker API Integration (Upstox & ICICI Breeze)**:
   - Built-in Flask API Gateway (`server.py`) and standalone Python bots (`upstox_algo_bot.py` & `icici_breeze_algo_bot.py`).

---

## 🚀 How to Run Locally (Windows 1-Click Launch)

1. Open the project folder: `c:\Users\Admin\Desktop\zenith_algo_terminal\`.
2. Double click **`setup_python_env.bat`** (installs required Python packages).
3. Double click **`run_terminal.bat`** (launches the local server and opens `http://localhost:8000`).

---

## ☁️ How to Deploy on Google Cloud Platform (GCP)

1. Create a VM instance on [Google Cloud Console](https://console.cloud.google.com/) in region **`asia-south1 (Mumbai)`** for sub-10ms latency to Upstox & ICICI Direct servers.
2. Upload this folder to your GCP VM.
3. Run the automated GCP deployment bash script:
   ```bash
   chmod +x gcp_deploy.sh
   ./gcp_deploy.sh
   ```
4. Access your live trading software anywhere at `http://YOUR_GCP_VM_IP:8000`.

---

## 📂 File Inventory

- `index.html` - HTML5 Trading Dashboard UI
- `style.css` - Dark Glassmorphism Design Architecture
- `app.js` - Chart Engine, Indicators, Signals & Backtester Logic
- `server.py` - Flask Backend API Bridge
- `upstox_algo_bot.py` - Python Auto-Trader for Upstox API v2 (`upstox-python-sdk`)
- `icici_breeze_algo_bot.py` - Python Auto-Trader for ICICI Breeze API (`breeze-connect`)
- `run_terminal.bat` - Windows 1-Click Launcher
- `setup_python_env.bat` - Python Dependency Installer
- `config.json` - System Configuration Settings
- `requirements.txt` - Python Package Requirements
- `Dockerfile` & `docker-compose.yml` - Docker Container Setup for Cloud Deployment
- `gcp_deploy.sh` - Google Cloud Deployment Script
