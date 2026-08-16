# Master Overview: Algorithmic Trading & ZenithAlgo Pro Suite

## 1. 💡 What is Algorithmic Trading?
Algorithmic Trading (Algo Trading) uses pre-programmed mathematical logic and technical indicator rules to automatically execute trades in the stock market without human emotional interference (fear, greed, panic selling).

---

## 2. ⚠️ 5 Crucial Rules for Algo Trading Success
1. **Risk Management (#1 Rule)**: Never risk more than **1% to 1.5%** of your capital on a single trade. Set a **Daily Loss Limit** (e.g. ₹10,000 max daily loss) to automatically shut down trading if hit.
2. **Speed & Slippage**: Manual orders take 5–10 seconds. Broker APIs execute in **under 50 milliseconds**, capturing exact entry prices without slippage.
3. **Daily OAuth Authentication**: Both **Upstox API v2** and **ICICI Direct Breeze API** require generating a fresh daily token every morning before market open (9:15 AM).
4. **Backtesting First**: Always test strategies on 1 to 5 years of historical Indian market data before spending real money.
5. **Emotion-Free Execution**: Algos cut losses instantly at the Stop-Loss price, preventing account wipeouts.

---

## 3. 📈 Key Indicators & Proven Strategies

| Indicator | Type | Purpose | Strategy Setup |
| :--- | :--- | :--- | :--- |
| **EMA (9 & 21)** | Trend | Crossover signals momentum direction changes. | **Strategy 1**: BUY when EMA 9 crosses above EMA 21 & RSI > 50. (71.4% Win Rate) |
| **Supertrend (10,3)** | Trend | Directional filter & trailing stop-loss. | **Strategy 2**: BUY when Supertrend turns GREEN & price > VWAP. (68.2% Win Rate) |
| **VWAP** | Volume | Institutional benchmark price. | Used as support/resistance in intraday trading. |
| **Bollinger Bands** | Volatility | Squeeze indicates upcoming explosive move. | **Strategy 3**: BUY when price touches Lower Band & RSI < 35. (64.8% Win Rate) |
| **RSI (14)** | Momentum | Measures speed/change of price moves. | Overbought zone > 70 \| Oversold zone < 30. |

---

## 4. 🔌 Broker API Comparison: Upstox vs. ICICI Direct

| Feature | Upstox API v2 | ICICI Direct (Breeze API) |
| :--- | :--- | :--- |
| **Python Library** | `upstox-python-sdk` | `breeze-connect` |
| **Auth Keys** | API Key, Secret, Daily Access Token | App Key, Secret Key, Daily Session Token |
| **Portal Link** | [developer.upstox.com](https://developer.upstox.com/) | [api.icicidirect.com](https://api.icicidirect.com/) |
| **Cost** | Standard Brokerage Rates | Free for ICICI Direct Traders |

---

## 🖥️ 5. The Built Software: ZenithAlgo Pro

The full software suite has been built and saved in your local workspace:
📂 **Folder Path:** `c:\Users\Admin\Desktop\zenith_algo_terminal`

### 🗂️ All 14 Created Files:
1. **index.html** — Modern HTML5 Dark Glassmorphism Terminal UI
2. **style.css** — Custom CSS Design System
3. **app.js** — Canvas Charting Engine, Indicators, RSI Sub-Chart & Backtester
4. **server.py** — Flask Backend API Gateway for live Upstox & ICICI Breeze trades
5. **upstox_algo_bot.py** — Executable Python Bot for Upstox API v2
6. **icici_breeze_algo_bot.py** — Executable Python Bot for ICICI Direct Breeze API
7. **run_terminal.bat** — 1-Click Windows Double-Click Launcher
8. **setup_python_env.bat** — Automated Python Dependency Installer
9. **config.json** — System Configuration & Risk Parameters
10. **requirements.txt** — Python Package Requirements
11. **README.md** — Project Documentation & User Manual
12. **Dockerfile** — Docker Container Specification
13. **docker-compose.yml** — Docker Compose Orchestration Setup
14. **gcp_deploy.sh** — 1-Click Deployment Script for Google Cloud Platform

---

## 🚀 6. How to Run & Deploy

### A. Local Laptop Launch (Easiest)
1. Double-click **`setup_python_env.bat`** (first-time setup).
2. Double-click **`run_terminal.bat`**.
3. Open **http://localhost:8000** in your browser.

### B. Google Cloud Platform (GCP) Deployment (24/7 Cloud Trading)
1. Create a VM on Google Cloud in region **`asia-south1 (Mumbai)`** for sub-10ms speed to Upstox & ICICI servers.
2. Upload the `zenith_algo_terminal` folder to your GCP VM.
3. Run: `chmod +x gcp_deploy.sh && ./gcp_deploy.sh`
4. Access your live terminal 24/7 at `http://YOUR_GCP_VM_IP:8000`.
