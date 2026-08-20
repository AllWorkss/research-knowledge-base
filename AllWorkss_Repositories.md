# AllWorkss GitHub Repositories - Deep Dive

This document contains an in-depth look at all repositories under the `AllWorkss` GitHub account, including full descriptions, languages, and detailed README information.

## [ABIs-Mobile-App](https://github.com/AllWorkss/ABIs-Mobile-App)
**Language**: Java | **Stars**: 0 | **Forks**: 0

**Description**: ABIs Mobile App

### Repository Details (README)

<details>
<summary>Click to expand full README</summary>

# ABIS Mobile App

Free, low-cost Android wrapper for the ABIS web application at `https://allworkss.space`.

## What this app does

- Loads the existing ABIS SaaS web app in a secure Android WebView.
- Supports Google OAuth redirects in the same WebView.
- Supports Razorpay web checkout from the existing web payment flow.
- Supports file upload from Android storage/camera providers.
- Supports report/PDF downloads through Android Download Manager.
- Shows a friendly offline screen when the phone has no internet.
- Uses only free Android platform components; there are no paid mobile SDK dependencies.

## Build

```bash
gradle :app:assembleDebug
```

For Play Store upload, generate a signed Android App Bundle from Android Studio or run:

```bash
gradle :app:bundleRelease
```

> Note: Play Store publishing still requires a Google Play Developer account.

## App configuration

- Package/application id: `com.allworkss.abis`
- App name: `ABIS`
- Website URL: `https://allworkss.space`
- Min SDK: 23
- Target SDK: 35


</details>

---

## [AllWorkss](https://github.com/AllWorkss/AllWorkss)
**Language**: Python | **Stars**: 0 | **Forks**: 0

**Description**: No description provided.

### Repository Details (README)

<details>
<summary>Click to expand full README</summary>

<div align="center">

<h3><code>AllWorkss@github ~ $ ./contributions.sh</code></h3>
<img src="./contrib-heatmap.svg" width="860" />

<br><br>

<h3><code>AllWorkss@github ~ $ whoami</code></h3>
<table>
  <tr>
    <td valign="top"><img src="./avi-ascii.svg" width="370" /></td>
    <td valign="top"><img src="./info-card.svg" width="490" /></td>
  </tr>
</table>

</div>


</details>

---

## [AllWorkss.in](https://github.com/AllWorkss/AllWorkss.in)
**Language**: Python | **Stars**: 0 | **Forks**: 0

**Description**: ALLWORKSS WEBSITE 

### Repository Details (README)

<details>
<summary>Click to expand full README</summary>

# AllWorkss Consultancy Website

A modern, professional website for AllWorkss Consultancy - SAP Business Consulting and Digital Solutions.

## Features

✨ **Modern Design**
- Beautiful gradient color scheme with animations
- Responsive design (mobile, tablet, desktop)
- Smooth transitions and floating effects
- Professional layout with excellent UX

🎯 **Core Features**
- Homepage with hero section and service showcase
- Consultancy booking system with calendar integration
- WhatsApp API integration for each service
- SEO optimized (meta tags, sitemap, robots.txt)
- Contact section with company information
- Services showcase with detailed descriptions

📱 **Services**
- SAP Consulting
- Web & Software Development
- Business Consulting
- Cloud Management (AWS, Google Cloud)
- Data & Analytics
- Inventory Management
- Marketing & Branding

## Tech Stack

- **Frontend**: Next.js, React, CSS Modules
- **Backend**: Node.js with Next.js API routes
- **Animations**: Framer Motion, CSS Animations
- **Deployment**: Railway.app

## Installation

### Prerequisites
- Node.js 16+
- npm or yarn

### Setup

1. Clone the repository:
```bash
git clone https://github.com/allworkss/allworkss.in.git
cd allworkss.in
```

2. Install dependencies:
```bash
npm install
```

