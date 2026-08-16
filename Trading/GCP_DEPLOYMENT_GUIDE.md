# ☁️ ZenithAlgo Pro - Complete GCP Deployment & Broker Setup Guide

A complete, step-by-step guide to deploying **ZenithAlgo Pro** 24/7 on **Google Cloud Platform (GCP)** and connecting it to **Upstox API v2** and **ICICI Direct Breeze API**.

---

## 📌 STEP 1: Create a Google Cloud Platform (GCP) Virtual Machine

1. Log in to [Google Cloud Console](https://console.cloud.google.com/).
2. Navigate to **Compute Engine** ➔ **VM instances** ➔ Click **Create Instance**.
3. Configure the VM settings:
   - **Name:** `zenith-algo-terminal`
   - **Region:** `asia-south1 (Mumbai)` *(Recommended for ultra-low latency <10ms to Indian stock broker servers)*
   - **Machine Type:** `e2-medium` (2 vCPU, 4 GB RAM)
   - **Boot Disk:** Ubuntu 22.04 LTS (20 GB SSD)
   - **Firewall:** Check both ✅ **Allow HTTP traffic** and ✅ **Allow HTTPS traffic**.
4. Click **Create**.

---

## 📌 STEP 2: Configure GCP Firewall Rules (Allow Ports 8000 & 5000)

Your terminal needs ports `8000` (Web UI) and `5000` (Backend API) open to access it from your browser or mobile phone:

1. In GCP Console, search for **VPC Network** ➔ **Firewall**.
2. Click **Create Firewall Rule**:
   - **Name:** `allow-zenith-ports`
   - **Targets:** All instances in the network
   - **Source IPv4 Ranges:** `0.0.0.0/0`
   - **Protocols and ports:** Specified protocols and ports ➔ check `tcp` ➔ type `8000, 5000`.
3. Click **Create**.

---

## 📌 STEP 3: Deploy ZenithAlgo Pro via Docker (1-Click Command)

1. On your GCP VM Instances page, click the **SSH** button next to your `zenith-algo-terminal` instance to open the terminal.
2. Upload this `zenith_algo_terminal` folder to the VM or clone your repository.
3. Run the automated deployment script:
   ```bash
   cd zenith_algo_terminal
   chmod +x gcp_deploy.sh
   ./gcp_deploy.sh
   ```
4. Once completed, your software is running 24/7!
5. Open your browser and go to:
   `http://YOUR_GCP_VM_EXTERNAL_IP:8000`

---

## 📌 STEP 4: Connecting Broker APIs (Daily Authentication)

### 🔵 Option A: Upstox API v2
1. Log in to [Upstox Developer Console](https://developer.upstox.com/).
2. Create an App and get your **API Key** and **API Secret**.
3. Generate your daily **Access Token** via Upstox OAuth login.
4. Open your ZenithAlgo Terminal Web UI ➔ Go to **Upstox & ICICI Integration** tab.
5. Paste your Access Token in the token field and click **Connect Upstox Account**.

### 🟠 Option B: ICICI Direct Breeze API
1. Register on [ICICI Direct Breeze Portal](https://api.icicidirect.com/).
2. Copy your **App Key** and **Secret Key**.
3. Log in to ICICI Direct to generate your **Daily Session Token**.
4. In ZenithAlgo Terminal Web UI ➔ Go to **Upstox & ICICI Integration** tab ➔ Click **ICICI Direct Breeze API**.
5. Input App Key, Secret Key, and Session Token ➔ Click **Connect ICICI Breeze Account**.

---

## 🛡️ Capital Protection (Dad's Safety Guard)

- Max Daily Loss limit is set to **₹10,000** in `config.json`.
- If cumulative daily losses touch ₹10,000, the Python server automatically blocks all subsequent trade triggers to protect capital.
- Position sizing calculates exact lot sizes based on a maximum 1.5% capital risk per trade.
