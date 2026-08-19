import os
import sys
import json
import subprocess
import time
import difflib
import threading
import asyncio

# Auto-install dependencies if missing
required_packages = ["requests", "psutil", "pyautogui", "edge-tts", "pillow", "pytesseract"]
for package in required_packages:
    import_name = package
    if package == "pillow":
        import_name = "PIL"
    elif package == "pytesseract":
        import_name = "pytesseract"
    elif package == "edge-tts":
        import_name = "edge_tts"
        
    try:
        __import__(import_name)
    except ImportError:
        print(f"Installing missing dependency: {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

import requests
import psutil
import pyautogui
from PIL import Image
import pytesseract
import edge_tts

# Set safety settings for PyAutoGUI
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.1

# Configure PyTesseract standard installation paths on Windows
tess_paths = [
    r"C:\Program Files\Tesseract-OCR\tesseract.exe",
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
    r"C:\Users\Admin\AppData\Local\Tesseract-OCR\tesseract.exe"
]
for p in tess_paths:
    if os.path.exists(p):
        pytesseract.pytesseract.tesseract_cmd = p
        break

# Configuration
OLLAMA_URL = "http://localhost:11434/api/generate"
FAST_MODEL = "qwen2.5:1.5b"
REASONING_MODEL = "deepseek-r1:1.5b"
DEEP_MODEL = "grif-core"
EMBED_MODEL = "nomic-embed-text"
ALLOWED_DRIVE = "F:\\"

def is_safe_path(path):
    try:
        real_path = os.path.realpath(path)
        return real_path.upper().startswith(ALLOWED_DRIVE.upper())
    except Exception:
        return False

def resolve_smart_path(approx_name, base_dir="F:\\"):
    if not approx_name:
        return base_dir
        
    approx_name = os.path.normpath(approx_name)
    base_dir = os.path.normpath(base_dir)

    if os.path.exists(approx_name) and is_safe_path(approx_name):
        return approx_name

    if approx_name.upper().startswith(base_dir.upper()):
        search_dir = os.path.dirname(approx_name)
        target_name = os.path.basename(approx_name)
    else:
        search_dir = base_dir
        target_name = approx_name

    if not os.path.exists(search_dir) or not is_safe_path(search_dir):
        search_dir = base_dir

    all_paths = []
    try:
        for root, dirs, files in os.walk(search_dir):
            if not is_safe_path(root):
                continue
            for name in files + dirs:
                all_paths.append(os.path.join(root, name))
    except Exception:
        pass

    if not all_paths:
        return approx_name

    target_base, target_ext = os.path.splitext(target_name)

    # 1. Exact match with common extensions appended
    for ext in ['', '.txt', '.py', '.md', '.json']:
        test_name = target_name + ext if ext else target_name
        for p in all_paths:
            if os.path.basename(p).lower() == test_name.lower():
                return p

    # 2. Substring matching
    for p in all_paths:
        p_base, p_ext = os.path.splitext(os.path.basename(p))
        if os.path.isfile(p) and target_base.lower() == p_base.lower():
            return p

    # 3. Fuzzy matching
    p_bases = [os.path.splitext(os.path.basename(p))[0] for p in all_paths]
    matches = difflib.get_close_matches(target_base, p_bases, n=1, cutoff=0.75)
    if matches:
        matched_base = matches[0]
        for p in all_paths:
            p_base, p_ext = os.path.splitext(os.path.basename(p))
            if p_base == matched_base:
                return p

    return os.path.join(search_dir, target_name)

def read_file(path):
    path = resolve_smart_path(path)
    if not is_safe_path(path):
        return "Error: Access denied. Path must reside on F:\\"
    try:
        if not os.path.exists(path):
            return f"Error: File '{path}' does not exist."
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"

def write_file(path, content):
    path = resolve_smart_path(path)
    if not is_safe_path(path):
        return "Error: Access denied. Path must reside on F:\\"
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"File successfully written to '{path}'"
    except Exception as e:
        return f"Error writing file: {str(e)}"

def list_directory(path):
    path = resolve_smart_path(path)
    if not is_safe_path(path):
        return "Error: Access denied. Path must reside on F:\\"
    try:
        if not os.path.exists(path):
            return f"Error: Directory '{path}' does not exist."
        entries = os.listdir(path)
        return "\n".join(entries)
    except Exception as e:
        return f"Error listing directory: {str(e)}"

def visual_notepad_write(path, content):
    path = resolve_smart_path(path)
    if not is_safe_path(path):
        return "Error: Access denied. Path must reside on F:\\"
    try:
        # Write directly to prevent save-dialog hijacks
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
            
        print(f"[GUI Mode] Launching Notepad to display {path}...")
        # Open in notepad visually for the user
        subprocess.Popen(["notepad.exe", path])
        return f"Visual GUI task completed. File written and displayed via Notepad at: {path}"
    except Exception as e:
        return f"Error in Visual GUI mode: {str(e)}"

def launch_system_app(app_name: str) -> str:
    app_lower = app_name.lower().strip()
    try:
        if "chrome" in app_lower:
            subprocess.Popen(['start', 'chrome'], shell=True)
            return "Chrome launched successfully."
        elif "notepad" in app_lower:
            subprocess.Popen(['notepad.exe'])
            return "Notepad launched successfully."
        elif "calc" in app_lower or "calculator" in app_lower:
            subprocess.Popen(['calc.exe'])
            return "Calculator launched successfully."
        elif "explorer" in app_lower or "folder" in app_lower:
            parts = app_lower.split()
            path = "F:\\"
            for p in parts:
                if p.startswith("f:\\") or p.startswith("f:/"):
                    path = p
                    break
            path = resolve_smart_path(path)
            if is_safe_path(path):
                subprocess.Popen(['explorer.exe', path])
                return f"File Explorer opened at {path}."
            else:
                subprocess.Popen(['explorer.exe', 'F:\\'])
                return "File Explorer opened at F:\\."
        elif "cmd" in app_lower or "terminal" in app_lower or "powershell" in app_lower:
            subprocess.Popen(['cmd.exe', '/c', 'start'])
            return "Command Prompt launched successfully."
        else:
            subprocess.Popen(['start', app_lower], shell=True)
            return f"Attempted to launch {app_name}."
    except Exception as e:
        return f"Failed to launch app {app_name}: {str(e)}"

def get_diagnostics():
    try:
        cpu = psutil.cpu_percent(interval=0.5)
        mem = psutil.virtual_memory()
        processes = []
        for p in list(psutil.process_iter(['pid', 'name']))[:10]:
            processes.append(f"PID: {p.info['pid']} | Name: {p.info['name']}")
        
        diag = (
            f"System Diagnostics:\n"
            f"- CPU Utilization: {cpu}%\n"
            f"- Total RAM: {mem.total / (1024**3):.2f} GB\n"
            f"- Available RAM: {mem.available / (1024**3):.2f} GB\n"
            f"- Active Processes (Top 10):\n" + "\n".join(processes)
        )
        return diag
    except Exception as e:
        return f"Error getting diagnostics: {str(e)}"

def analyze_active_screen(query_context: str) -> str:
    temp_img_path = r"F:\AllWorkss_AI_Bridge\temp_screen.png"
    try:
        print("[Vision Mode] Capturing active monitor screenshot...")
        screenshot = pyautogui.screenshot()
        screenshot.save(temp_img_path)
        
        print("[Vision Mode] Processing OCR...")
        img = Image.open(temp_img_path)
        extracted_text = pytesseract.image_to_string(img)
        
        if not extracted_text.strip():
            extracted_text = "(No visible text or UI elements detected on active screen)"
            
        result = (
            f"--- Active Screen Capture Analysis ---\n"
            f"Query Context: {query_context}\n"
            f"Extracted UI/Screen Text:\n{extracted_text}\n"
            f"--------------------------------------"
        )
        return result
    except pytesseract.TesseractNotFoundError:
        return "Error: Tesseract OCR is not installed or configured. Please install Tesseract-OCR on your Windows machine."
    except Exception as e:
        return f"Error in screen capture/OCR analysis: {str(e)}"

def play_audio_thread(text: str):
    try:
        clean_text = ""
        in_code_block = False
        for line in text.split("\n"):
            if line.strip().startswith("```"):
                in_code_block = not in_code_block
                continue
            if not in_code_block:
                clean_line = line.replace("*", "").replace("#", "").replace("[", "").replace("]", "").replace("`", "")
                if clean_line.strip():
                    clean_text += clean_line + " "
        
        if not clean_text.strip():
            return

        async def amain():
            communicate = edge_tts.Communicate(clean_text, "hi-IN-SwaraNeural")
            temp_mp3 = r"F:\AllWorkss_AI_Bridge\temp_speech.mp3"
            await communicate.save(temp_mp3)
            
            escaped_path = os.path.abspath(temp_mp3).replace("\\", "\\\\")
            ps_cmd = (
                f'[System.Reflection.Assembly]::LoadWithPartialName("PresentationCore") | Out-Null; '
                f'$player = New-Object System.Windows.Media.MediaPlayer; '
                f'$player.Open("{escaped_path}"); '
                f'$player.Play(); '
                f'while ($player.NaturalDuration.HasTimeSpan -eq $false -or $player.Position -lt $player.NaturalDuration.TimeSpan) {{ Start-Sleep -Milliseconds 100 }}; '
                f'$player.Close()'
            )
            subprocess.run(["powershell", "-Command", ps_cmd], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            try:
                os.remove(temp_mp3)
            except Exception:
                pass
                
        asyncio.run(amain())
    except Exception as e:
        print(f"[TTS Error] {str(e)}")

def speak_response(text: str):
    t = threading.Thread(target=play_audio_thread, args=(text,))
    t.daemon = True
    t.start()

def get_embedding(text: str):
    try:
        payload = {"model": EMBED_MODEL, "prompt": text}
        r = requests.post("http://localhost:11434/api/embeddings", json=payload)
        if r.status_code == 200:
            return r.json().get("embedding")
    except Exception:
        pass
    return None

def semantic_search(query: str, target_dir="F:\\AllWorkss_AI_Bridge"):
    print(f"[Semantic Search] Running query embeddings for: '{query}'...")
    query_emb = get_embedding(query)
    if not query_emb:
        return "Error: Could not retrieve query embedding from Ollama nomic-embed-text."
    
    best_file = None
    best_sim = -1.0
    
    for root, dirs, files in os.walk(target_dir):
        if not is_safe_path(root):
            continue
        for name in files:
            if name.endswith(('.txt', '.md', '.py', '.json')):
                filepath = os.path.join(root, name)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read(1000)
                    if content.strip():
                        emb = get_embedding(content)
                        if emb:
                            dot = sum(a*b for a, b in zip(query_emb, emb))
                            norm_a = sum(a*a for a in query_emb)**0.5
                            norm_b = sum(b*b for b in emb)**0.5
                            sim = dot / (norm_a * norm_b)
                            if sim > best_sim:
                                best_sim = sim
                                best_file = filepath
                except Exception:
                    pass
    if best_file:
        return f"Top Match: {best_file} (Similarity: {best_sim:.4f})"
    return "No similar text files found in workspace."

def route_model(prompt: str) -> str:
    prompt_lower = prompt.lower()
    
    # App launcher routing
    launcher_keywords = ["open", "launch", "start", "notepad", "chrome", "calc", "calculator", "explorer", "cmd"]
    if any(kw in prompt_lower for kw in launcher_keywords):
        return FAST_MODEL

    emb_keywords = ["semantic search", "find similar", "embedding", "retrieve", "match document"]
    if any(kw in prompt_lower for kw in emb_keywords):
        return EMBED_MODEL

    gui_ocr_keywords = ["dikha ke", "screen pe", "live", "notepad open", "visual", "gui", 
                         "screen", "dekho", "graph", "chart", "ocr", "error dikh raha", "capture", "read screen"]
    if any(kw in prompt_lower for kw in gui_ocr_keywords):
        return FAST_MODEL

    fast_keywords = ["file", "banao", "write", "read", "ram", "cpu", "list", "status", "folder"]
    if len(prompt) < 100 or any(kw in prompt_lower for kw in fast_keywords):
        return FAST_MODEL
        
    reasoning_keywords = ["math", "solve", "algorithm", "think", "reasoning", "steps", "calculate", "fibonacci", "primes"]
    if any(kw in prompt_lower for kw in reasoning_keywords):
        return REASONING_MODEL
        
    return DEEP_MODEL

def execute_prompt(prompt):
    selected_model = route_model(prompt)
    
    if selected_model == FAST_MODEL:
        print("[Active Engine: Fast-1.5B (Speed Mode)]")
    elif selected_model == REASONING_MODEL:
        print("[Active Engine: Reasoning-1.5B (DeepSeek-R1 Mode)]")
    elif selected_model == EMBED_MODEL:
        print("[Active Engine: Nomic-Embed (Embedding Search Mode)]")
    else:
        print("[Active Engine: GRIF-Core-7B (Deep Mode)]")

    if selected_model == EMBED_MODEL:
        res = semantic_search(prompt)
        speak_response("Semantic search completed.")
        return res

    system_prompt = (
        "You are GRIF-Core, the private offline Systems Intelligence of AllWorkss.\n"
        "Creator & Chief Systems Architect: Yasar Intakhab Khan.\n"
        "INSTRUCTIONS:\n"
        "1. You MUST strictly extract the target file path and file content from the user's prompt.\n"
        "2. If the user asks to write/create a file using visual GUI mode (keywords like 'dikha ke', 'live', 'screen pe', 'visual', 'gui'), you MUST output the tool 'visual_notepad_write'.\n"
        "3. If the user asks to analyze their screen/capture/read active monitor, you MUST output the tool 'analyze_active_screen'.\n"
        "4. If the user asks to launch or open a system application (like Chrome, Notepad, Calculator, Cmd, Explorer, folder), you MUST output the tool 'launch_system_app' with the app_name parameter.\n"
        "5. If it is a purely conversational request (like greeting, introducing yourself, or small talk), answer naturally and concisely in English/Hinglish (e.g., 'Main GRIF-Core hoon, AllWorkss ka autonomous offline intelligence engine.') using the 'none' tool with your response.\n"
        "6. Format your response ONLY as a raw JSON instruction containing one of these tools:\n"
        "{\"tool\": \"visual_notepad_write\", \"path\": \"<EXTRACTED_PATH>\", \"content\": \"<EXTRACTED_CONTENT>\"}\n"
        "{\"tool\": \"write_file\", \"path\": \"<EXTRACTED_PATH>\", \"content\": \"<EXTRACTED_CONTENT>\"}\n"
        "{\"tool\": \"read_file\", \"path\": \"<EXTRACTED_PATH>\"}\n"
        "{\"tool\": \"list_directory\", \"path\": \"<EXTRACTED_PATH>\"}\n"
        "{\"tool\": \"get_diagnostics\"}\n"
        "{\"tool\": \"analyze_active_screen\", \"query_context\": \"<CONTEXT>\"}\n"
        "{\"tool\": \"launch_system_app\", \"app_name\": \"<APP_NAME>\"}\n"
        "{\"tool\": \"none\", \"response\": \"<CONVERSATIONAL_ANSWER>\"}\n"
        "Do not output anything other than this raw JSON."
    )
    
    payload = {
        "model": selected_model,
        "prompt": prompt,
        "system": system_prompt,
        "stream": False
    }
    try:
        r = requests.post(OLLAMA_URL, json=payload)
        if r.status_code == 200:
            response_text = r.json().get("response", "").strip()
            if "<think>" in response_text and "</think>" in response_text:
                think_block = response_text[response_text.find("<think>")+7:response_text.find("</think>")]
                print(f"[DeepSeek Thinking]: {think_block.strip()}")
                response_text = response_text[response_text.find("</think>")+8:].strip()
                
            try:
                action = json.loads(response_text)
                tool = action.get("tool")
                if tool == "read_file":
                    res = read_file(action.get("path"))
                elif tool == "write_file":
                    res = write_file(action.get("path"), action.get("content"))
                elif tool == "visual_notepad_write":
                    res = visual_notepad_write(action.get("path"), action.get("content"))
                elif tool == "list_directory":
                    res = list_directory(action.get("path"))
                elif tool == "get_diagnostics":
                    res = get_diagnostics()
                elif tool == "analyze_active_screen":
                    res = analyze_active_screen(action.get("query_context"))
                elif tool == "launch_system_app":
                    res = launch_system_app(action.get("app_name"))
                else:
                    res = action.get("response", response_text)
                
                speak_response(res)
                return f"Executed {tool or 'response'}:\n{res}"
            except json.JSONDecodeError:
                speak_response(response_text)
                return f"Response (Raw):\n{response_text}"
        else:
            return f"Error from Ollama: {r.status_code} {r.text}"
    except Exception as e:
        return f"Connection error: {str(e)}"

if __name__ == "__main__":
    print("==================================================")
    print("AllWorkss Secure Local Automation Bridge Running")
    print("==================================================")
    
    if len(sys.argv) > 1:
        prompt = " ".join(sys.argv[1:])
        print(f"Executing prompt: {prompt}")
        print(execute_prompt(prompt))
    else:
        print("Diagnostic self-check...")
        print(get_diagnostics())
        print("\nEntering interactive execution loop (Type 'exit' to quit):")
        while True:
            try:
                p = input("\nEnter prompt > ")
                if p.lower().strip() == 'exit':
                    break
                if p.strip():
                    print(execute_prompt(p))
            except KeyboardInterrupt:
                print("\n[!] Operation cancelled by user. Ready for next command.")
                continue