3. Configure environment variables:
```bash
cp .env.local.example .env.local
```

Update `.env.local` with your settings:
- WhatsApp number: `NEXT_PUBLIC_WHATSAPP_NUMBER`
- Company details
- Google Calendar API credentials (for booking integration)

4. Run development server:
```bash
npm run dev
```

Visit `http://localhost:3000` to see the website.

## Deployment on Railway

### Step 1: Connect Repository
1. Go to [Railway.app](https://railway.app)
2. Click "New Project"
3. Select "Deploy from GitHub"
4. Connect your GitHub account
5. Select the `allworkss/allworkss.in` repository

### Step 2: Configure Environment Variables
In Railway dashboard:
1. Go to Variables
2. Add the following:
```
NEXT_PUBLIC_WHATSAPP_NUMBER=919004246792
NEXT_PUBLIC_COMPANY_PHONE=9004246792
NEXT_PUBLIC_COMPANY_EMAIL=theallworkss@gmail.com
NEXT_PUBLIC_COMPANY_ADDRESS=Shop 19, Noori Bella Vista, Mumbra, Mumbai, Maharashtra 400612
NEXT_PUBLIC_GOOGLE_CALENDAR_ID=your-google-calendar-id@group.calendar.google.com
GOOGLE_CALENDAR_API_KEY=your-api-key
GOOGLE_CALENDAR_AUTH_TOKEN=your-auth-token
```

### Step 3: Configure Custom Domain
1. In Railway project settings, go to "Custom Domain"
2. Add your domain: `www.allworkss.in`
3. Update DNS records with provided CNAME

### Step 4: Deploy
Railway will automatically deploy on every push to main branch.

## Google Calendar Integration

To enable appointment booking with Google Calendar:

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a new project
3. Enable "Google Calendar API"
4. Create OAuth 2.0 credentials
5. Add the credentials to `.env.local`
6. Set up webhook for booking notifications

## WhatsApp Integration

Each service has a pre-configured WhatsApp button that opens:
- WhatsApp chat with your business number
- Pre-filled message about the service
- Custom message for each service type

Phone: +91 9004246792

## SEO Optimization

- Meta tags for all pages
- Open Graph tags for social sharing
- Structured data markup
- Sitemap.xml
- Robots.txt
- Mobile-friendly design
- Fast page load times

## Build & Production

Build for production:
```bash
npm run build
npm run start
```

## Project Structure

```
├── pages/
│   ├── _app.js
│   ├── _document.js
│   ├── index.js (Homepage)
│   └── booking.js (Booking page)
├── components/
│   ├── Navbar.js
│   ├── Footer.js
│   └── ServiceCard.js
├── styles/
│   ├── globals.css
│   ├── Home.module.css
│   ├── Booking.module.css
│   └── ...
├── api/
│   └── booking.js
├── public/
│   ├── sitemap.xml
│   └── robots.txt
└── next.config.js
```

## Future Enhancements

- [ ] Blog section
- [ ] Client testimonials
- [ ] Case studies
- [ ] Team member profiles
- [ ] Email notifications
- [ ] Admin dashboard
- [ ] Database integration (PostgreSQL)
- [ ] Payment integration
- [ ] Live chat support
- [ ] Analytics integration

## Contact

- **Phone**: +91 9004246792
- **Email**: theallworkss@gmail.com
- **Address**: Shop 19, Noori Bella Vista, Mumbra, Mumbai, Maharashtra 400612

## License

© 2026 AllWorkss Consultancy. All rights reserved.

---

**Built with ❤️ for AllWorkss Consultancy**


</details>

---

## [CostFlow](https://github.com/AllWorkss/CostFlow)
**Language**: TypeScript | **Stars**: 0 | **Forks**: 0

**Description**: CSF Costing (Costing Sheet Flow) — Universal Multi-Industry AI/ML Powered Costing Platform. Next.js 14, TypeScript, ExcelJS real formulas, React Flow, Recharts, Zustand.

### Repository Details (README)

<details>
<summary>Click to expand full README</summary>

# CostFlow — CSF Costing

# 🎯 Universal Multi-Industry AI/ML Powered Costing Platform

[![Next.js](https://img.shields.io/badge/Next.js-14-black?logo=next.js)](https://nextjs.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-blue?logo=typescript)](https://www.typescriptlang.org)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-4-06B6D4?logo=tailwindcss)](https://tailwindcss.com)
[![ExcelJS](https://img.shields.io/badge/ExcelJS-Real%20Formulas-1D6F42)](https://github.com/exceljs/exceljs)
[![React Flow](https://img.shields.io/badge/React%20Flow-Interactive-8B5CF6)](https://reactflow.dev)

---

## 📋 Overview

**CostFlow (CSF Costing)** is a production-grade, modular costing platform that dynamically adapts to **any industry domain** without code modification. It ships with 5 industry presets, a live Excel exporter generating real formula cells, an interactive React Flow architecture diagram, AI/ML anomaly detection, and an optimal price recommender.

---

## 🏭 Supported Industries

| Industry | Preset Blocks |
|---|---|
| **Manufacturing & Fabrication** | Raw Material (Kg/m), Scrap %, Labor Shift Rate, Machine Wear, Surface Finishing |
| **Education (School/College)** | Classroom Allocation, Teacher Salary, Lab Fee, Bus Transport, Admin Overhead |
| **Retail & Kirana Store** | Landed Cost, Spoilage %, Store Overhead, Retail Margin, GST |
| **E-Commerce & D2C** | COGS, Packaging, Shipping Tiers, Payment Gateway %, CAC Buffer, Return Rate |
| **Construction & Metals** | Area (sq.m), Material Yield Loss, Fabrication Labor, Subcontract, Site Overhead |

---

## 🚀 Key Features

### ✅ Live Excel Export with Real Formulas
Cells in the exported `.xlsx` contain actual Excel formula strings (`=SUM(C2:C10)`, `=C5*D5*(1+E5)`) — not hardcoded values. Open in Excel and check the formula bar.

### ✅ React Flow Architecture Diagram
Interactive visualization of the full costing flow:
`[Raw Input] → [Unit Conversion] → [Cost Blocks] → [Tax/GST] → [Profit Markup] → [Selling Price]`
Click any node to see its underlying formula.

### ✅ ML Anomaly Detection
Z-score statistical analysis flags inputs that deviate >2σ from historical baselines with severity levels (low/medium/high).

### ✅ AI Price Recommender
Break-even optimizer + target margin slider + optimal price range calculator.

### ✅ Universal Unit Conversion Matrix
Seamless conversion across weight (Kg, g, Ton, lb), length (m, cm, mm, ft, inch), area (m², ft²), volume (L, mL, gal), count (pcs, dozen), and time (hr, shift, day, month).

### ✅ Dynamic Formula Engine
Evaluate user-defined expressions like `FinalCost = (MaterialCost * (1 + ScrapPct)) + (LaborHours * HourlyRate) + FinishingPerMeter` with live variable injection.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Framework | Next.js 14 (App Router) |
| Language | TypeScript 5 |
| Styling | Tailwind CSS 4 + Custom Design System |
| State | Zustand (with localStorage persistence) |
| Excel | ExcelJS (real formula cells) |
| Flow Diagram | React Flow |
| Charts | Recharts |
| Animation | Framer Motion |
| Icons | Lucide React |
| AI/ML | IQR + Z-Score anomaly detection |

---

## ⚡ Getting Started

```bash
# Clone
git clone https://github.com/AllWorkss/CostFlow.git
cd CostFlow/costflow-app

# Install dependencies
npm install

# Run development server
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

---

## 📁 Project Structure

```
costflow-app/
├── app/
│   ├── page.tsx              # Landing page with domain selector
│   ├── dashboard/page.tsx    # Main costing dashboard
│   ├── flow/page.tsx         # React Flow architecture diagram
│   └── api/export/route.ts  # Excel export API (real formulas)
├── lib/
│   ├── engine/
│   │   ├── domainPresets.ts  # 5 industry presets
│   │   ├── unitConverter.ts  # Unit conversion matrix
│   │   └── formulaEngine.ts  # Dynamic formula evaluator
│   ├── ml/
│   │   └── anomalyDetector.ts # IQR/Z-score anomaly detection
│   ├── excel/
│   │   └── excelExporter.ts  # ExcelJS 3-sheet export
│   └── store/
│       └── costingStore.ts   # Zustand global state
└── types/
    └── costing.ts            # TypeScript interfaces
```

---

## 📊 Excel Export — 3 Sheets

1. **Cost Summary** — All enabled blocks with formula column showing `=SUM()`, `=C5*D5*(1+E5)` etc., totals with real `=SUM(D5:D12)` formulas, conditional formatting for margins
2. **Variable Detail** — Every variable from every block with its value, unit, and column reference
3. **Formula Reference** — Side-by-side: human formula vs Excel formula string for all blocks

---

## 🤖 AI/ML Details

- **Anomaly Detector**: Uses Z-score method. Flags values >2σ from historical baselines. Severity: Low (2-2.5σ), Medium (2.5-3σ), High (>3σ).
- **Price Recommender**: `RecommendedPrice = TotalCost / (1 - TargetMargin)`. Break-even calculation, optimal price = geometric mean of recommended and break-even. Elasticity score based on margin ratio.

---

## 📜 License

MIT © 2026 CostFlow — CSF Costing System


</details>

---

## [grif_assistant](https://github.com/AllWorkss/grif_assistant)
**Language**: Python | **Stars**: 0 | **Forks**: 0

**Description**: No description provided.

### Repository Details (README)

<details>
<summary>Click to expand full README</summary>

# 👑 GRIF — Personal AI Executive & PC Command Center (Master Edition)

**GRIF** is an all-powerful personal executive AI assistant and PC command center. It operates via a private Telegram bot, understands **Hinglish, Hindi, and English** (Text, Voice Notes, & Photos/Documents), uses the official **Google Gemini API** with native **Multimodal Function Calling**, and executes advanced local PC & remote multi-PC automations.

---

## 📁 Directory Structure

```text
grif_assistant/
├── .env.example       # Environment variables template
├── requirements.txt   # Python project dependencies
├── README.md          # Comprehensive setup guide
├── config.py          # Configuration loader and security validator
├── memory.py          # Long-term persistent SQLite memory engine (memory.db)
├── local_agent.py     # Local PC automation engine (29+ tools)
├── brain.py           # Gemini AI engine with multimodal tool calling and Hinglish persona
├── main.py            # Async Telegram Bot entry point with voice, photo OCR, PDF & scheduler
└── remote_node.py     # Lightweight node agent for secondary PCs/Laptops
```

---

## ⚡ Master Features

1. 📧 **Email Dispatcher Engine:** Send emails via SMTP (`/email` or *"Email bhej user@domain.com..."*).
2. 💬 **WhatsApp Messenger:** Dispatch WhatsApp messages directly (`/whatsapp` or *"WhatsApp message bhej..."*).
3. 📶 **Windows Bluetooth Manager:** Discover and toggle Bluetooth devices (`/bt`).
4. ⏰ **System Alarm & Timer Audio Player:** Set PC speaker countdown alarms & audio alerts (`/alarm 60 Wake up`).
5. 📋 **PC Clipboard Manager:** Read or copy text to PC clipboard (`/clipboard`).
6. ⚡ **Active Process Manager & Task Killer:** Inspect top CPU/RAM processes (`/proc`) or terminate apps (`/kill chrome.exe`).
7. 📦 **ZIP Compressor & Exporter:** Compress any folder into `.zip` and send document directly to Telegram (`/zip Desktop`).
8. 📶 **Network & IP Diagnostics:** Retrieve local IP, public IP, hostname, and connectivity (`/net`).
9. 🌐 **Remote Web URL Launcher:** Open URLs on default PC browser (*"Open youtube.com on PC"*).
10. 🛡️ **AI Sentinel Mode:** `/sentinel` — Background webcam motion watcher with Telegram photo alerts.
11. 🧠 **Long-Term Memory Engine:** SQLite database (`memory.db`) via `memory.py` (`/memory`).
12. 📸 **Photo OCR & Document Scanner:** Send any photo/document image from Telegram — Gemini Vision reads text.
13. 📄 **Deep Research & PDF Report Generator:** Automatically generates formatted executive PDF reports.
14. 💻 **Remote Terminal Execution:** Execute CLI shell commands on host PC (`/cmd ipconfig`).
15. 🏠 **Smart Home IoT Control:** Dispatch webhooks to control smart devices.
16. 🎙️ **Voice Notes (Voice In / Voice Out):** Send voice messages and receive text + AI Voice Note replies!
17. 📸 **Screen Screenshot Vision:** `/screenshot` — High-res screen capture.
18. 📷 **Webcam Snapshot:** `/cam` — Live camera photo snapshot.
19. 🔒 **Windows Lock & Power Commands:** `/lock` — Lock workstation (`LockWorkStation`), Sleep, Shutdown, Restart.
20. 🔊 **Master Audio & Media Control:** Volume adjustment (0-100%), mute/unmute audio, play/pause music.
21. 🌅 **Automated Morning Briefing:** Daily 8:00 AM executive report (`/briefing`).
22. ⚙️ **Hardware Diagnostics:** Real-time CPU, RAM, disk space, and battery status (`/status`).
23. 📂 **Directory Explorer:** List files in Desktop/Downloads/Documents.
24. 📖 **File Reader:** Read content of local text, code, or markdown files.
25. 🚀 **App Launcher:** Launch `Notepad`, `Chrome`, `VSCode`, `Calculator`, `Cmd`, etc.
26. 📝 **Quick Notes Archive:** Timestamped `.txt` notes created in `Notes/`.
27. 🛡️ **Strict Security Guard:** Only allowed Telegram User IDs can command GRIF.

---

## 🚀 Quick Setup & Launch Guide

```bash
cd F:\grif_assistant
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```


</details>

---

## [jurisflow-by-allworkss](https://github.com/AllWorkss/jurisflow-by-allworkss)
**Language**: TypeScript | **Stars**: 0 | **Forks**: 0

**Description**: No description provided.

### Repository Details (README)

<details>
<summary>Click to expand full README</summary>

# JurisFlow by AllWorkss (Phase 1)
**Autonomous Legal Platform & Public Intake OS**  
*Powered by JurisAI Engine*

---

### Corporate Identity & Leadership
- **Parent Entity:** YARSA ALLWORKSS (OPC) PRIVATE LIMITED  
- **Managed By:** AllWorkss  
- **Leadership:**  
  - **Daniya** — Founder & Legal Domain Lead  
  - **Yasar Intakhab Khan** — CEO & Chief Systems Architect  
- **Environment:** Google Cloud Platform (GCP) + FastAPI + Next.js 14 + Cloud SQL (PostgreSQL/pgvector)

---

## Key Modules

### 1. Public Client Acquisition & Intake OS (`/frontend`)
- **Landing Page (`/`):** Strategic hero section, leadership credentials, practice area showcase, live trust statistics.
- **Interactive Case Viability Calculator:** Triage wizard computing bail urgency, limitation period, and risk score across BNS/BNSS, Corporate, Matrimonial, Sec 138, Cyber Crime, Property.
- **Public Case Filing Wizard (`/file-case`):** 4-step Zod-validated wizard with demographics, FIR/Notice narrative, secure file dropzone, OTP verification simulation, and tracking token (`AW-2026-CASE-XXXX`) generation.
- **Public Case Tracker (`/track-case`):** Instant case lookup by token ID, displaying progress timeline, assigned advocate, and hearing date.
- **Programmatic Legal SEO Engine (`/services/[city]/[practice-area]`):** Dynamic landing pages equipped with JSON-LD `LegalService`, `LegalArticle`, and `FAQPage` schemas.

### 2. Advocate War Room & AI Operating System (`/war-room`)
- **Dark-Mode Advocate Workspace (`/war-room`):** High-density workspace dashboard for Advocates.
- **Multimodal Evidence & Chargesheet OCR Canvas (`/war-room/evidence`):** PDF/Image analysis viewer with OCR bounding boxes, extracted facts, and witness statement contradiction matrix.
- **Indian Legal Code Matcher (`/war-room/legal-codes`):** Converter for IPC $\rightarrow$ BNS 2023, CrPC $\rightarrow$ BNSS 2023, and IEA $\rightarrow$ BSA 2023 with bailable/non-bailable indicators and penalty terms.
- **Automated Court Drafting Suite (`/war-room/drafting`):** AI generator for Anticipatory Bail, Regular Bail (BNSS 482/483), Sec 138 Legal Notice, and Written Statements.

### 3. Backend REST API Architecture (`/backend`)
- **FastAPI (Python 3.11+ async):** Clean architecture with SQLAlchemy 2.0 Async Engine, Pydantic v2 schemas.
- **Services:**
  - `bns_converter.py`: Mappings and vector search for Bharatiya Nyaya Sanhita (BNS), BNSS, and BSA.
  - `ocr_service.py`: Document extraction and contradiction identification algorithm.
  - `drafting_service.py`: Context-aware court petition builder.

---

## Directory Structure
```
F:\jurisflow-by-allworkss\
├── frontend/                # Next.js 14 App Router Frontend
│   ├── src/
│   │   ├── app/             # Next.js App Router pages
│   │   ├── components/      # UI components & Bento Grid
│   │   └── lib/             # TypeScript types & Mock data
│   ├── package.json
│   └── tailwind.config.js
└── backend/                 # FastAPI Python Backend
    ├── app/
    │   ├── api/v1/          # Endpoints (/intake, /legal-codes, /evidence, /drafting)
    │   ├── core/            # Configuration & Settings
    │   ├── models/          # SQLAlchemy DB Models
    │   ├── schemas/         # Pydantic Schemas
    │   └── services/        # AI Legal Engines & BNS Matcher
    ├── main.py
    └── requirements.txt
```

---

## Setup & Running Instructions

### Frontend (Next.js 14)
```bash
cd frontend
npm install
npm run dev
```
Open [http://localhost:3000](http://localhost:3000)

### Backend (FastAPI)
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```
Open API Docs at [http://localhost:8000/docs](http://localhost:8000/docs)


</details>

---

## [research-knowledge-base](https://github.com/AllWorkss/research-knowledge-base)
**Language**: Python | **Stars**: 0 | **Forks**: 0

**Description**: No description provided.

### Repository Details (README)

<details>
<summary>Click to expand full README</summary>

# Research & Knowledge Base

Welcome to your structured knowledge base!

## Folder Structure

*   **Trading/**: ZenithAlgo Pro algorithmic trading terminal source code, GCP deployment guides, and algorithmic strategies.
*   **BusinessPlans/**: Core business model (ABIS Company Profile), financial plans, and pitch drafts.
*   **Marketing/**: Marketing notes, target audience research (Meta Ads Strategy), and campaign ideas.
*   **Documents/**: Store official documents, legal texts, or reference PDFs here.
*   **Strategies/**: Brainstorms, action plans, and general execution steps.

## How to Sync

You can sync your files securely to your Private GitHub repository by running the script from the root folder:
`.\sync.ps1 -message "Your commit message"`


</details>

---

## [smartparchi](https://github.com/AllWorkss/smartparchi)
**Language**: TypeScript | **Stars**: 0 | **Forks**: 0

**Description**: No description provided.

### Repository Details (README)

<details>
<summary>Click to expand full README</summary>

# SmartParchi (स्मार्टपर्ची) - Modular OPD, Practice & Loose Tablet Dispensary ERP

SmartParchi is an ultra-fast, zero-friction Electronic Medical Record (EMR), Outpatient Practice Management, and Loose Tablet Dispensary software built for single-doctor OPDs, dispensing general physicians (GPs), dentists, optometrists, pediatricians, and multi-doctor polyclinics.

## 🚀 Key Ground-Reality Features

1. **Sub-5-Second Token Generator (< 5s)**: Instant 10-digit mobile lookup, 2-click new patient record creation, sequential daily token assignment (`Token #1, #2...`), and instant WhatsApp alert dispatch.
2. **"Pudiya" & Loose Dispensing Calculator**: Auto-calculates tablet counts (`Paracetamol 650mg TDS x 3 days = 9 tablets`) and deducts exact loose units from clinic inventory.
3. **1-Click Clinical Add-on Procedures**: Quick procedure chips (`+ IV Saline Drip ₹300`, `+ Injection Voveran ₹50`, `+ Nebulization ₹100`, `+ Wound Dressing ₹150`).
4. **Specialty Practice Modules**:
   - **Dental**: Interactive 32-Teeth SVG canvas (Cavities, RCT, Crowns, Fillings).
   - **Eye Refraction**: Matrix table for Right (OD) & Left (OS) eye Sph, Cyl, Axis, Add & Visual Acuity.
   - **Pediatrics**: WHO vaccination schedule & height/weight percentile growth tracker.
5. **Split Billing & Permanent Khata Ledger**: Mixed payments (Cash + UPI + Khata/Udhar) with permanent patient debt ledger alerts on future visits.
6. **Polyclinic Multi-Doctor Revenue Split**: Automated calculation of 70% Doctor / 30% Facility revenue splits.
7. **Waiting Room TV Screen Board (`/screen/token-board`)**: High-contrast waiting room TV view with Web Audio bell chime.
8. **Mobile-First Responsive & PWA-Ready**: Responsive design with touch-friendly navigation (>44px targets) and native bottom navigation for mobile phones and WebView wrappers.

---

## 🛠 Tech Stack

- **Framework**: Next.js 14 (App Router) + TypeScript
- **Styling**: Tailwind CSS + Lucide Icons + Framer Motion
- **Database & ORM**: PostgreSQL + Prisma ORM
- **Offline Cache**: Dexie.js (IndexedDB)
- **Container & Deployment**: Docker + GCP Cloud Run + GitHub Actions CI/CD

---

## 📦 Getting Started Locally

```bash
# 1. Install dependencies
npm install

# 2. Generate Prisma Client
npx prisma generate

# 3. Push Database Schema (Or set DATABASE_URL in .env)
npx prisma db push

# 4. Seed Sample Clinic & Medicines
npx prisma db seed

# 5. Start Development Server
npm run dev
```

Navigate to `http://localhost:3000`.

---

## 🐳 Docker & Google Cloud Run Deployment

```bash
# Build production Docker container
docker build -t smartparchi-app .

# Run locally on port 8080
docker run -p 8080:8080 -e DATABASE_URL="postgresql://user:password@localhost:5432/smartparchi" smartparchi-app
```


</details>

---

## [zenith_algo_terminal](https://github.com/AllWorkss/zenith_algo_terminal)
**Language**: Python | **Stars**: 0 | **Forks**: 0

**Description**: No description provided.

### Repository Details (README)

<details>
<summary>Click to expand full README</summary>

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


</details>

---

