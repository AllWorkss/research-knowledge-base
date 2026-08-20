# ALLWORKSS ENTERPRISE AI ECOSYSTEM — SESSION 2 MASTER ARCHITECTURAL DOSSIER

**Lead Architect:** Yasar Intakhab Khan (M.Sc. Data Science & IT, Cloud Architect)

**Commercial Entity:** YARSA ALLWORKSS (OPC) PRIVATE LIMITED

**WhatsApp:** +919004246792
**Session Scope:** Dual-System Runtime, 9-Repo Isolation, Turbo Sync & Hybrid CI/CD

---

## 1. DUAL-SYSTEM WORKSTATION COEXISTENCE MATRIX (HOST: F:\ DRIVE)

| Dimension | System 1: GRIF-CORE WORKSTATION | System 2: ALLWORKSS ENTERPRISE HUB | Shared Inference Engine (Ollama) |
| :--- | :--- | :--- | :--- |
| **Directory** | `F:\AllWorkss_AI_Bridge\` | `F:\ALLWORKSSHUB\` | Localhost Daemon |
| **Dedicated Port** | `localhost:8000` (FastAPI / WebSockets) | `localhost:8501` (Streamlit Dashboard) | `localhost:11434` (Ollama REST API) |
| **Primary Domain** | Autonomous Win32 OS Actuation, Screen Vision (`mss`), Mobile PWA, WhatsApp CRM, Invoicing | M.Sc. Data Science Second Brain, ERP Tabular Anomaly Hunter, LaTeX Math, LoRA Telemetry | Neural Engine (`allworkss-omni`, `grif-core` via Qwen-2.5-Coder / 7B) |
| **Data / Storage** | `memoryvault.db` (Exclusive SQLite Owner) | Isolated Tabular CSV/Excel & Git Docs | Shared Model Weights & Context Cache |
| **Resource Guard** | Full CPU/VRAM Headroom for live execution | Strict 300MB–500MB RAM budget, 0% local VRAM | 15-second graceful request queue, zero crash |

---

## 2. VERIFIED 9-PROJECT REPOSITORY NAMESPACE ISOLATION

Each project operates in strict sandbox isolation to prevent port collisions, cross-database corruption, or logic bleeding:

1. `F:\AllWorkss.in`: Official enterprise website, consulting portfolio, and brand gateway.
2. `F:\AllWorkss_AI_Bridge`: Autonomous AI workstation, PWA backend (Port 8000), Win32 system actuators.
3. `F:\allworkss-bi-suite`: 360° AI Business Intelligence Suite, SAP ERP analytics & predictive modeling.
4. `F:\AllWorkss-Cloud-Infra-Mangement`: Cloud IaC (Infrastructure as Code), Docker topologies, server configs.
5. `F:\CostFlow`: Enterprise SaaS expense tracking, financial optimization, and burn-rate intelligence.
6. `F:\grif_assistant`: Voice engine, offline STT/TTS assistant, and desktop helper routines.
7. `F:\jurisflow-by-allworkss`: Autonomous workflow DAG execution engine and compound background task queues.
8. `F:\SmartParchi`: Digital receipt generation, GSTIN OCR tax reconciliation, and POS mobile bridge.
9. `F:\research-knowledge-base-master` (Alias: `research-knowledge-base`): M.Sc. Research second brain, ML algorithms, LaTeX math formulations, and PyTorch research papers.

---

## 3. PRODUCTION MODULE STATUS (ALLWORKSS AI BRIDGE)

* **14 Verified Production Modules (100% Operational):**
  * `unifiedmemory.py`: Cross-process persistent SQLite memory synchronization.
  * `systemactuator.py`: Win32 API window control, process monitor, task killer, and network toggle.
  * `In-Memory Screen Capture`: Sub-50ms low-latency screen streaming via `mss` (`/api/screen`).
  * `webserver.py`: Asynchronous FastAPI & WebSockets token-streaming and audio server.
  * `static/index.html`: Glassmorphic mobile PWA with PIN 7860 gatekeeper authentication.
  * `sttengine.py` & `edge-tts`: Faster-Whisper Hinglish engine with `hi-IN-SwaraNeural` voice.
  * `gitmanager.py`: Automated Git commits, status logs, and branch sync routines.
  * `webintelligence.py`: Clean HTML stripping web scraper and 4-bullet executive summarizer.
  * `emaildispatcher.py` & `gdrivebridge.py`: Official AllWorkss branded SMTP dispatch and cloud backup.
  * `browserrobot.py`: Headless/Headed Playwright automation for GSTIN and enterprise portals.
  * `whatsappgateway.py`: Real-time lead capture and dynamic PDF proposal generator.
  * `gstinreconciliation.py`: Computer Vision OCR with tax formula mathematical verification.
  * `socialintelligence.py` & `adcopygenerator.py`: Social viral metrics and AIDA/PAS copy engines.
  * `marketingreporter.py`: Luxury enterprise-grade PDF audit and business intelligence report generator.

* **v12.0 Expansion Modules (Antigravity Pipeline):**
  * `proactivescheduler.py`: Background daemon, RAM trimmer (>88% threshold), 9:00 AM briefing.
  * `livescreenvision.py`: Active window OCR lens for code bug analysis and UI review.
  * `researchstudyengine.py`: LaTeX equation generator and NumPy/PyTorch companion.
  * `workflowplanner.py`: Directed Acyclic Graph (DAG) compound task coordinator.
  * `displaywindowmanager.py`: Win32 window snapping, volume controls, and session locker.
  * `clientcrminvoicing.py`: GST automated calculator with luxury invoice PDF engine.
  * `codesandboxrunner.py`: Isolated subprocess code runner with a strict 10s timeout guard.
  * `morningbriefing.py`: Executive audio standup routine ("Start My Day").

---

## 4. LOCAL AUTOMATION, TURBO COMPILATION & CLI TOOLS

* **Alias-Aware Multi-Repository Sync Engine (`sync_selected_projects.py`):**
  * Parses all 9 repositories on `F:\` drive dynamically, supporting folder aliases (e.g., `research-knowledge-base-master` vs `research-knowledge-base`).
  * Extracts configs (`requirements.txt`, `package.json`, `Dockerfile`) and docs (`.md`, `.txt`).
  * Injects high-density system prompts into Ollama Modelfile with `num_ctx 8192` and `num_thread 8`.
  * Benchmark: Full 9-project compilation completed in **1.42 seconds** with zero RAM bottleneck.
* **1-Click Batch Synchronizer:** Mapped to `C:\Users\Admin\Desktop\Sync_Projects_Brain.bat`.
* **Global Git-AI CLI Bridge (`git_ollama_bridge.py`):**
  * Registered at `$env:LOCALAPPDATA\Microsoft\WindowsApps\git-ai.bat`.
  * Commands: `git-ai commit` (AI commit messages & push), `git-ai review` (local diff code review), `git-ai status`.

---

## 5. HYBRID CLOUD-TO-EDGE ARCHITECTURAL PIPELINE

```text
[THOUGHT / PROMPT CORE] (Gemini Co-Architect)
                 |
                 v
[LOCAL DEV RUNTIME] (Antigravity IDE / VS Code)
                 |
       +---------+-------------------------+
       v                                   v
[CLOUD CI/CD PIPELINE]              [EDGE WORKSTATION (F:\ DRIVE)]
       |                                   |
       v                                   +--> System 1: GRIF-CORE (Port 8000)
GitHub Remote Repo                         |    (FastAPI, Win32 OS, PWA, CRM)
       |                                   |
       v                                   +--> System 2: ALLWORKSS HUB (Port 8501)
Google Cloud Build (Triggers)              |    (Streamlit, M.Sc. Brain, ERP Hunter)
       |                                   |
       v                                   +--> 1-Click Sync Batch --> Ollama (Port 11434)
Google Cloud Run                            |    (allworkss-omni, 8K Turbo, 9 Repos)
(Serverless Auto-Scaling Container)
```

---

## 6. SESSION CLOSURE & TRANSITION DIRECTIVE

- **Session 2 Status:** ARCHITECTURE LOCKED, SYNCED, AND CERTIFIED (2026).
- **Session 3 Focus:** Feature deployment, Module 9 (`docvaultrag.py`), Module 10 (`llmcascadecache.py`), and multi-agent live testing.
