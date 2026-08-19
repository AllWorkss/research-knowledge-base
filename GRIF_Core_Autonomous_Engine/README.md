# GRIF-Core Autonomous AI Engine & Automation Bridge

This folder contains the complete engineering report, configuration reference files, and architecture breakdown for the **GRIF-Core Autonomous AI Bridge** deployed on August 20, 2026.

## Session Accomplishments & Deployments

During this session, we built and stabilized a production-grade local AI orchestration pipeline for the AllWorkss ecosystem. The deployment has been fully configured, hardened, and verified.

### 1. Key Engineering Deliverables
*   **`agent_core.py` (Secure Local Automation Bridge):**
    *   Fuses local LLMs with system files, diagnostics tools, and GUI subprocesses.
    *   Features a **Smart Fuzzy Path Resolver** with a strict `0.75` cutoff to dynamically match user-specified paths without false-positive extensions matching.
    *   Implements **Dual-Mode Execution** (Visual GUI Notepad launcher vs silent background file I/O).
    *   Secured inside the `F:\` drive sandbox.
    *   Features graceful `KeyboardInterrupt` (Ctrl+C) handling to prevent terminal crashes.
*   **`Modelfile` (Custom GRIF-Core Brain):**
    *   Configures `grif-core` using `qwen2.5:7b` as the base model, fine-tuning parameters (temp=0.6, top_p=0.9), and loading system prompts tailored for AllWorkss executive operations.
*   **1-Click Desktop Launcher (`Start_GRIF_Brain.bat`):**
    *   Generates a convenient terminal launcher on the Windows Desktop for quick execution.
*   **Auto-Installing Bootstrapper:**
    *   Dynamically checks and installs required modules (`requests`, `psutil`, `pyautogui`, `edge-tts`, `pillow`, `pytesseract`) at runtime.
*   **PowerShell Asynchronous TTS Engine:**
    *   Bypasses complex C-compilation blocks in Python 3.14 (associated with Pygame) by leveraging Windows' native `MediaPlayer` API asynchronously.

### 2. Multi-Tier Model Routing Matrix
The bridge dynamically routes prompts across **4 active local model engines** using Ollama:
1.  **Fast Tier (`qwen2.5:1.5b`):** Dispatched for sub-second file management, GUI automation triggers, diagnostics, and app launching.
2.  **Reasoning Tier (`deepseek-r1:1.5b`):** Dispatched for chain-of-thought calculation, algorithmic analysis, and logical checks.
3.  **Architect Tier (`grif-core:7b`):** Dispatched for heavy coding, full-stack Next.js/FastAPI construction, and architectural refactoring.
4.  **Embedding Tier (`nomic-embed-text`):** Dispatched for local semantic search and document retrieval across workspace directories.

---

## Folder Contents
*   [`ALLWORKSS_GRIF_AUTONOMOUS_ENGINE_REPORT.pdf`](ALLWORKSS_GRIF_AUTONOMOUS_ENGINE_REPORT.pdf): The formal corporate engineering report detailing the deployment metrics, system resources, and technical specifications.
*   [`agent_core_reference.py`](agent_core_reference.py): A versioned copy of the active secure automation bridge script.
*   [`Modelfile_reference`](Modelfile_reference): The configuration file used to build the custom `grif-core` Ollama image.
*   [`README.md`](README.md): This file (session review and file directory guide).

---
**Chief Systems Architect:** Yasar Intakhab Khan  
**Brand:** AllWorkss (OPC) Private Limited  
**Status:** 100% Deployed & Operational (Production Ready)
